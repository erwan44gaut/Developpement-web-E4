from flask import Flask, g
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = '../db/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM table_name")
    rows = cursor.fetchall()
    return str(rows)

if __name__ == '__main__':
    app.run(debug=True)
