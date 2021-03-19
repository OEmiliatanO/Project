# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:41:20 2020

@author: Hens
"""


import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 2 ** (4 - x)
g = lambda x: x

c = lambda x: 2 ** x
d = lambda x: 4 - x

x = np.arange(1, 5, .125)
y1 = f(x)
y2 = g(x)

y3 = c(x)
y4 = d(x)

plt.figure()
plt.xlabel("x")
plt.ylabel("y")
#plt.plot(x, y1)
#plt.plot(x, y2)

plt.plot(x, y3)
plt.plot(x, y4)