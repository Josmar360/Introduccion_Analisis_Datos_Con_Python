# coding: utf-8
import numpy as np

a = np.random.randint(0, 10, 20)

def operacion(valor):
    return (valor ** 2) + 2

operacion(3)
for valor in a:
    print(operacion(valor))
    
vector = np.vectorize(operacion)
vector(a)

print(vector(a))