# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:20:48 2021

@author: Hens
"""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x, y: (x*x + y*y/3)

def dfdx(x0, y0):
    h = 1e-6
    return (f(x0 + h, y0) - f(x0, y0)) / h

def dfdy(x0, y0):
    h = 1e-6
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

def grad(x, y):
    return np.array([dfdx(x, y), dfdy(x, y)])

X = np.linspace(-5, 9, 512)
Y = np.linspace(-5, 9, 512)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)
plt.xlabel("x")
plt.ylabel("y")
C = plt.contour(X, Y, Z)


a = 0.4

x0 = 8.3
y0 = 7.6

GD_preP = np.array([x0, y0])
GD_nowP = GD_preP - grad(GD_preP[0], GD_preP[1]) * a

NT_preP = np.array([x0, y0])
k = -np.linalg.solve(H(NT_preP[0], NT_preP[1]), grad(NT_preP[0], NT_preP[1]))
NT_nowP = NT_preP + k

plt.plot((GD_preP[0], GD_nowP[0]), (GD_preP[1], GD_nowP[1]), 'ro-')
plt.plot((NT_preP[0], NT_nowP[0]), (NT_preP[1], NT_nowP[1]), 'bo-')
plt.savefig('0.png')

for i in range(10):
    GD_preP = GD_nowP
    GD_nowP = GD_preP - grad(GD_preP[0], GD_preP[1]) * a
    
    NT_preP = NT_nowP
    k = -np.linalg.solve(H(NT_preP[0], NT_preP[1]), grad(NT_preP[0], NT_preP[1]))
    NT_nowP = NT_preP + k
    
    plt.plot((GD_preP[0], GD_nowP[0]), (GD_preP[1], GD_nowP[1]), 'ro-')
    plt.plot((NT_preP[0], NT_nowP[0]), (NT_preP[1], NT_nowP[1]), 'bo-')
    
    plt.savefig('%d.png' %(i + 1))
    
print(GD_nowP)
print(f(GD_nowP[0], GD_nowP[1]))

print(NT_nowP)
print(f(NT_nowP[0], NT_nowP[1]))
