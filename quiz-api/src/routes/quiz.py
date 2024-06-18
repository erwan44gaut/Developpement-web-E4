import sqlite3
from flask import Blueprint, request, jsonify
from db import get_db
import datetime
import utils.jwt_utils
import glob
import os
import random

quiz_bp = Blueprint('quiz', __name__)
@quiz_bp.route('/quiz-info', methods=['GET'])
def get_quiz_info():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM questions")
    quiz_size = cursor.fetchone()[0]

    cursor.execute("""
    SELECT playerName, score, avatarName
    FROM participations
    ORDER BY score DESC, timestamp ASC
    """)
    scores = [{"playerName": row[0], "score": row[1], "avatarName":row[2]} for row in cursor.fetchall()]

    return jsonify({"size": quiz_size, "scores": scores}), 200

@quiz_bp.route('/questions/<int:question_id>', methods=['GET'])
def get_question_by_id(question_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM questions WHERE question_id = ?", (question_id,))
    question = cursor.fetchone()

    if question:
        cursor.execute("SELECT * FROM answers WHERE question_id = ?", (question_id,))
        answers = cursor.fetchall()
        return jsonify({
            "id": question_id,
            "title": question[1],
            "text": question[2],
            "image": question[3],
            "position": question[4],
            "possibleAnswers": [{"answer_id": ans[0], "text": ans[2], "isCorrect": bool(ans[3])} for ans in answers]
        }), 200
    else:
        return jsonify({"error": "Question not found"}), 404

@quiz_bp.route('/questions', methods=['GET'])
def get_question_by_position():
    position = request.args.get('position')
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM questions WHERE position = ?", (position,))
    question = cursor.fetchone()
    if question:
        cursor.execute("SELECT * FROM answers WHERE question_id = ?", (question[0],))
        answers = cursor.fetchall()

        return jsonify({
            "id": question[0],
            "title": question[1],
            "text": question[2],
            "image": question[3],
            "position": question[4],
            "possibleAnswers": [{"answer_id": ans[0], "text": ans[2], "isCorrect": bool(ans[3])} for ans in answers]
        }), 200
    else:
        return jsonify({"error": "Question not found"}), 404

@quiz_bp.route('/participations', methods=['POST'])
def submit_participation():
    db = get_db()
    payload = request.get_json()
    username = payload['playerName']
    answers = payload['answers']
    avatarName = payload.get('avatarName')
    if not avatarName:
        files = glob.glob(os.path.join('../../public/grades', '*.png'))
        if files:
            selected_file = random.choice(files)
            avatarName = selected_file.split('.png')[0]
        else:
            avatarName = None

    cursor = db.cursor()
    cursor.execute("SELECT question_id FROM questions ORDER BY position")
    questions = cursor.fetchall()
    
    if(len(questions)>len(answers)):
        return 'Participation incomplete', 400
    
    if(len(questions)<len(answers)):
        return 'Participation overcomplete', 400
    
    correct_answers = 0
    answers_id = []
    print(questions)
    for i in range(len(answers)) :
        cursor.execute("SELECT answer_id, is_correct FROM answers WHERE question_id = ?", questions[i])
        answers_per_question = cursor.fetchall()
        answer_id, isCorrect = answers_per_question[answers[i]-1]
        if isCorrect :
            correct_answers+=1
        answers_id.append(answer_id)
        

    score = correct_answers
    timestamp = datetime.datetime.now()
    
    cursor.execute("INSERT INTO participations (playerName, avatarName, score, timestamp) VALUES (?, ?, ?, ?)", 
                   (username, avatarName, score, timestamp))
    participation_id = cursor.lastrowid

    for i in range (len(answers)):
        cursor.execute("INSERT INTO participation_answers (participation_id, answer_id) VALUES (?, ?)", 
                       (participation_id, answers_id[i]))
    
    db.commit()
    return jsonify({"message": "Participation submitted successfully", "score": score, "playerName":username, "avatarName":avatarName}), 200

@quiz_bp.route('/questions', methods=['POST'])
def create_question():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not utils.jwt_utils.decode_token(auth_header):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    question_title = data['title']
    question_text = data['text']
    image_url = data['image']
    position = data['position']
    possible_answers = data['possibleAnswers']

    db = get_db()
    cursor = db.cursor()

    try:
        # Start a transaction
        db.execute("BEGIN")
        print("Transaction started")

        # Shift positions up for questions at and after the new position, starting from the bottom
        cursor.execute("""
        SELECT MAX(position) FROM questions WHERE position >= ?
        """, (position,))
        max_position = cursor.fetchone()[0]
        
        if max_position is not None:
            for pos in range(max_position, position - 1, -1):
                cursor.execute("""
                UPDATE questions
                SET position = position + 1
                WHERE position = ?
                """, (pos,))

        print("Positions shifted up")

        # Insert the new question
        cursor.execute("""
        INSERT INTO questions (question_title, question_text, image_url, position)
        VALUES (?, ?, ?, ?)
        """, (question_title, question_text, image_url, position))
        question_id = cursor.lastrowid
        print(f"Inserted new question with ID: {question_id}")

        # Insert possible answers
        for answer in possible_answers:
            cursor.execute("""
            INSERT INTO answers (question_id, answer_text, is_correct)
            VALUES (?, ?, ?)
            """, (question_id, answer['text'], answer['isCorrect']))
        print("Inserted possible answers")

        # Commit the transaction
        db.commit()
        print("Transaction committed")
        return jsonify({"id": question_id}), 200

    except sqlite3.IntegrityError as e:
        db.rollback()
        print("Database error: " + str(e))
        return jsonify({"error": "Database error: " + str(e)}), 500

    except Exception as e:
        db.rollback()
        print("Server error: " + str(e))
        return jsonify({"error": "Server error: " + str(e)}), 500

@quiz_bp.route('/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    print("a")
    auth_header = request.headers.get('Authorization')
    if not auth_header or not utils.jwt_utils.decode_token(auth_header):
        return jsonify({"error": "Unauthorized"}), 401

    db = get_db()
    cursor = db.cursor()

    # Fetch the current position and check if the question exists
    cursor.execute("SELECT position FROM questions WHERE question_id = ?", (question_id,))
    result = cursor.fetchone()

    if result is None:
        return jsonify({"error": "Question not found"}), 404

    current_position = result[0]

    data = request.get_json()
    question_title = data.get('title')
    question_text = data.get('text')
    image_url = data.get('image')
    new_position = data.get('position')
    possible_answers = data.get('possibleAnswers')

    try:
        # Start a transaction
        db.execute("BEGIN")

        if current_position != new_position:
            # Temporarily set the position to a unique value to avoid conflicts
            temp_position = -1
            cursor.execute("UPDATE questions SET position = ? WHERE question_id = ?", (temp_position, question_id))
            if current_position < new_position:
                for pos in range(current_position+1,new_position+1) :
                    cursor.execute("""
                    UPDATE questions
                    SET position = position - 1
                    WHERE position = ?
                    """, (pos,))
            else:
                for pos in range(current_position-1, new_position-1,-1):
                    print("pos ::" +str(pos))
                    cursor.execute("""
                    UPDATE questions
                    SET position = position + 1
                    WHERE position = ?
                    """, (pos,))

            # Update the question's position to the new value
            cursor.execute("UPDATE questions SET position = ? WHERE question_id = ?", (new_position, question_id))

        # Update the rest of the question's details
        cursor.execute("""
        UPDATE questions
        SET question_title = ?, question_text = ?, image_url = ?
        WHERE question_id = ?
        """, (question_title, question_text, image_url, question_id))

        cursor.execute("SELECT answer_id,answer_text,is_correct FROM answers WHERE question_id = ?",(question_id,))
        answers = cursor.fetchall()
        answer_without_id = [answer[1:] for answer in answers]
        new_answers = [(answer['text'],answer['isCorrect']) for answer in possible_answers]
        
        #Delete answer
        if len(answers)>len(new_answers) :
            for answer in answers :
                if answer[1:] not in answers :
                    cursor.execute("DELETE FROM participation_answers WHERE answer_id = ?",(answer[0],))
                    cursor.execute("DELETE FROM answers where answer_id = ?",(answer[0],))
                    break
                    
                    
        elif len(answers)<len(new_answers) :
            cursor.execute("""
                INSERT INTO answers (question_id, answer_text, is_correct)
                VALUES (?, ?, ?)
                """, (question_id, new_answers[-1][0], new_answers[-1][1]))
        
        else :
            for index,answer in enumerate(answers):
                if answer[1:]!=new_answers[index]:
                    cursor.execute("DELETE FROM participation_answers WHERE answer_id = ?",(answer[0],))
                    cursor.execute("""
                        UPDATE answers
                        SET answer_text = ?, is_correct = ?
                        WHERE answer_id = ?
                        """, (new_answers[index][0],new_answers[index][1],answer[0],))
                
        # Commit the transaction
        db.commit()
        return "", 204

    except sqlite3.IntegrityError as e:
        db.rollback()
        return jsonify({"error": "Database error: " + str(e)}), 500

    except Exception as e:
        db.rollback()
        return jsonify({"error": "Server error: " + str(e)}), 500

@quiz_bp.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not utils.jwt_utils.decode_token(auth_header):
        return jsonify({"error": "Unauthorized"}), 401

    db = get_db()
    cursor = db.cursor()

    # Fetch the current position and check if the question exists
    cursor.execute("SELECT position FROM questions WHERE question_id = ?", (question_id,))
    result = cursor.fetchone()

    if result is None:
        return jsonify({"error": "Question not found"}), 404

    current_position = result[0]

    try:
        # Start a transaction
        db.execute("BEGIN")

        # Delete the question and its answers
        cursor.execute("DELETE FROM questions WHERE question_id = ?", (question_id,))
        cursor.execute("""
            DELETE FROM participation_answers 
            WHERE answer_id IN (
                SELECT answer_id FROM answers WHERE question_id = ?
            )
        """, (question_id,))
        cursor.execute("DELETE FROM answers WHERE question_id = ?", (question_id,))
        
        cursor.execute("""
            SELECT MAX(position) FROM questions """, )
        max_position = cursor.fetchone()[0]
        # Shift positions down for questions after the deleted position
        # Verify is there is still values after ther delete
        if max_position :
            for pos in range (current_position+1,max_position+1) :
                cursor.execute("""
                UPDATE questions
                SET position = position - 1
                WHERE position = ?
                """, (pos,))
        # Commit the transaction
        db.commit()
        return "", 204

    except sqlite3.IntegrityError as e:
        db.rollback()
        return jsonify({"error": "Database error: " + str(e)}), 500

    except Exception as e:
        db.rollback()
        return jsonify({"error": "Server error: " + str(e)}), 500

@quiz_bp.route('/questions/all', methods=['DELETE'])
def delete_all_questions():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not utils.jwt_utils.decode_token(auth_header):
        return jsonify({"error": "Unauthorized"}), 401

    db = get_db()
    cursor = db.cursor()

    cursor.execute("DELETE FROM questions")
    cursor.execute("DELETE FROM answers")
    cursor.execute("DELETE FROM participation_answers")

    db.commit()
    return "", 204

@quiz_bp.route('/participations/all', methods=['DELETE'])
def delete_all_participations():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not utils.jwt_utils.decode_token(auth_header):
        return jsonify({"error": "Unauthorized"}), 401

    db = get_db()
    cursor = db.cursor()

    cursor.execute("DELETE FROM participations")
    cursor.execute("DELETE FROM participation_answers")

    db.commit()
    return "", 204

@quiz_bp.route('/participation-answers/<int:question_id>', methods=['GET'])
def get_participation_answers_by_question_id(question_id):
    db = get_db()
    cursor = db.cursor()
    
    # Exécution de la requête JOIN avec COUNT et GROUP BY
    cursor.execute("""
        SELECT
            a.is_correct,
            COUNT(pa.participation_answer_id) AS answer_count
        FROM
            answers a
        JOIN
            participation_answers pa ON a.answer_id = pa.answer_id
        WHERE
            a.question_id = ?
        GROUP BY
            a.is_correct
        ORDER BY
            a.is_correct;
    """, (question_id,))
    
    # Initialisation des compteurs
    is_correct_count = 0
    is_not_correct_count = 0
    
    # Récupération des résultats
    results = cursor.fetchall()
    
    # Mise à jour des compteurs en fonction des résultats
    for row in results:
        if row[0] == 1:
            is_correct_count = row[1]
        else:
            is_not_correct_count = row[1]
    
    # Préparation des données pour le JSON
    participation_answers = {
        "is_correct": is_correct_count,
        "is_not_correct": is_not_correct_count
    }
    
    return jsonify(participation_answers), 200
    