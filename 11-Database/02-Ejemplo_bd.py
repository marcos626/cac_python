#conecto con la base de datos MySQL
import mysql.connector
cnx = mysql.connector.connect(host='127.0.0.1', user='root', password='')
#cnx = mysql.connector.connect(host='db4free.net', user='pruebascodo', password='746650ac')
cursor = cnx.cursor()
#creo la base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS ejemplo23412")
#creo la tabla
cursor.execute("CREATE TABLE IF NOT EXISTS ejemplo23412.personas (id INT NOT NULL AUTO_INCREMENT, nombre VARCHAR(50), apellido VARCHAR(50), PRIMARY KEY (id))")
#inserto datos
cursor.execute("INSERT INTO ejemplo23412.personas (nombre, apellido) VALUES ('Juan', 'Perez')")
cursor.execute("INSERT INTO ejemplo23412.personas (nombre, apellido) VALUES ('Maria', 'Gomez')")
cursor.execute("INSERT INTO ejemplo23412.personas (nombre, apellido) VALUES ('Pedro', 'Gomez')")
#consulto datos
print("estos son los datos luego de insertarlos")
cursor.execute("SELECT * FROM ejemplo23412.personas")
for (id, nombre, apellido) in cursor:
    print("{}, {} {}".format(id, nombre, apellido))
#borro datos
cursor.execute("DELETE FROM ejemplo23412.personas WHERE nombre = 'Pedro'")
#actualizo datos
cursor.execute("UPDATE ejemplo23412.personas SET apellido = 'Perez' WHERE nombre = 'Juan'")
#consulto datos
print("estos son los datos luego de borrar y actualizar")
cursor.execute("SELECT * FROM ejemplo23412.personas")
for (id, nombre, apellido) in cursor:
    print("{}, {} {}".format(id, nombre, apellido))
#borro la tabla
cursor.execute("DROP TABLE ejemplo23412.personas")
#borro la base de datos
cursor.execute("DROP DATABASE ejemplo23412")
#cierra la conexion
cursor.close()
cnx.close()