import numpy as np

# Generar un arreglo aleatorio entero
a = np.random.randint(0, 10, 20)
print("====== Imprimir arreglo a ======")
print(a)

# Aplicar metodo sort ascendente
print("====== Imprimir el arreglo orden ascendente ======")
b = np.sort(a)
print(b)

# Ordenar de manera descentende
print("====== Imprimir el arreglo descendente ======")
c = np.sort(a)[::-1]
print(c)

# Metodo sort a.sort() ordena el arreglo

# Funcion sort np.sort(a) genera un nuevo arreglo con los elementos ordenados