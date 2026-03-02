from app import app, db
from flask import render_template, redirect, url_for, request, flash
import formularios
from models import Tarea

@app.route('/')
@app.route('/index')
def index():
    # Obtenemos todas las tareas para mostrarlas en el inicio
    tareas = Tarea.query.all()
    return render_template('index.html', subtitulo="Actividad en grupo TAI", tareas=tareas)

@app.route('/sobrenosotros', methods=['GET', 'POST'])
def sobrenosotros():
    formulario = formularios.FormAgregarTareas()
    if formulario.validate_on_submit():
        nueva_tarea = Tarea(titulo=formulario.titulo.data)
        db.session.add(nueva_tarea)
        db.session.commit()
        flash('Tarea agregada correctamente', 'success')
        return redirect(url_for('index'))
    return render_template('sobrenosotros.html', form=formulario)

# --- NUEVAS RUTAS ---

@app.route('/tareas')
def mostrar_tareas():
    """Muestra todas las tareas en una lista dedicada"""
    tareas = Tarea.query.all()
    return render_template('tareas.html', tareas=tareas)

@app.route('/tarea/<int:id>')
def ver_tarea(id):
    """Muestra el detalle de una sola tarea"""
    tarea = Tarea.query.get_or_404(id)
    return render_template('ver_tarea.html', tarea=tarea)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_tarea(id):
    """Edita una tarea existente"""
    tarea = Tarea.query.get_or_404(id)
    formulario = formularios.FormAgregarTareas(obj=tarea)
    
    if formulario.validate_on_submit():
        tarea.titulo = formulario.titulo.data
        db.session.commit()
        flash('Tarea actualizada correctamente', 'success')
        return redirect(url_for('mostrar_tareas'))
    
    return render_template('sobrenosotros.html', form=formulario, editar=True)

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_tarea(id):
    """Elimina una tarea"""
    tarea = Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    flash('Tarea eliminada correctamente', 'success')
    return redirect(url_for('mostrar_tareas'))

@app.route('/saludo')
def saludo():
    return 'Hola bienvenido a Taller Apps'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Hola {nombre} bienvenido a Taller Apps'