# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 14:26:11 2021

@author: Hens
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#f = lambda x, y : x * np.exp(-(x*x + y*y))

fig = plt.figure()
ax = Axes3D(fig)

ax.view_init(45, 45)

X = np.linspace(-.8, 1, 9)
Y = np.linspace(-.8, 1, 9)
Z = np.linspace(-.8, 1, 3)

X, Y, Z = np.meshgrid(X, Y, Z)

#Z = f(X, Y)

u = np.sin(X) * np.cos(Y) 
v = -np.cos(X) * np.cos(Z)
w = np.cos(Y) * np.sin(Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'jet')
ax.quiver(X, Y, Z, u, v, w, length = .1, normalize=True)