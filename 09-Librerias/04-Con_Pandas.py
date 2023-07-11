#pip3 install pandas

import pandas as pd
from openpyxl import workbook #A Python library to read/write Excel 2010 xlsx/xlsm files

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('/home/marcos/cac_python/09-Librerias/datos1.csv')

# Mostrar las primeras filas del DataFrame
print("---primeras filas del DataFrame----")
print(df.head(3)) #muestra el encabezado y las primeras 3 líneas de datos
print("-----------------")

# Calcular el total de ventas por producto
print("---Calcular el total de ventas por producto---")
total_ventas = df.groupby('Producto')['Cantidad'].sum() #groupby = agrupar por
print(total_ventas)
print("-----------------")

# Calcular el promedio de precio por mes
print("-----promedio de precio------")
promedio_precio = df.groupby('Mes')['Precio'].mean()
print(promedio_precio)
print("-----------------")

# Filtrar las ventas de un producto específico
print("---Filtrar las ventas de Producto A-------")
producto_filtrado = df[df['Producto'] == 'Yerba']
print(producto_filtrado)
print("-----------------")

# Guardar el resultado en un nuevo archivo CSV
total_ventas.to_csv('total_ventas.csv', header=True)

# Guardar el DataFrame en un archivo Excel
df.to_excel('datos.xlsx', index=False)
