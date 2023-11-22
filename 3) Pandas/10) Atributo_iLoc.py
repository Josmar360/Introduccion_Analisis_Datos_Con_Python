import pandas as pd

# Abrir archivo csv
print("====== Imprimir el archivo csv ======")
data = pd.read_csv("3) Pandas/10) Users.csv", index_col='id')
print(data)

# Atributo iloc permite usar indices de tipo int
print("\n====== Imprimir fila especifica ======")
print(data.iloc[0])

print("\n====== Imprimir valores de ultima fila ======")
print(data.iloc[199])

# Generar SubDataFrames 
print("\n====== Imprimir subDataFrames ======")
print(data.iloc[0:5, [0, 2, 4]])

print("\n====== Imprimir subDataFrames de otra forma ======")
print(data.iloc[0:5][['nombre', 'genero', 'email']])