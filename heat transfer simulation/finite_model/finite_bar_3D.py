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
ax = plt.axes(projection = '3d')

X = np.linspace(0.5, l - 0.5, 1024)
T = np.linspace(0, 10, 512)

calKn()

X, T = np.meshgrid(X, T)
U = u(X, T, alpha = 0.5)

ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('temperature')
ax.plot_surface(X, T, U, cmap = 'rainbow')

plt.show()
