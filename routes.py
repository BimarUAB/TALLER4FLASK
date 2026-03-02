from app import app, db
from flask import render_template, redirect, url_for, request, flash
import formularios
from models import Tarea

@app.route('/')
@app.route('/index')
def index():
        #Obtenemos todas las tareas para mostrarlas en el inicio
        tareas = Tarea.query.all()
        return render_template('index.html', subtitulo = "Actidad en grupo TAI", tareas=tareas)

@app.route('/sobrenosotros', methods = ['GET', 'POST'])
def sobrenosotros():
        formulario = formularios.FormAgregarTareas()
        if formulario.validate_on_submit() :
                nueva_tarea = Tarea (titulo =  formulario.titulo.data)
                db.session.add(nueva_tarea)
                db.session.commit()

@app.route('/saludo')
def saludo():
        return 'Hola bienvenido a Taller Apps '
    
@app.route('/usuario/<nombre>')
def usuario(nombre):
        return f'Hola{nombre} bienvenido a Taller Apps '
