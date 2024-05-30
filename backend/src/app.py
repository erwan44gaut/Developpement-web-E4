from flask import Flask
from config import Config
from routes.quiz import quiz_bp
from routes.auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(quiz_bp)
app.register_blueprint(auth_bp)

@app.route('/quizz-space')
def quizz_space():
    return 'Quizz Space'

if __name__ == '__main__':
    app.run(debug=True)
