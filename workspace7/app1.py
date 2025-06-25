#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, session, make_response
import os
from werkzeug.utils import secure_filename
from weasyprint import HTML

app = Flask(__name__)
app.secret_key = 'clave_super_secreta'

# Configuración para subir imágenes
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Crear carpeta si no existe
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.to_dict()

        # Procesar imagen
        if 'foto' in request.files:
            foto = request.files['foto']
            if foto and foto.filename != '':
                filename = secure_filename(foto.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                foto.save(filepath)
                data['foto_url'] = os.path.join('uploads', filename)

        # Guardar datos en sesión y redirigir
        session['cv_data'] = data
        return redirect(url_for("mostrar_cv"))

    return render_template("index.html")

@app.route("/cv")
def mostrar_cv():
    data = session.get("cv_data")
    if not data:
        return redirect(url_for("index"))
    return render_template("cv.html", data=data)

@app.route("/cv/pdf")
def mostrar_cv_pdf():
    data = session.get("cv_data")
    if not data:
        return redirect(url_for("index"))
    
    # Renderiza el HTML con Jinja2
    html_out = render_template("cv.html", data=data)
    
    # Genera el PDF desde el HTML
    pdf = HTML(string=html_out, base_url=request.base_url).write_pdf()
    
    # Crea la respuesta con el PDF para mostrarlo inline en el navegador
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=cv.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)

