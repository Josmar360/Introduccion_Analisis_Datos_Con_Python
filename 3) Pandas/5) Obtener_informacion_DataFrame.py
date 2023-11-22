import pandas as pd

# Se encuentra conformado por filas y columnas

# Crear un diccionario
Usuarios = {'Username': ['user1', 'user2', 'user3'], 'Email': [
    'user1@example.com', 'user2@example.com', 'user3@example.com'], 
    'Age':[27, 10, 30], 'Status':[True, True, False]}

# Crear primer DataFrame
data = pd.DataFrame(Usuarios, index=['a', 'b', 'c'])
print("====== Imprimir el DataFrame ======")
print(data)

# Ver todos los valores de una columa
print("====== Imprimir una sola columna del DataFrame ======")
print(data['Username'])

# Ver todos los valores de una columa y valor especifico
print("====== Imprimir un valor de una columa especifica del DataFrame ======")
print(data['Age']['b'])

# Otra forma de obtener los datos
print("====== Imprimir una columa de otra forma ======")
print(data.Username)

# Obtener solo los nombres de las columnas
print("====== Imprimir el nombre de las columas ======")
print(data.columns)

# Obtener solo los valores que contienen las columnas
print("====== Imprimir solo los valores ======")
print(data.values)