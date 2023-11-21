# coding: utf-8
import numpy as np

a = np.random.randint(0, 10, 20)

# a[start:end:saltos]
a[0,5]
a[0:5]
a[:5]
a[5:]
a[5::2]

# a[0, 1, 3]
a[0,1,3]
a[[0,1,3]]
b = np.array( [1, 2, 3, 4, 5] )

b[[True, False, False, False, True]]
b[[True, False, True, False, True]]
