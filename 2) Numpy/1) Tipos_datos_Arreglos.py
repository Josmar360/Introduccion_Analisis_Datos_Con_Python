# coding: utf-8
import numpy as np
a = np.array( [1, 2, 3, 4, 5] )

a.dtype

a = np.array( [1, 2, 3, 4, 5], dtype=float )
"""Resultado: 1, 2, 3, 4, 5 """

a = np.array( [1, 2, 3, 4, 5], dtype=str )
"""Resultado: '1', '2', '3', '4', '5' """

a = np.array( [1, 2, 3, 4, 5], dtype=bool )
"""Resultado: True, True, True, True, True"""

a = np.array( [0, 2, 3, 4, 5], dtype=bool )
"""Resultado: False, True, True, True"""

a = np.array( [0, 1, 2, 3, 4, 5], dtype=np.complex )
"""Resultado: 0.+0.j, 1.+0.j, 2.+0.j, 3.+0.j, 4.+0.j, 5.+0.j"""
