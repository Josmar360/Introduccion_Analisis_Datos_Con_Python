import numpy as np

# Crear un arreglo
a = np.random.randint(0, 10, 10)
print("====== Imprimir arreglo a ======")
print(a)

# Almacenar en un archivo de texto
np.savetxt("Arreglo.txt", a, fmt="%i")

# Leer el archivo de texto
print("====== Imprimir archivo de texto ======")
b = np.loadtxt("Arreglo.txt", dtype=int)
print(b)

# Crear una matriz
c = np.array([[9, 1, 9, 4, 5], [9, 9, 8, 8, 7]])
print("====== Imprimir la matriz ======")
print(c)

# Crear un archivo csv
np.savetxt("Matriz.csv", c, delimiter=",", fmt="%i")

# Abrir el archivo Matriz.scv
print("====== Imprimir el archivo csv ======")
d = np.loadtxt("Matriz.csv", delimiter=",", dtype=int)
print(d)
