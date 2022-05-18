import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

eps = 1e-8

def sec(x):
	return 1 / np.cos(x);

l = 5
maxn = 1000
K = [0] * maxn

# original function
def f(x):
	#return np.piecewise(x, [np.less_equal(abs(x), 1), np.logical_not(np.less_equal(abs(x), 1))], [1, 0])
	return np.sin(x)

def calKn_cos():
	dl = l / maxn
	for n in range(maxn):
		for i in range(maxn):
			K[n] += f(dl * n) * np.cos(np.pi * n * dl * i / l)
		K[n] *= (2 * dl / l)
	K[0] /= 2

def calKn_sin():
	dl = l / maxn
	for n in range(maxn):
		for i in range(maxn):
			K[n] += f(dl * n) * np.sin(np.pi * n * dl * i / l)
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

fig = plt.figure()

X = np.linspace(-10, 10, 1024)

calKn()

plt.plot(X, u(X, 0, alpha = 0.5))
plt.plot(X, u(X, 1, alpha = 0.5))
plt.plot(X, u(X, 2, alpha = 0.5))
plt.plot(X, u(X, 4, alpha = 0.5))

plt.show()
