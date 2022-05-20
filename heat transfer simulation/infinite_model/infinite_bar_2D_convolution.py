import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

eps = 1e-8

def sec(x):
	return 1 / np.cos(x);

# original function
def f(x):
	#return np.piecewise(x, [np.less_equal(abs(x), 1), np.logical_not(np.less_equal(abs(x), 1))], [1, 0])
	#return np.exp(-x**2)
	return np.sinc(x)


def G(x, t, alpha):
	return 0.5 * np.sqrt(1 / (t * alpha * np.pi)) * np.exp(-(x**2) / (4 * t * alpha))

def u(x, t, alpha = 1):
	maxn = 10000
	dk = (np.pi) / maxn
	s = 0
	for n in range(1, maxn):
		s += f(x - np.tan(-np.pi / 2 + dk * n)) * G(np.tan(-np.pi / 2 + dk * n), t, alpha) * (sec(-np.pi / 2 + dk * n) ** 2)
	s *= dk
	return s

fig = plt.figure()

X = np.linspace(-3, 3, 512)
t0 = u(X, 0.0001, alpha = 0.5)
t1 = u(X, 1, alpha = 0.5)
t2 = u(X, 2, alpha = 0.5)
t3 = u(X, 4, alpha = 0.5)
t4 = u(X, 10, alpha = 0.5)
t5 = u(X, 30, alpha = 0.5)
t6 = u(X, 80, alpha = 0.5)


plt.plot(X, t0, label = 't=0.001')
plt.plot(X, t1, label = 't=1')
plt.plot(X, t2, label = 't=2')
plt.plot(X, t3, label = 't=4')
plt.plot(X, t4, label = 't=10')
plt.plot(X, t5, label = 't=30')
plt.plot(X, t6, label = 't=80')


plt.legend(loc = 0)

plt.show()
