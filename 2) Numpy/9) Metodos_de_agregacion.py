import numpy as np

A = np.array([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [100, 200, 300, 400, 500]])

# Permite conocer la desviacion estandar del matriz
print("Desviación estandar es: ", A.std())

# Permite conocer la suma total del matriz
print("Suma total de matriz: ", A.sum())

# Permite conocer el valor minimo del matriz
print("Valor minimo de la matriz: ", A.min())

# Permite concoer el valor maximo del matriz
print("Valor maximo de la matriz: ", A.max())

# Permite conocer el promedio de la matriz
print("Promedio de la matriz: ", A.mean())

# Obtener valores de la fila numero 2
print("Fila de matriz numero 1: ", A[1])
print("La suma de la fila 1 es: ", A[1].sum())

# Obtener valores de la fila numero 3
print("Valor minimo de la fila 2: ", A[1].min())
print("Valor maximo de la fila 2: ", A[1].max())

# Usar solo la tercera columna
print(A[:, 2])
print("El promedio de la tercera columna: ", A[:, 2].mean())

# Usar solo la tercera columna
print("El promedio de la cuarta columna: ", A[:, 2].mean())