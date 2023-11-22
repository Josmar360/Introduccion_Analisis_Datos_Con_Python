import pandas as pd

# Abrir archivo csv de Usuarios
print("====== Imprimir el archivo csv ======")
data = pd.read_csv("3) Pandas/16) Users.csv", index_col='id')
print(data)

# Limpieza de datos
print("\n====== Limpieza de datos de la lista Usuarios ======")
data = data.dropna()
print(data)

# Mostrar en consola la cantidad de hombres y mujeres del dataset
print("\n====== Mostrar en consola la cantidad de hombres y mujeres del dataset ======")
print(data.groupby('genero')['genero'].count())

# Mostrar el pais con mas mujeres
print("\n====== Mostrar el pais con mas mujeres ======")
print(data[data['genero'] == 'female'].groupby(
    'pais')['pais'].count().sort_values(ascending=False).head(1))
