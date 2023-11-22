import pandas as pd

# Abrir archivo csv de Usuarios
print("====== Imprimir el archivo csv ======")
data = pd.read_csv("3) Pandas/13) Users.csv", index_col='id')
print(data)

# Limpieza de datos
print("\n====== Limpieza de lista de usuarios ======")
data = data.dropna()
print(data)

# Obtener todos los usuarios entre las edades 40 y 50
print("\n====== Obtener todos los usuarios entre las edades 40 y 50 ======")
print(data[(data['edad'] >= 40) & (data['edad'] <= 50 )].sort_values('edad'))

# Obtener todos los usuarios entre las edades 40 y 50 con funcion between
print("\n====== Obtener todos los usuarios entre las edades 40 y 50 con Between ======")
print(data[data['edad'].between(40, 50)].sort_values('edad'))