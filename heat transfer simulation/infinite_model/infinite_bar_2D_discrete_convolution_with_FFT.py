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

# heat transfer characteristic function
def G(x, t, alpha):
	return 0.5 * np.sqrt(1 / (t * alpha * np.pi)) * np.exp(-(x**2) / (4 * t * alpha))

L = 256
l, r = -3, 3

sf = np.zeros((L), dtype = complex)
def samplef():
	dk = (r - l) / L
	for i in range(L):
		sf[i] = f(l + dk * i)

sG = np.zeros((L), dtype = complex)
def sampleG(t, alpha):
	dk = (r - l) / L
	for i in range(L):
		sG[i] = G(l + dk * i, t, alpha)

def fft(X, mode = 'fft'):
	tmp = np.zeros((2, (Len:=len(X))), dtype = complex)
	tmp[0] = np.copy(X)
	
	# reorder
	N = len(tmp[0])
	j = 0
	for i in range(1, N):
		k = N >> 1
		while not ((j := j ^ k) & k):
			k >>= 1
		if (i > j):
			tmp[0][i], tmp[0][j] = tmp[0][j], tmp[0][i]
	
	# fft
	N = 2
	W = np.exp((-1 if mode == 'fft' else 1) * 2j * np.pi / N)
	lev = 0
	while N <= Len:
		for i in range(Len):
			if i % N < (N >> 1):
				base = (i // N) * N
				tmp[(lev & 1) ^ 1][(i + (1 << lev)) % N + base] += tmp[lev & 1][i]
				tmp[(lev & 1) ^ 1][i % N + base] += tmp[lev & 1][i]
			else:
				base = (i // N) * N
				tmp[(lev & 1) ^ 1][(i + (1 << lev)) % N + base] += tmp[lev & 1][i] * ( W ** ((i + (1 << lev)) % N) )
				tmp[(lev & 1) ^ 1][i % N + base] += tmp[lev & 1][i] * ( W ** (i % N) )
		tmp[lev & 1] = np.zeros((Len))
		W **= 0.5
		lev += 1
		N <<= 1

	return tmp[(lev) & 1]

def ifft(X):
	return fft(X, mode = 'ifft') / len(X)

def calu(t, alpha):
	dk = (r - l) / L
	if t == 0: return sf[n];
	sampleG(t, alpha)
	
	cpsf = np.append(sf, np.zeros((L)))
	cpsG = np.append(sG, np.zeros((L)))
	s = ifft(fft(cpsf) * fft(cpsG))
	s *= dk
	return s.real

def u(n, t, alpha = 1):
	s = calu(t, alpha)
	return s[n]

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
