# coding: utf-8
import numpy as np

# array
np.array( [True, True, False] )

# arange crear un rango
np.arange(0, 10)
np.arange(0, 100)
np.arange(0, 20, 2)

# zeros crear un arreglo de zeros
np.zeros(10)
np.zeros(10, dtype=int)
np.zeros(10, dtype=int).dtype

# ones crear un arreglo de unos
np.ones(10, dtype=int)

# empty crear arreglo de datos basura
np.empty(10)
np.empty(10, dtype=int)

# randint crear un arreglo de rangos
np.random.randint(0, 100, 50)
np.random.randint(0, 10, 50)