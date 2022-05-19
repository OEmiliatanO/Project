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

L = 100
W_L = np.exp(-2j * np.pi / L)
l, r = -3, 3

# sample of original function
# n shall be in [0, maxn - 1]
def samplef(n):
	dk = (r - l) / L
	return f(l + dk * n)

# naive DFT
def hatf(k):
	s = 0
	for m in range(L):
		s += samplef(m) * (W_L**(k*m))
	return s

# naive IDFT
def u(n, t, alpha = 1):
	s = 0
	for k in range(L):
		s += hatf(k) * (W_L**(-k*n)) * np.exp(-t * alpha * (k**2))
		#print(np.exp(-t * alpha * (k**2)))
	s /= L
	#print(s)
	return s.real


fig = plt.figure()

X = np.array([*range(L)])
t0 = u(X, 0, alpha = 0.5)
t1 = u(X, 1, alpha = 0.5)
t2 = u(X, 2, alpha = 0.5)
t3 = u(X, 10, alpha = 0.5)
#t1 = u(X, 0.0001, alpha = 0.5)
#t2 = u(X, 0.001, alpha = 0.5)
#t3 = u(X, 0.01, alpha = 0.5)

X = X * ((r - l) / L)
X = X + l

#print(X)

plt.bar(X, t0, width = 0.1, label = 't=0', alpha = 0.3)
plt.bar(X, t1, width = 0.1, label = 't=1', alpha = 0.3)
plt.bar(X, t2, width = 0.1, label = 't=2', alpha = 0.3)
plt.bar(X, t3, width = 0.1, label = 't=10', alpha = 0.3)
#plt.bar(X, t1, width = 0.1, label = 't=0.0001', alpha = 0.3)
#plt.bar(X, t2, width = 0.1, label = 't=0.001', alpha = 0.3)
#plt.bar(X, t3, width = 0.1, label = 't=0.01', alpha = 0.3)

plt.legend(loc = 0)

plt.show()
