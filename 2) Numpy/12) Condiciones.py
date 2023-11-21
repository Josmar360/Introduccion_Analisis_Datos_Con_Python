import numpy as np

# Crear el primer arreglo
a = np.random.randint(0, 100, 50)
print("====== Imprimir el arreglo a ======")
print(a)

# Si todos los elementos son mayores a 50
print("Todos los valores son mayores a 0?", np.all(a >= 0))
print("Todos los valores son menores a 100?", np.all(a <= 100))

# Aplicar multiples condiciones
print("Todos los valores son mayores a 0 y menores a 100:", np.all((a >= 0) & (a <= 100)))

# Funcion any permite saber si algun elemento cumple la condicion
print("Algun elemento es mayor a 10: ", np.any(a > 10))
print("Algun elemento es mayor a 200: ", np.any(a > 200))