import sqlite3

def crear_tabla():
    conexion = sqlite3.connect('proyecto_testing\\data\\table_home.db')
    cursor = conexion.cursor()
    tabla_sql = '''
    CREATE TABLE IF NOT EXISTS stock (
        username_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        codigo NUMERIC,
        nombre TEXT,
        descripcion TEXT
    )
    '''
    cursor.execute(tabla_sql)
    conexion.commit()
    conexion.close()

def agregar_producto(username, codigo, nombre, descripcion):
    conexion = sqlite3.connect('proyecto_testing\\data\\table_home.db')
    cursor = conexion.cursor()
    sql = '''
    INSERT INTO stock (username, codigo, nombre, descripcion)
    VALUES (?, ?, ?, ?)
    '''
    cursor.execute(sql, (username, codigo, nombre, descripcion))
    conexion.commit()
    conexion.close()

def mostrar_productos(username):
    conexion = sqlite3.connect('proyecto_testing\\data\\table_home.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM stock WHERE username=?", (username,))
    productos = cursor.fetchall()
    
    conexion.close()
    
    return productos

