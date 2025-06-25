#!/usr/bin/env python3
from flask import Flask, render_template, request
# from importlib.metadata import version


# versionfl = version("flask")
# print('La versión de Flask es:', versionfl)
# print('ok')

app = Flask(__name__)

@app.route("/")
def index():
    return "hello word from flask"

@app.route("/pn")
def pn():
    return render_template('hello.html',nameHtml='Fabian')

@app.route("/loop")
def loop():
    # Obtener el número desde los parámetros de la URL, por ejemplo: /loop?limite=5
    limite = request.args.get("limite", default=30, type=int)  # por defecto 10 si no se indica
    # http://localhost:5000/loop?limite=25

    # Generar la lista de números del 1 al limite
    numeros = list(range(1, limite + 1))

    return render_template('loop.html', numeros=numeros)



@app.route("/sumar")
def sumar():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    # http://localhost:5000/sumar?a=7&b=5

    
    if a is None or b is None:
        return "Por favor envía los parámetros 'a' y 'b' en la URL", 400
    
    resultado = a + b
    return render_template("sumar.html", a=a, b=b, resultado=resultado)


# @app.route("/about")
# def about():
#     return "this is about"

@app.route("/home")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




