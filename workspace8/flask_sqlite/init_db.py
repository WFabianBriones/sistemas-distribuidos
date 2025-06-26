import sqlite3


connection=sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cor=connection.cursor()

cor.execute('INSERT INTO posts (title,content) VALUES(?,?)',
('FIRST post', 'CONTENT FOR THE FIRST POST'))

cor.execute('INSERT INTO posts (title,content) VALUES(?,?)',
('SECOND post', 'CONTENT FOR THE SECOND POST'))

connection.commit()
connection.close()