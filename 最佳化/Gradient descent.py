# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 18:57:41 2021

@author: Hens
"""

import numpy as np
import matplotlib.pyplot as plt

def generateData(n):
    x = np.arange(-5, 5, 10 / (n - 1))
    y = 3 * x + 2 + np.random.rand(len(x)) * 6
    return x, y

dataX, dataY = generateData(20)

X = np.linspace(-5, 10, 256)
Y = np.linspace(-5, 10, 256)
X, Y = np.meshgrid(X, Y)

def pic(a, b):
    err = X * 0
    i = 0
    for aa, bb in zip(a, b):
        j = 0
        for A, B in zip(aa, bb):
            for x, y in zip(dataX, dataY):
                err[i][j] += np.abs(A * x + B - y)
            j += 1
        i += 1
    return err

Z = pic(X, Y)
plt.xlabel("x")
plt.ylabel("y")
C = plt.contour(X, Y, Z)

def f(a, b):
    err = 0
    for x, y in zip(dataX, dataY):
        err += np.abs(a * x + b - y)
    return err

def dfdx(x0, y0):
    h = 1e-6
    return (f(x0 + h, y0) - f(x0, y0)) / h

def dfdy(x0, y0):
    h = 1e-6
    return (f(x0, y0 + h) - f(x0, y0)) / h

def grad(x, y):
    return np.array([dfdx(x, y), dfdy(x, y)])

a = 0.021

preP = np.array([.0, .0])
nowP = preP - grad(preP[0], preP[1]) * a
plt.plot((preP[0], nowP[0]), (preP[1], nowP[1]), 'bo-')
plt.savefig('0.png')

for i in range(20):
    preP = nowP
    nowP = preP - grad(preP[0], preP[1]) * a
    plt.plot((preP[0], nowP[0]), (preP[1], nowP[1]), 'ro-')
    plt.savefig('%d.png' %(i + 1))
    
print(nowP)
print(f(nowP[0], nowP[1]))
    