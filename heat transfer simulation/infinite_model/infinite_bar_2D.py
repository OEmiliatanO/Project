import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

eps = 1e-8

def sec(x):
	return 1 / np.cos(x);

# original function
def f(x):
	#return np.piecewise(x, [np.less_equal(abs(x), 1), np.logical_not(np.less_equal(abs(x), 1))], [1, 0])
	return np.exp(-x**2)
	#return np.sinc(x)

# tan(k)-subtitute version
def sub_u(x, t, alpha = 1, maxn = 10000):
	dk = np.pi / maxn
	coe = dk / np.sqrt(np.pi)
	s = 0
	for n in range(1, maxn):
		# if f(np.tan(-np.pi + dk * n)) <= eps: continue;
		s += f(x + 2 * np.tan(-np.pi / 2 + dk * n) * np.sqrt(t * alpha)) * np.exp(-np.tan(-np.pi / 2 + dk * n) ** 2) * (sec(-np.pi / 2 + dk * n) ** 2)
		"""
		print("\t%f" % (f(np.tan(-np.pi + dk * n))), end = ' ')
		print("\t%f" % (np.exp(-((x - np.tan(-np.pi / 2 + dk * n)) ** 2)/(4 * t * alpha))), end = ' ')
		print("\t%f" % (-((x - np.tan(-np.pi / 2 + dk * n)) ** 2)/(4 * t * alpha)), end = ' ')
		print("\t%f" % ((sec(-np.pi / 2 + dk * n) ** 2)))
		"""
		
	s += f(x + 2 * np.tan(-np.pi / 2 + dk) * np.sqrt(t * alpha)) * np.exp(-np.tan(-np.pi / 2 + dk) ** 2) * (sec(-np.pi / 2 + dk) ** 2)
	s += f(x + 2 * np.tan(np.pi / 2 - dk) * np.sqrt(t * alpha)) * np.exp(-np.tan(np.pi / 2 - dk) ** 2) * (sec(np.pi / 2 - dk) ** 2)
	s *= coe
	return s

# non-subtitute version
def nonsub_u(x, t, alpha = 1, L = -100, R = 100, maxn = 10000):
	dk = (R - L) / maxn
	coe = dk / np.sqrt(np.pi)
	s = 0
	for n in range(1, maxn - 1):
		s += f(x + 2 * (L + dk * n) * np.sqrt(t * alpha)) * np.exp(-(L + dk * n)**2)
	s *= coe
	return s

"""
print(altu(0, 0.1))
print(u(0, 0.1))
print(altu(0, 1))
print(u(0, 1))
print(u(0, 2))
print(u(0, 2))
"""

fig = plt.figure()

X = np.linspace(-3, 3, 1024)

plt.plot(X, sub_u(X, 0, alpha = 0.5), label = 't=0')
#plt.plot(X, sub_u(X, 1, alpha = 0.5), label = 't=1')
#plt.plot(X, sub_u(X, 2, alpha = 0.5), label = 't=2')
#plt.plot(X, sub_u(X, 4, alpha = 0.5), label = 't=4')
plt.plot(X, sub_u(X, 10, alpha = 0.5), label = 't=10')
plt.plot(X, sub_u(X, 20, alpha = 0.5), label = 't=20')
plt.plot(X, sub_u(X, 30, alpha = 0.5), label = 't=30')

plt.legend(loc = 0)
plt.show()
