# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:19:32 2021

@author: Hens
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f = lambda x, y : np.sin(x) * np.power(y ** 2, 1./3.)

fig = plt.figure()
ax = Axes3D(fig)

ax.view_init(45, 90)

X = np.linspace(-2, 2, 256)
Y = np.linspace(-2, 2, 256)
X, Y = np.meshgrid(X, Y)

Z = f(X, Y)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'jet')

ax.contour(X, Y, Z, zdir = 'z', offset = Z.min())
#ax.contour(X, Y, Z, zdir = 'x', offset = X.min())
#ax.contour(X, Y, Z, zdir = 'y', offset = Y.min())
