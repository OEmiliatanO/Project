# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib

import mpmath
mpmath.dps = 5
mpmath.pretty = True
def normalize(x):
    return mpmath.sin(mpmath.arg(x))

f = lambda x: mpmath.sin(x) * mpmath.cos(x)

fig = plt.figure()

ax = Axes3D(fig)

ax.view_init(90, 0)

#ax.set_zlim3d(-3, 3)

ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('c')

a = np.arange(-5, 5, .125)
b = np.arange(-5, 5, .125)

A, B = np.meshgrid(a, b)
an, bn = A.shape
C, D = A * 0, A * 0

for i in range(an):
    for j in range(bn):
        try:
            z = mpmath.mp.mpc(A[i, j], B[i, j])
            w = f(z)
            
            #print(w)
            
            C[i, j] = w.real
            D[i, j] = w.imag
            
        except (ValueError, TypeError, ZeroDivisionError):
            # print(A[i, j], B[i, j])
            pass


color_dimension = D
minn, maxx = color_dimension.min(), color_dimension.max()
norm = matplotlib.colors.Normalize()
m = plt.cm.ScalarMappable(norm = norm, cmap = 'jet')
fcolors = m.to_rgba(color_dimension)

surf = ax.plot_surface(A, B, C, rstride=1, cstride=1, facecolors=fcolors, vmin=minn, vmax=maxx)

plt.colorbar(m)


#ax.plot_surface(A, B, C, cmap = 'jet')
#ax.plot_wireframe(A, B, C, rstride=2, cstride=2)

#cmap = plt.get_cmap('Reds')
