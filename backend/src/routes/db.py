from flask import Blueprint, request, jsonify
from db import get_db
import datetime
import utils.jwt_utils

db_bp = Blueprint('database', __name__)

@db_bp.route('/rebuild-db', methods=['POST'])
def rebuild_db():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS questions")
    cursor.execute("DROP TABLE IF EXISTS answers")
    cursor.execute("DROP TABLE IF EXISTS participations")
    cursor.execute("DROP TABLE IF EXISTS participation_answers")

    cursor.execute("""
    CREATE TABLE questions (
        question_id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_title TEXT NOT NULL,
        question_text TEXT NOT NULL,
        image_url TEXT,
        position INTEGER NOT NULL UNIQUE
    )
    """)
    cursor.execute("""
    CREATE TABLE answers (
        answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_id INTEGER NOT NULL,
        answer_text TEXT NOT NULL,
        is_correct BOOLEAN NOT NULL,
        FOREIGN KEY (question_id) REFERENCES questions (question_id)
    )
    """)
    cursor.execute("""
    CREATE TABLE participations (
        participation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        score INTEGER NOT NULL,
        timestamp DATETIME NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE participation_answers (
        participation_answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        participation_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        answer_id INTEGER NOT NULL,
        FOREIGN KEY (participation_id) REFERENCES participations (participation_id),
        FOREIGN KEY (question_id) REFERENCES questions (question_id),
        FOREIGN KEY (answer_id) REFERENCES answers (answer_id)
    )
    """)
    db.commit()

    return "Ok", 200
