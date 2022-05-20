import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

eps = 1e-8

def sec(x):
	return 1 / np.cos(x);

# original function
def f(x):
	return np.piecewise(x, [np.less_equal(abs(x), 1), np.logical_not(np.less_equal(abs(x), 1))], [1, 0])
	#return np.exp(-x**2)
	#return np.sinc(x)

L = 100
l, r = -3, 3

sf = np.array([0.0] * (3*L))

def samplef():
	dk = (r - l) / L
	for i in range(L):
		sf[i] = f(l + dk * i)

def G(x, t, alpha):
	return 0.5 * np.sqrt(1 / (t * alpha * np.pi)) * np.exp(-(x**2) / (4 * t * alpha))

sG = np.array([0.0] * (3*L))
def sampleG(t, alpha):
	dk = (r - l) / L
	for i in range(L):
		sG[i] = G(l + dk * i, t, alpha)

def u(n, t, alpha = 1):
	dk = (r - l) / L
	if t == 0: return sf[n];
	sampleG(t, alpha)
	s = 0
	for m in range(2 * L):
		s += sf[n - m] * sG[m]
	s *= dk
	return s

fig = plt.figure()


samplef()
X = np.array([*range(2 * L)])

t0 = u(X, 0.01, alpha = 0.5)
t1 = u(X, 1, alpha = 0.5)
t2 = u(X, 4, alpha = 0.5)
t3 = u(X, 10, alpha = 0.5)
t4 = u(X, 50, alpha = 0.5)


X = X * ((r - l) / L)
X = X + l*2

plt.bar(X, t0, width = 0.1, label = 't=0.01', alpha = 0.3)
plt.bar(X, t1, width = 0.1, label = 't=1', alpha = 0.3)
plt.bar(X, t2, width = 0.1, label = 't=4', alpha = 0.3)
plt.bar(X, t3, width = 0.1, label = 't=10', alpha = 0.3)
plt.bar(X, t4, width = 0.1, label = 't=50', alpha = 0.3)

plt.legend(loc = 0)

plt.show()
