import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

eps = 1e-8

def sec(x):
	return 1 / np.cos(x);

l = np.pi
maxn = 1000
K = [0] * maxn

# original function
def f(x):
	#return np.piecewise(x, [np.logical_and(np.less_equal(x, 3), np.greater_equal(x,2)), np.logical_not(np.logical_and(np.less_equal(x, 3), np.greater_equal(x,2)))], [1, 0])
	return np.cos(x)
	#return np.cos(np.sin(x * np.pi / l))
	#return 1/3 * (x**3) - l/2 * (x**2)
	#return (1/5) * (x**5) - ((7 + l) / 4) * (x**4) + ((10 + 7 * l) / 3) * (x**3) - 5*l *(x**2)
	#return np.sin(np.pi * x**2 / (2 * l**2))

def calKn_cos():
	dl = l / maxn
	for n in range(maxn):
		for i in range(maxn):
			K[n] += f(dl * i) * np.cos(np.pi * n * dl * i / l)
		K[n] *= (2 * dl / l)
	K[0] /= 2

def calKn_sin():
	dl = l / maxn
	for n in range(maxn):
		for i in range(maxn):
			K[n] += f(dl * i) * np.sin(np.pi * n * dl * i / l)
		K[n] *= (2 * dl / l)

def calKn(mode = "cos"):
	if mode == "cos":
		calKn_cos()
	elif mode == "sin":
		calKn_sin()
	else:
		print("error argument")

def u(x, t, alpha = 1, maxn = 1000):
	s = 0
	for n in range(maxn):
		s += K[n] * np.cos(x * n * np.pi / l) * np.exp(-alpha * t * (n * np.pi / l) ** 2)
	return s

fig = plt.figure()

X = np.linspace(0.5, l - 0.5, 1024)

calKn()

plt.plot(X, u(X, 0, alpha = 0.5), label = 't=0')
plt.plot(X, u(X, 1, alpha = 0.5), label = 't=1')
plt.plot(X, u(X, 2, alpha = 0.5), label = 't=2')
plt.plot(X, u(X, 4, alpha = 0.5), label = 't=4')

plt.legend(loc = 0)

plt.show()

