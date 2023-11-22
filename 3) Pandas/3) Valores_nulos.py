import pandas as pd
import numpy as np

# Numpy o Pandas = NaN
print("====== Imprimir valor null con Numpy ======")
print(np.nan)

# Crear una serie de valores
a = pd.Series([1, 2, np.nan, np.nan, 5,6, 7, np.nan, 8, 9])
print("====== Imprimir la serie a ======")
print(a)

# Metodo para filtrar valores con isnull
print("====== Imprimir serie con filtro isnull ======")
print(a.isnull())

# Metodo para filtrar valores con notnull
print("====== Imprimir serie con filtro notnull ======")
print(a.notnull())

# Obtener indices con valores null
print("====== Imprimir solo los indices con valores null ======")
print(a[a.isnull()])

# Obtener indices con valores no null
print("====== Imprimir solo los indices con valores no null ======")
print(a[a.notnull()])