import numpy as np

# Crear un arreglo
a = np.random.randint(0, 10, 10)
print("====== Imprimir arreglo a ======")
print("Tamaño del arreglo:", a.size)
print(a)

# Añadir nuevos elementos al arreglo con funciones insert o append

# Funcion Insert
print("====== Se crea un nuevo arreglo y añade 200 ======")
b = np.insert(a, 0, 200)
print(b)

# Funcion append
print("====== Se crea un nuevo arreglo y añade al final 200 ======")
c = np.append(a, 200)
print(c)

# Uso de la funcion delete
print("====== Se crea un nuevo arreglo y elimina el 200 final ======")
c = np.delete(c, -1)
print(c)

# Redimensionar el tamaño del arreglo
print("====== Redimensionar el tamaño del arreglo ======")
c = np.resize(c, 5)
print(c)

# Generar nuevos arreglos apartir de otros
print("====== Generar nuevos arreglos con otros arreglos ======")
d = np.random.randint(0, 10, 10)
e = np.concatenate( [a, d])
print("Arreglo a:", a)
print("Arreglo d:", d)
print(e)