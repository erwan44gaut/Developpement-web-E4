import sqlite3
from flask import Blueprint, request, jsonify
from db import get_db
import datetime
import utils.jwt_utils

quiz_bp = Blueprint('quiz', __name__)
@quiz_bp.route('/quiz-info', methods=['GET'])
def get_quiz_info():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM questions")
    quiz_size = cursor.fetchone()[0]

    cursor.execute("""
    SELECT username, score
    FROM participations
    ORDER BY score DESC, timestamp ASC
    """)
    scores = [{"playerName": row[0], "score": row[1]} for row in cursor.fetchall()]

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
    print(question)
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
    username = payload['username']
    answers = payload['answers']

    cursor = db.cursor()
    correct_answers = 0

    for answer in answers:
        question_id = answer['question_id']
        answer_id = answer['answer_id']
        cursor.execute("SELECT is_correct FROM answers WHERE answer_id = ?", (answer_id,))
        is_correct = cursor.fetchone()[0]
        if is_correct:
            correct_answers += 1

    score = correct_answers
    timestamp = datetime.datetime.now()
    
    cursor.execute("INSERT INTO participations (username, score, timestamp) VALUES (?, ?, ?)", 
                   (username, score, timestamp))
    participation_id = cursor.lastrowid

    for answer in answers:
        cursor.execute("INSERT INTO participation_answers (participation_id, question_id, answer_id) VALUES (?, ?, ?)", 
                       (participation_id, answer['question_id'], answer['answer_id']))
    
    db.commit()
    return jsonify({"message": "Participation submitted successfully", "score": score}), 201

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

    cursor.execute("""
    INSERT INTO questions (question_title, question_text, image_url, position)
    VALUES (?, ?, ?, ?)
    """, (question_title, question_text, image_url, position))
    question_id = cursor.lastrowid

    for answer in possible_answers:
        cursor.execute("""
        INSERT INTO answers (question_id, answer_text, is_correct)
        VALUES (?, ?, ?)
        """, (question_id, answer['text'], answer['isCorrect']))

    db.commit()
    return jsonify({"id": question_id}), 200

@quiz_bp.route('/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
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
                # Shift positions down for questions between current and new position
                cursor.execute("""
                UPDATE questions
                SET position = position - 1
                WHERE position > ? AND position <= ?
                """, (current_position, new_position))
            else:
                # Shift positions up for questions between new and current position
                cursor.execute("""
                UPDATE questions
                SET position = position + 1
                WHERE position >= ? AND position < ?
                """, (new_position, current_position))

            # Update the question's position to the new value
            cursor.execute("UPDATE questions SET position = ? WHERE question_id = ?", (new_position, question_id))

        # Update the rest of the question's details
        cursor.execute("""
        UPDATE questions
        SET question_title = ?, question_text = ?, image_url = ?
        WHERE question_id = ?
        """, (question_title, question_text, image_url, question_id))

        # Delete existing answers and insert the new ones
        cursor.execute("DELETE FROM answers WHERE question_id = ?", (question_id,))
        for answer in possible_answers:
            cursor.execute("""
            INSERT INTO answers (question_id, answer_text, is_correct)
            VALUES (?, ?, ?)
            """, (question_id, answer['text'], answer['isCorrect']))

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
    cursor.execute("SELECT * FROM questions WHERE question_id = ?", (question_id,))
    result = cursor.fetchone()

    if result is None:
        return jsonify({"error": "Question not found"}), 404


    db = get_db()
    cursor = db.cursor()

    cursor.execute("DELETE FROM questions WHERE question_id = ?", (question_id,))
    cursor.execute("DELETE FROM answers WHERE question_id = ?", (question_id,))
    
    db.commit()
    return "", 204

@quiz_bp.route('/questions/all', methods=['DELETE'])
def delete_all_questions():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not utils.jwt_utils.decode_token(auth_header):
        return jsonify({"error": "Unauthorized"}), 401

    db = get_db()
    cursor = db.cursor()

    cursor.execute("DELETE FROM questions")
    cursor.execute("DELETE FROM answers")

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