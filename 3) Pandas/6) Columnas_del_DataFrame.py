import pandas as pd
import numpy as np

# Crear un diccionario
Usuarios = {'Username': ['user1', 'user2', 'user3'], 'Email': [
    'user1@example.com', 'user2@example.com', 'user3@example.com'], 
    'Age':[27, 10, 30], 'Status':[True, True, False]}

# Crear primer DataFrame
data = pd.DataFrame(Usuarios, index=['a', 'b', 'c'])
print("====== Imprimir el DataFrame ======")
print(data)

# Las Columnas = Series
print("====== Crear una serie de calificaciones ======")
Calificaciones = pd.Series(np.random.randint(5, 10, 3), index=['a', 'b', 'c'])
print(Calificaciones)

# Agregar la serie calificaciones al DataFrame
data['Calificaciones'] = Calificaciones
print("====== Imprimir el DataFrame con calificaciones ======")
print(data)

# Renombrar las columnas
data = data.rename(columns={'Calificaciones':'Score'})
print("====== Renombrar la columna de calificaciones ======")
print(data)

# Renombrar la columna por nombre de columna o por atributo del objeto
# Eliminar una columan del DataFrame
data = data.drop('Score', axis=1)
print("====== Eliminar la columna Score ======")
print(data)