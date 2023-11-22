import pandas as pd

# Abrir archivo csv de Usuarios
print("====== Imprimir el archivo csv ======")
data = pd.read_csv("3) Pandas/15) Users.csv", index_col='id')
print(data)

# Limpieza de datos
print("\n====== Limpieza de datos de la lista Usuarios ======")
data = data.dropna()
print(data)

# Metodo starswitch sirve para buscar inicial en texto = LIKE %a
print("\n====== Obtener todos los usuarios que su correo inicie con la letra a ======")
print(data[data['email'].str.startswith('a')])

# Metodo endswitch sirve para buscar final en texto = LIKE a%
print("\n====== Obtener todos los usuarios que su correo termine con .com ======")
print(data[data['email'].str.endswith('.com')])

# Metodo contains sirve para buscar en medio = LIKE %a%
print("\n====== Obtener todos los usuarios que contengan Gabriel en su nombre ======")
print(data[data['nombre'].str.contains('Gabriel')])

# Atributo str permite buscar si inicia, termina o esta por medio de los metodos de arriba