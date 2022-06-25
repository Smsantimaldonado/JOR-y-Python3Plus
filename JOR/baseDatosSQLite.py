import sqlite3


def conectar():
    conexion = sqlite3.connect('miDB.db')
    cursor = conexion.cursor()
    return conexion, cursor


def crearTabla():
    conexion, cursor = conectar()
    directiva = """ 
        CREATE TABLE IF NOT EXISTS agenda(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(20) NOT NULL,
            telefono VARCHAR(14) NOT NULL
        )
        """
    if (cursor.execute(directiva)):  # Ejecutá lo que se indica en 'directiva'
        print('\n', 'Tabla creada')
    else:
        print('\n', 'Imposible crear tabla')
    conexion.close()


def insertar(data):
    conexion, cursor = conectar()
    accion = """ 
        INSERT INTO agenda(nombre, telefono) VALUES (?, ?)
        """
    # Ejecutá lo que se indica en 'accion' usando los datos en la variable 'data'
    if (cursor.execute(accion, data)):
        print('\n', 'Datos guardados')
    else:
        print('\n', 'Error en la carga de datos')
    conexion.commit()  # Actualizar los cambios en la DB
    conexion.close()


def consultar():
    conexion, cursor = conectar()
    indicacion = 'SELECT id, nombre, telefono FROM agenda'
    cursor.execute(indicacion)
    for fila in cursor:
        print('\n', 'ID: ', fila[0])
        print('Nombre:   ', fila[1])
        print('Telefono: ', fila[2])
    conexion.close()


def modificar(id, telefono):
    conexion, cursor = conectar()
    cursor.execute('UPDATE agenda SET telefono=' + telefono + ' where ID=' + id)
    cursor.close()
    conexion.commit()
    conexion.close()


def borrar(id):
    conexion, cursor = conectar()
    cursor.execute('DELETE from agenda where ID=' + id)
    cursor.close()
    conexion.commit()
    conexion.close()


crearTabla()
insertar(data=('Gringo', '3517541906'))
insertar(data=('Elon', '3513896521'))
insertar(data=('Cocos', '3514321987'))
insertar(data=('Cocos', '3514321987'))
print('\n--CONSULTA 1--')
consultar()
modificar(id='2', telefono='3515129010')
print('\n--CONSULTA 2--')
consultar()
borrar('2')
print('\n--CONSULTA 3--')
consultar()
