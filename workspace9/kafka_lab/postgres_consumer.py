#!/usr/bin/env python3 
import psycopg2

conn = psycopg2.connect(
    dbname="replicated_db",
    user="uleam",
    password="uleam20251",
    host="127.0.0.1"
)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS mensajes (id SERIAL PRIMARY KEY, mensaje TEXT)')
conn.commit()

consumer = Consumer({
    'bootstrap.servers': '127.0.0.1:9092',
    'group.id': 'grupo_postgresql',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe(['messages'])


while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Error:", msg.error())
        continue

    data = json.loads(msg.value().decode('utf-8'))
    cursor.execute('INSERT INTO mensajes (mensaje) VALUES (%s)', (data['mensaje'],))
    conn.commit()
