import pandas as pd

# Abrir el archivo user.csv
print("====== Imprimir el archivo csv ======")
data = pd.read_csv("3) Pandas/7) Users.csv", index_col='id')
print(data)

# Usar metodos head()
print("====== Imprimir las primeras 5 filas ======")
print(data.head(10))

# Usar metodo tail()
print("====== Imprimir las ultimas 5 filas ======")
print(data.tail(10))