import numpy as np

# Crear un arreglo de calificaciones
Calificaciones = np.random.randint(1, 11, 10)
print("====== Lista de calificaciones ======")
print(Calificaciones)

# Todas las calificaciones mayores a 7 son aprobatorias
# Tendra dos mensajes:...
# Felicidades, aprobaste la materia
# Lo sentimos, no aprobaste la materia
print("====== Lista de mensajes ======")
print(np.where(Calificaciones >= 7, "Felicidades, aprobaste la materia", "Lo sentimos, no aprobaste la materia"))

# Aplicar diferentes tipos de condiciones y valores
# Se van almacenar 4 tipos de mensajes
# Felicidades aprobaste la materia con 10 = 10
# Felicidades aprobaste la materia = 8 o 9
# Aprobaste la materia = 7
# Lo sentimos no aprobaste la materia < 7
print("====== Hacer uso de la función select ======")
Condicion = [(Calificaciones == 10), (Calificaciones == 8) | (Calificaciones == 9), (Calificaciones == 7), (Calificaciones < 7)]
Opciones = ["Felicidades aprobaste la materia con 10", "Felicidades aprobaste la materia con 8 o 9", "Aprobaste la materia", "Lo sentimos, no aprobaste la materia"]
print(np.select(Condicion, Opciones))

# Where se usa con 2 valores y cuando la condicion se cumple y no se cumple
# Select se usa cuando son mas de 2 valores, y se necesitan mas de una condicion