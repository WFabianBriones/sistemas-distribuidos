#!/usr/bin/env python3 
from db_config import get_db_connection
import psycopg2.extras

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM posts') 
    posts = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', postsHtml=posts)

@app.route('/add')
def add_post():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO posts(title, content) VALUES (%s, %s)', ('Primer post', 'Este es el contenido del primer post'))
    conn.commit()
    cur.close()
    conn.close()
    return 'Post añadido'

if __name__ == '__main__':
    app.run(debug=True)




