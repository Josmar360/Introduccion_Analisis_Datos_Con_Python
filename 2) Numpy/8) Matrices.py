import numpy as np

A = np.array([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [100, 200, 300, 400, 500]])
print(A)
print(A.ndim)
print(A.shape)

# Obtener elementos de la matriz
# Axi0 = Filas
# Axi1 = Columnas 
# A[Axi0][Axi1]
print(A[0][0])
print(A[1][2])
print(A[2][4])

# Obtener elementos de la matriz de otra forma con solo un corchete
print(A[0, 0])
print(A[1, 2])
print(A[2, 4])

# Obtener los primeros 3 indices de la fila
print(A[1, :3])
print(A[2, 2:])

# Obtener el primero y ultimo elemento de la primera fila
print(A[0, [0,4]])

# Obtener valores de columnas
print(A[:, 3])
print(A[[0,2], 3])