# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:37:40 2021

@author: Hens
"""

import numpy as np
import matplotlib.pyplot as plt

f1 = open("function1.txt", 'r')
f2 = open("function2.txt", 'r')

x = np.arange(-1, 1, 0.001)

orgFun = []
predictFun1 = []
predictFun2 = []
x = []
y = []

for cnt in x:
    s = f1.readline()
    orgFun.append(float(s.strip())) #real
    s = f1.readline()
    predictFun1.append(float(s.strip())) #predict

orgFun = []
for cnt in x:
    s = f2.readline()
    orgFun.append(float(s.strip())) #real
    s = f2.readline()
    predictFun2.append(float(s.strip())) #predict

orgFun = np.array(orgFun)
predictFun1 = np.array(predictFun1)
predictFun2 = np.array(predictFun2)

plt.figure()
plt.xlabel("x")
plt.ylabel("y")

plt.plot(x, orgFun, 'r')
plt.plot(x, predictFun1, 'g')
plt.plot(x, predictFun2, 'b')

dotf = open("xy.txt", 'r')
n = int(dotf.readline().strip())

for i in range(n):
    s = dotf.readline()
    x.append(float(s.strip()))
    s = dotf.readline()
    y.append(float(s.strip()))

plt.scatter(x, y)

plt.show()
