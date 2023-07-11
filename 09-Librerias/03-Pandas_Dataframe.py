#ejemplo de data frame del power point de codo a codo

import pandas as pd 

#Crear un Dataframe desde un diccionario
data = {'Nombre': ['Alice','Bob','Charlie','David'],
        'Edad': [25, 30, 35, 40],
        'Ciudad': ['Londres','Nueva York', 'Paris', 'Tokio'],}
df = pd.DataFrame(data)
print(df)
