#!/usr/bin/env python3 
from flask import Flask, request, render_template, redirect
from confluent_kafka import Producer
import json

app = Flask(__name__)

producer = Producer({'bootstrap.servers': 'localhost:9092'})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    mensaje = request.form['mensaje']
    producer.produce('messages', json.dumps({'mensaje': mensaje}))
    producer.flush()
    return redirect('/')

# Ruta para mostrar datos
@app.route('/ver')
def ver():
    # Aquí iría la lógica para leer de PostgreSQL y SQLite
    return "Aquí se mostrarán los datos de ambas bases"

# from flask import Flask, request, render_template, redirect
# from confluent_kafka import Producer
# import json

# app = Flask(__name__)

# producer = Producer({'bootstrap.servers': 'localhost:9092'})

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     mensaje = request.form['mensaje']

#     try:
#         # Envía el mensaje a Kafka codificado como JSON
#         producer.produce('messages', json.dumps({'mensaje': mensaje}))
#         producer.flush()
#         return redirect('/')
#     except Exception as e:
#         return f"⚠️ Error al enviar a Kafka: {str(e)}"
