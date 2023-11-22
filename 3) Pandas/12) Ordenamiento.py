import pandas as pd

# Abrir archivo csv de Usuarios
print("====== Imprimir el archivo csv ======")
data = pd.read_csv("3) Pandas/12) Users.csv")
print(data)

# Limpieza de datos
print("\n====== Limpieza de datos del archivo usuarios ======")
data = data.dropna()
print(data)

# Obtener el ususario mas joven del pais de Canada
print("\n====== Obtener el ususario mas joven del pais de Canada ======")
print(data[data['pais'] == 'Canada'].sort_values('edad').head(1))

# Obtener a los 5 usuarios mas viejos de Alemania
print("\n====== Obtener a los 5 usuarios mas viejos de Alemania ======")
print(data[data['pais'] == 'Germany'].sort_values('edad', ascending=False).head(5))