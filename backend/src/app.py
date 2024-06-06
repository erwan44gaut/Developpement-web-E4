from flask import Flask
from flask_cors import CORS
from config import Config
from routes.quiz import quiz_bp
from routes.auth import auth_bp
from routes.db import db_bp

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

app.register_blueprint(quiz_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(db_bp)

@app.route('/quizz-space')
def quizz_space():
    return 'Quizz Space'

if __name__ == '__main__':
    app.run(debug=True)
