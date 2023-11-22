import pandas as pd

# Abrir el archivo csv de Usuarios
print("====== Imprimir el archivo csv ======")
data = pd.read_csv("3) Pandas/14) Users.csv", index_col='id')
print(data)

# Limpieza de datos en lista de Usuarios
print("\n====== Limpieza de datos de la lista Usuarios ======")
data = data.dropna()
print(data)

# Obtener el nombre de todos los usuarios mayores a 30 años de los paises Canada, Alemania y Francia
print("\n====== Obtener el nombre de todos los usuarios mayores a 30 años de los paises Canada, Alemania y Francia ======")
print(data[(data['edad'] > 30) & ((data['pais'] == 'Canada') | (
    data['pais'] == 'Germany') | (data['pais'] == 'France'))].sort_values('pais'))

# Otra forma de realizar el ejercicio con la funcion isin()
print("\n====== Obtener el nombre de todos los usuarios mayores a 30 años de los paises Canada, Alemania y Francia ======")
Paises = ['Canada', 'Germany', 'France']
print(data[(data['edad'] > 30) & (data['pais'].isin(Paises))].sort_values('pais'))