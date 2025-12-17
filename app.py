from flask import Flask, render_template
import os
import sqlite3

db_path = "data/reviews.db"
db_schema = """
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT
        name TEXT NOT NULL
        review TEXT NOT NULL 
    )
"""


app = Flask(__name__)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute(db_schema)
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8653)) 
    app.run(host='0.0.0.0', port=port)