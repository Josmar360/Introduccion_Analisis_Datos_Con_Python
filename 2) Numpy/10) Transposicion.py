import numpy as np

A = np.array([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [100, 200, 300, 400, 500]])
print(A)

# Implementar la transposicion
print(A.T)

# Obtener la suma total de la ultima columna
print(A[:, 4].sum())
print(A.T[4].sum())
print("Suma de ultima columna: ", A[:, 4].sum())
print("Suma de ultima fila: ", A.T[4].sum())