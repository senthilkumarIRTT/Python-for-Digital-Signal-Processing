#Power spectrum Estimation of discrete sequence
#x[n] = (0.9)^n, 0<=n<20
import numpy as np
from numpy.fft import fft,ifft
import scipy as sy
from matplotlib import pyplot as plt
N = 16 #16 point dft
n = np.arange(0,20,1)
x1 = (0.9**n) #given discrete sequence
x = x1[0:15]
X = fft(x,N)
X_mag = abs(X)
Pxx = ((abs(X))**2)/N
K = np.arange(0,len(Pxx),1)
plt.figure(1)
plt.stem(K,Pxx,'grey')
plt.xlabel('Discrete Frequency Variable K---->')
plt.ylabel('Pxx-Periodogram---->')
plt.grid(True, which='both')
plt.title('Power Spectrum Estimation of Discrete Sequence')
plt.figure(2)
plt.stem(K,X_mag,'red')
plt.xlabel('Discrete Frequency Variable K---->')
plt.ylabel('Magnitude Response |X(K)|---->')
plt.grid(True, which='both')
plt.title('DFT of Discrete Sequence')
plt.show()

