# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:14:24 2021

@author: WarleY
"""

import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([5, 6, 7])

# padrão axis=0
matriz = np.concatenate((array1, array2))

print(matriz)