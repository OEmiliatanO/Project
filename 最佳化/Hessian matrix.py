# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:46:00 2021

@author: Hens
"""

import numpy as np
import math
import matplotlib.pyplot as plt

f = lambda x, y: x * np.exp(-x * x - y * y)

def dfdxdx(x0, y0):
    g = 1e-5
    h = 1e-5
    return (f(x0 + g + h, y0) - f(x0 + g, y0) - f(x0 + h, y0) + f(x0, y0)) / g / h
def dfdxdy(x0, y0):
    g = 1e-5
    h = 1e-5
    return (f(x0 + g, y0 + h) - f(x0 + g, y0) - f(x0, y0 + h) + f(x0, y0)) / g / h
def dfdydy(x0, y0):
    g = 1e-5
    h = 1e-5
    return (f(x0, y0 + g + h) - f(x0, y0 + g) - f(x0, y0 + h) + f(x0, y0)) / g / h

def dfdx(x0, y0):
    h = 1e-5
    return (f(x0 + h, y0) - f(x0, y0)) / h

def dfdy(x0, y0):
    h = 1e-5
    return (f(x0, y0 + h) - f(x0, y0)) / h

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
plt.clabel(C, inline = True)

L = 1

x0 = 1
y0 = 0.2
k = -np.linalg.solve(H(x0, y0), grd(x0, y0))
x1 = x0 + L * k[0]
y1 = y0 + L * k[1]

plt.plot((x0, x1), (y0, y1), 'bo-')
plt.savefig('0.png')

eps = 1e-6

for i in range(10):
    x0 = x1
    y0 = y1
    k = -np.linalg.solve(H(x0, y0), grd(x0, y0))
    x1 = x0 + L * k[0]
    y1 = y0 + L * k[1]
    plt.plot((x0, x1), (y0, y1), 'ro-')
    plt.savefig('%d.png' %(i+1))

print(x0, y0)
print("extreme:", f(x0, y0))
