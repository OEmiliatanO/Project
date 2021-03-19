# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:52:19 2020

@author: Hens
"""


import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

f = lambda x, y: np.log(np.fabs(x - 1)) * (5 * y - 1) - 1

fig = plt.figure()
ax = Axes3D(fig)

ax.view_init(60, 90)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#ax.set_zlim3d(-3, 3)

x = np.arange(-5, 10, .125)
y = np.arange(-5, 10, .125)

X, Y = np.meshgrid(x, y)

Z = f(X, Y)

ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'rainbow')