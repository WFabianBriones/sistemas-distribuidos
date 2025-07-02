#!/usr/bin/env python3 
import sqlite3
from confluent_kafka import Consumer
import json

conn = sqlite3.connect('local.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS mensajes (mensaje TEXT)')
conn.commit()

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'grupo_sqlite',
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
    cursor.execute('INSERT INTO mensajes (mensaje) VALUES (?)', (data['mensaje'],))
    conn.commit()
