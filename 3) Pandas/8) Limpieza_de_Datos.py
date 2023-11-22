import pandas as pd

# Abrir el archivo csv
print("====== Imprimir el archivo csv ======")
data = pd.read_csv("3) Pandas/8) Users.csv", index_col='id')
print(data)

# Eliminar las filas que tengan Nan por metodo dropna()
print("====== Eliminar filas con datos Nan ======")
a = data.dropna()
print(a)

# Usar metodo fillan() para colocar valores en Nan
print("====== Agregar valores filas NaN con dato Nuevo valor ======")
b = data.fillna('Nuevo valor')
print(b)

# USar un diccionario de datos usando metodo fillna()
print("====== Agregar valores filas NaN con diccionario de datos ======")
c = data.fillna({'nombre':'Sin nombre', 'email':'example@example.com'})
print(c)