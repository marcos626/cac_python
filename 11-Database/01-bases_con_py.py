# para instalar el conector: pip3 install mysql-connector-python

import mysql.connector
import getpass #para ocultar la contraseña
#conecto con la base de datos
db=mysql.connector.connect(host='db4free.net', user='pruebascodo', passwd='746650ac', database='pruebascodo')
#creo el cursor
cursor=db.cursor()
#pido al usuario nombre de usuario y contraseña
nusuario = input('Ingrese su nombre de usuario: ')
contrasenia=getpass.getpass("ingrese su contraseña: ")

#creo una consulta
#  "select * from usuarios where username='" + varuser + "' and pass='" + varpass + "'"
sql="select * from usuarios where username ='" + nusuario + "' and pass='" + contrasenia + "'"
cursor.execute(sql)
#obtengo los resultados
resultado=cursor.fetchall()
#si hay resultados 
if resultado:
    print('Bienvenido')
else:
    print('Usuario o contraseña incorrectos')
