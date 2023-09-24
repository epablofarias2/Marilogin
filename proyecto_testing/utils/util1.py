import sqlite3

def requisitos_contraseña(contraseña):
    """
    Verifica que la contraseña cumpla con los siguientes requisitos:
    """
    longitud_valida = len(contraseña) >= 8
    contiene_mayuscula = any(c.isupper() for c in contraseña)
    contiene_minuscula = any(c.islower() for c in contraseña)
    contiene_numero = any(caracter.isdigit() for caracter in contraseña)

    if not longitud_valida:
        return False
    elif not contiene_mayuscula:
        return False
    elif not contiene_minuscula:
        return False
    elif not contiene_numero:
        return False
    else:
        return True

def enviar_datos(username, password, pregunta_seguridad, codigo_verificacion):
    """ 
    Envía los datos del usuario a la base de datos
    """ 
    conexion = sqlite3.connect('proyecto_testing/data/usuarios.db')
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO mi_tabla (username, password, pregunta_seguridad, codigo_verificacion) VALUES (?, ?, ?, ?)", (username, password, pregunta_seguridad, codigo_verificacion))
    conexion.commit()
    conexion.close()

def verificar_usuario(username):
    """
    Verifica que el usuario exista en la base de datos
    """
    conexion = sqlite3.connect('proyecto_testing/data/usuarios.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM mi_tabla WHERE username=?", (username,))
    usuario = cursor.fetchone()
    conexion.close()
    if usuario is None:
        return False
    else:
        return True

def verificar_contraseña(username, password):   
    """
    Verifica que la contraseña sea correcta
    """
    conexion = sqlite3.connect('proyecto_testing/data/usuarios.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM mi_tabla WHERE username=? AND password=?", (username, password))
    usuario = cursor.fetchone()
    conexion.close()
    if usuario is None:
        return False
    else:
        return True

def verificar_respuesta (username, pregunta):
    """
    Verifica que la respues de seguridad sea la correcta
    """
    conexion = sqlite3.connect('proyecto_testing/data/usuarios.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM mi_tabla WHERE username=? AND pregunta_seguridad=?", (username, pregunta))
    usuario = cursor.fetchone()
    conexion.close()
    if usuario is None:
        return False
    else:
        return True

def reemplazar_contraseña(usuario_id, new_password):
    """
    Sirve para reemplazar la contraseña dentro de la base de datos  
    """
    conexion = sqlite3.connect('proyecto_testing/data/usuarios.db')
    cursor = conexion.cursor()
    
    consulta_actualizar_contraseña = "UPDATE mi_tabla SET password = ? WHERE id = ?"

    cursor.execute(consulta_actualizar_contraseña, (new_password, usuario_id))
    conexion.commit()
    conexion.close()