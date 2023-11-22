import pandas as pd

# Series son objetos diseñados para representar una estructura de una dimension
print("====== Impresión de la serie ======")
a = pd.Series([1, 2, 3, 4, 5])
print(a)
print("Atributo type: ", type(a))
print("Atributo size: ", a.size)
print("Atributo dtype: ", a.dtype)
print("Atributo shape: ", a.shape)
print("Atributo index: ", a.index)

print("====== Obtener el valor de un indice ======")
print(a[4])

print("====== Actualizar el valor de una serie ======")
a[4] = 500
print(a)

print("====== Crear una serie nueva con indices definidos ======")
b = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(b)

print("====== Actualizar el valor de una serie ======")
print(b['a'])
b['a'] = 500
print(b)

print("====== Nombrar la serie con parametro name ======")
b = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name="Numeros")
print(b)

print("====== Especificar los tipos de datos para almacenar ======")
b = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name="Numeros", dtype=float)
print(b)