from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from utils import util1
from utils import util2

app = Flask(__name__)

app.secret_key = 'fran1234'

# Rutas de la aplicación
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrarse')
def registrarse():
    return render_template('registrarse.html')

@app.route('/cambiar_contraseña')
def cambiar_contraseña():
    return render_template('cambiar_contraseña.html')

@app.route('/verificar_correo')
def verificar_correo():
    return render_template('verificar_correo.html')

@app.route('/home')
def home():
    return render_template('home.html')

#Traemos los datos dle usuario, los comprobamos y los enviamos a la base de datos
@app.route('/registrarse', methods=['POST'])
def registrarse_post():
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    pregunta_seguridad = request.form['pregunta_seguridad']
    
    if password != password2:
        return render_template('registrarse.html', error='Las contraseñas no coinciden')

    if not util1.requisitos_contraseña(password):
        return render_template('registrarse.html', error="La contraseña debe tener 8 o más caracteres, una mayúscula y una minúscula")
    
    if util1.verificar_usuario(username):
        return render_template('registrarse.html', error='El usuario ya existe')
    
    codigo = util2.generar_codigo()
    session['codigo'] = codigo
    util2.verificar_correo(username, codigo)
    util1.enviar_datos(username, password, pregunta_seguridad, codigo)
    return redirect(url_for('verificar_correo'))

# Verificamos si el código de verificación es correcto
@app.route("/verificar_correo", methods=['POST'])
def verificar_correo_post():
    codigo_original = session.get('codigo')
    codigo_ingresado = request.form['codigo']

    if codigo_original == codigo_ingresado:
        return redirect(url_for('index'))
    else:
        return render_template('verificar_correo.html', error='El código es incorrecto')
    
#Vereficamos el inicio de sesion
@app.route("/iniciar_sesion", methods=['POST'])
def iniciar_sesion_post():
    username = request.form['username']
    password = request.form['password']

    if not util1.verificar_usuario(username):
        return render_template('index.html', error='El usuario no existe')
    elif not util1.verificar_contraseña(username, password):
        return render_template('index.html', error='Contraseña incorrecta')
    else: 
        return redirect(url_for('home'))

#Verificamos si la pregunta de seguridad esta bien 
@app.route("/cambiar_contraseña", methods=['POST'])
def pregunta_seguridad_post():
    username = request.form['username']
    pregunta = request.form['pregunta_seguridad']
    nueva_password = request.form['npassword']

    if util1.verificar_respuesta(username, pregunta):
        util1.reemplazar_contraseña(username, nueva_password)
        return redirect(url_for('index'))
    else:
        return render_template('cambiar_contraseña.html', error='La respuesta de seguridad es incorrecta')


# Conectarse a la base de datos (si no existe, se crea)
conexion = sqlite3.connect('proyecto_testing\\data\\usuarios.db')
cursor = conexion.cursor()

# Define la sentencia SQL para crear la tabla
tabla_sql = '''
CREATE TABLE IF NOT EXISTS mi_tabla (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    pregunta_seguridad TEXT
    codigo_verificacion NUMERIC
)
'''

# Ejecutar la sentencia SQL para crear la tabla
cursor.execute(tabla_sql)

# Guardar los cambios y cerrar la conexión a la base de datos
conexion.commit()
conexion.close()

print("La tabla se ha creado exitosamente.")

"""
Solo por hacer esto nos merecemos un 10!!!!!
"""

if __name__ == '__main__':
    app.run(debug=True)
