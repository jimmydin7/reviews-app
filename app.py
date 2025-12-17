from flask import Flask, render_template, request, jsonify
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


@app.post('/reviews')
def create_review():
    data = request.get_json()
    name = data.get('name')
    review = data.get('review')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO reviews (name, review) VALUES (?, ?)', (name, review))
    conn.commit()
    conn.close()


@app.get('/reviews')
def get_reviews():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, review FROM reviews')
    rows = cursor.fetchall()
    conn.close()

    reviews = [{'id': row[0], 'name': row[1], 'review': row[2]} for row in rows]
    return jsonify(reviews)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8653)) 
    app.run(host='0.0.0.0', port=port)