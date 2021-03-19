# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 22:47:55 2021

@author: Hens
"""

import numpy as np
import matplotlib.pyplot as plt
import math

f = lambda x, y: np.sin(x) * np.power(y ** 2, 1./3.)

X = np.linspace(-3, 3, 256)
Y = np.linspace(-3, 3, 256)

X, Y = np.meshgrid(X, Y)
Z = f(X, Y)
#Z = X * 0

"""
i = 0
for x, y in zip(X, Y):
    j = 0
    for xx , yy in zip(x, y):
        Z[i][j] = f(xx, yy)
        #print(xx, yy, Z[i][j])
        j = j + 1
    i = i + 1
"""
plt.xlabel("x")
plt.ylabel("y")
C = plt.contour(X, Y, Z)