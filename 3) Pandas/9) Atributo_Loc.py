import pandas as pd

# Crear un diccionario de datos
Usuarios = {'Username': ['User1', 'User2', 'User3', 'User4', 'User5',],
            'Email': ['User1@example.com', 'User2@example.com', 'User3@example.com', 'User4@example.com', 'User5@example.com'],
            'Age': [10, 20, 30, 40, 50],
            'Status': [True, True, False, False, True]}

# Crear un DataFrame String
print("\n====== Imprimir DataFrame ======")
data = pd.DataFrame(Usuarios, index=['a', 'b', 'c', 'd', 'e'])
print(data)

# Atriuto loc
print("\n====== Imprimir valores con indices de tipo string ======")
print(data.loc['a'])
print(data.loc['a':'c'])

print("\n====== Imprimir columnas especificas ======")
print(data.loc['a':'c', ['Username', 'Email']])
print(data.loc['a':'c'][['Username', 'Email']])