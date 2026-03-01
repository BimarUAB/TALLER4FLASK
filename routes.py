from app import app, db
from flask import render_template
import formularios
from models import Tarea

@app.route('/')
@app.route('/index')
def index():
        return render_template('index.html', subtitulo = "Actidad en grupo TAI")

@app.route('/sobrenosotros', methods = ['GET', 'POST'])
def sobrenosotros():
        formulario = formularios.FormAgregarTareas()
        if formulario.validate_on_submit() :
                nueva_tarea = Tarea (titulo =  formulario.titulo.data)
                db.session.add(nueva_tarea)
                db.session.commit()
                print('se envio correctamente', formulario.titulo.data)
                return render_template('sobrenosotros.html', 
                                       form = formulario,
                                       titulo = formulario.titulo.data)
        return render_template('sobrenosotros.html', form = formulario)

"""Ruta para eliminar"""

@app.route('/eliminar/<int:id>', methods=['POST'])

def eliminar_tarea(id):
    tarea =  Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    flash('Tarea eliminada correctamente', 'success')
    return redirect(url_for('mostrar_tareas'))


@app.route('/saludo')
def saludo():
        return 'Hola bienvenido a Taller Apps '
    
@app.route('/usuario/<nombre>')
def usuario(nombre):
        return f'Hola{nombre} bienvenido a Taller Apps '
