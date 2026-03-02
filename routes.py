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
                flash('se envio correctamente', 'success')
                return redirect(url_for('index'))
            return render_template('sobrenosotros.html', form=formulario)

#----- Nuevas rutas ---
#---ver tareas---



#--- Editar-------
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



@app.route('/saludo')
def saludo():
        return 'Hola bienvenido a Taller Apps '
    
@app.route('/usuario/<nombre>')
def usuario(nombre):
        return f'Hola{nombre} bienvenido a Taller Apps '
