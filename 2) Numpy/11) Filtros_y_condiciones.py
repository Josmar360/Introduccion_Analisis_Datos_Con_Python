import numpy as np

# Crear un segundo arreglo y obtener el primero y ultimo elemento
b = np.array([1, 2, 3, 4, 5])
print("====== Imprimir arreglo b ======")
print(b)
print("====== Obtener primero y ultimo valor ======")
print(b[[True, False, False, False, True]])

# Crear un arreglo random entero
a = np.random.randint(0, 100, 50)
print("====== Imprimir el arreglo a ======")
print(a)

# Obtener valores mayores a 50 por booleano
print("====== Obtener valores mayores a 50======")
print(a > 50)

# Obtener valores mayores a 50
print("====== Obtener valores mayores a 50 ======")
print(a[a > 50])
print("====== Obtener valores menores o igual a 50 ======")
print(a[a <= 50])

# Implementar operadores logicos
print("====== Obtener valores mayores a 50 y menores a 90 ======")
print(a[(a <50) & (a < 90)])

print("====== Obtener valores iguales a 10 o 20 o 50 ======")
print(a[(a==10) | (a==20) | (a==50)])

# Operador and = &
# Operador or = |
# a > num,  da booleanos