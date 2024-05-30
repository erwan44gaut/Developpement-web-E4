from flask import Blueprint, jsonify
from db import get_db

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/quiz-info', methods=['GET'])
def get_quiz_info():
    return jsonify({"size": 0, "scores": []}), 200

@quiz_bp.route('/', methods=['GET'])
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM table_name")
    rows = cursor.fetchall()
    return str(rows)