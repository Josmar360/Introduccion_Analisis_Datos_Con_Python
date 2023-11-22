import pandas as pd

# Crear una primer serie
a = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name="Numeros", dtype=float)
print("====== Impresión de la primer serie ======")
print(a)

# Crear una serie con diccionarios
Colores = {"Rojo":100, "Verde":200, "Azul":300, "Negro":400}
b = pd.Series(Colores)
print("====== Impresión de la segunda serie ======")
print(b)

print("====== Visualizar un valor especifico ======")
print("El valor de rojo es: ", b['Rojo'])
print("El valor de verde es: ", b['Verde'])
