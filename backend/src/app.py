from flask import Flask
from config import Config
from routes.quiz import quiz_bp
from routes.auth import auth_bp
from routes.db import db_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(quiz_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(db_bp)

if __name__ == '__main__':
    app.run(debug=True)
