# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:46:00 2021

@author: Hens
"""

import numpy as np
import matplotlib.pyplot as plt
import math

f = lambda x, y: (2 * x + 5) ** 2 * (213 * y - 0.65) ** 2 - 5

def dfdx(x0, y0):
    h = 1e-5
    return (f(x0 + h, y0) - f(x0, y0)) / h

def dfdy(x0, y0):
    h = 1e-5
    return (f(x0, y0 + h) - f(x0, y0)) / h

def dfdxdx(x0, y0):
    g = 1e-5
    return (dfdx(x0 + g, y0) - dfdx(x0, y0)) / g

def dfdxdy(x0, y0):
    g = 1e-5
    return (dfdx(x0, y0 + g) - dfdx(x0, y0)) / g

def dfdydy(x0, y0):
    g = 1e-5
    return (dfdy(x0, y0 + g) - dfdy(x0, y0)) / g


def H(x0, y0):
    h = [[dfdxdx(x0, y0), dfdxdy(x0, y0)], [dfdxdy(x0, y0), dfdydy(x0, y0)]]
    return h

def grd(x0, y0):
    return [dfdx(x0, y0), dfdy(x0, y0)]

def lenOfVec(v):
    return v[0] * v[0] + v[1] * v[1]

X = np.linspace(-5, 5, 1024)
Y = np.linspace(-5, 5, 1024)

X, Y = np.meshgrid(X, Y)
Z = f(X, Y)
plt.xlabel("x")
plt.ylabel("y")
C = plt.contour(X, Y, Z)
#plt.clabel(C, inline = True)

L = 1

x0 = 0
y0 = 0.3
k = -np.linalg.solve(H(x0, y0), grd(x0, y0))
x1 = x0 + L * k[0]
y1 = y0 + L * k[1]

plt.plot((x0, x1), (y0, y1), 'bo-')
plt.savefig('0.png')

eps = 1e-6

for i in range(9):
    x0 = x1
    y0 = y1
    k = -np.linalg.solve(H(x0, y0), grd(x0, y0))
    x1 = x0 + L * k[0]
    y1 = y0 + L * k[1]
    plt.plot((x0, x1), (y0, y1), 'ro-')
    plt.savefig('%d.png' %(i+1))

print(x0, y0)
print("extreme:", f(x0, y0))
