

import sqlite3
conexion = sqlite3.connect('mi_data_base1.db')
cur = conexion.cursor()
cur.execute("CREATE TABLE biblioteca(Titulo text, Autor text);")
conexion.commit()
conexion.close()

