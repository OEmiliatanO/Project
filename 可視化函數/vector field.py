# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:07:32 2021

@author: Hens
"""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x, y: np.cos(np.sqrt(x*x + y*y))

X = np.linspace(-2, 2, 20)
Y = np.linspace(-2, 2, 20)

X, Y = np.meshgrid(X, Y)
Z = f(X, Y)

plt.xlabel("x")
plt.ylabel("y")

[v, u] = np.gradient(Z)

C = plt.contour(X, Y, Z)
plt.quiver(X, Y, u, v)
#plt.clabel(C, inline = True)