#!/usr/bin/env python3 
from db_config import get_db_connection
import psycopg2.extras
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    conn = get_db_connection()
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cur.execute('SELECT * FROM posts;')
    posts = cur.fetchall()
    conn.close()
    return render_template('index.html', postsHtml=posts)

# Add a new post
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = get_db_connection()
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
        
        cur.execute('INSERT INTO posts (title, content) VALUES (%s,%s);', (title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')

# Edit/update an existing post
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cur.execute('SELECT * FROM posts WHERE id = %s', (id,))
    post = cur.fetchone()

    if post is None:
        conn.close()
        return "Post not found!", 404

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute('UPDATE posts SET title = %s, content = %s WHERE id = %s', (title, content, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('edit.html', post=post)

# Delete a post
@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('DELETE FROM posts WHERE id = %s', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
