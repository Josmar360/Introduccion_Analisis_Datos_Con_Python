import pandas as pd

# Abrir archivo scv de Paises
print("====== Imprimir el archivo csv ======")
data = pd.read_csv("3) Pandas/11) Users.csv", index_col='id')
print(data)

# Limpieza de datos
print("\n====== Imprimir lista limpia de usuarios ======")
data = data.dropna()
print(data)

# Obtener el nombre de todos los usuarios del pais Canada
print("\n====== Obtener el nombre de todos los usuarios del pais Canada ======")
print(data[data['pais'] == 'Canada'][['nombre']])

# Obtener el nombre y correo electronico de todos los usuarios con edad mayor a 50
print("\n====== Obtener el nombre y correo electronico de todos los usuarios con edad mayor a 50 ======")
print(data[data['edad'] > 50][['nombre', 'email']])

# Obtener el promedio de todos los usuarios de sexo femenino con una edad mayor a 30
print("\n====== Obtener el promedio de todos los usuarios de sexo femenino con una edad mayor a 30 ======")
print(data[(data['genero'] == 'female') & (data['edad'] > 30)][['edad']].mean())