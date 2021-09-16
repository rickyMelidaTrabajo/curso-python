import os
from flask import Flask, render_template, request
#from werkzeug import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './archivos'


@app.route('/')
def index():
    return 'Hola formulario de files'

@app.route('/recibe-datos', methods=['GET', 'POST'])
def recibe():
    if request.method == 'POST':
        before = request.files['before']
        after = request.files['after']

        name = request.form['nombre']
        lastName = request.form['apellido']

        print(f'El nombre es {name} y el apellido {lastName}')

        nameBefore = 'before'
        nameAfter = 'after'
        before.save(os.path.join(app.config['UPLOAD_FOLDER'], nameBefore))
        after.save(os.path.join(app.config['UPLOAD_FOLDER'], nameAfter))
        
        
        return elimina()
    
def elimina():
    before = 'archivos/before'
    after = 'archivos/after'

    try:
        os.remove(before)
        os.remove(after)
        return 'Excelente se eliminaron los archivos'
    except:
        return 'No se pudo eliminar el archivo'
