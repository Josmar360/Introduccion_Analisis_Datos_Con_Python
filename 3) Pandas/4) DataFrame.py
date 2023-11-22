import pandas as pd

# Se encuentra conformado por filas y columnas

# Crear un diccionario
Usuarios = {'Username': ['user1', 'user2', 'user3'], 'Email': [
    'user1@example.com', 'user2@example.com', 'user3@example.com'], 
    'Age':[27, 10, 30], 'Status':[True, True, False]}

# Crear primer DataFrame
a = pd.DataFrame(Usuarios, index=['a', 'b', 'c'])
print("====== Imprimir el DataFrame ======")
print(a)
