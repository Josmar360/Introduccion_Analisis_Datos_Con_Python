# coding: utf-8
import numpy as np

a = np.arange(0, 10)
# a es el Arreglo original

b = a.copy()

a is b

a[0] = 100
b[0] = 200

a.View()
a.view()

c = a.view()
# a -> Origional, b -> Copia, c -< Vista
id(c)
id(a)
c[-2] = 180

c
a

c.base
id(c.base)
id(c)
