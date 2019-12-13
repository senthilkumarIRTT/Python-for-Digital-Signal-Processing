#Program to find Discrete Fourier Transform
#Plotting magnitude and phase response
import numpy as np
import math
from numpy.fft import fft,ifft
import scipy as sy
from matplotlib import pyplot as plt

#input sequences

x = eval(input('Enter the input sequence x[n]='))
N = len(x)
X = fft(x,N);
print('Discrete Fourier Transform X[k] =\n',X)
x_n = ifft(X)
print('Inverse Discrete Fourier Transform x[n]=\n',x_n)
x_mag_res = abs(X)
x_phase_res = np.angle(X)
x_real = np.real(x_n)
print('Real values of x[n]=\n',x_real)
print('Magnitude response |X(K)|=\n',x_mag_res)
print('Phase response <X(K)=\n',x_phase_res)
n = np.arange(0,N,1)
#To open a new figure window
fig=plt.figure()
plt.stem(n,x_mag_res,linefmt='grey')
plt.xlabel('Discrete Frequency variable K---->')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.title('Amplitude response')
#To open a new figure window
fig = plt.figure()
plt.stem(n,x_phase_res,linefmt='grey')
plt.xlabel('Discrete Frequency variable K---->')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.title('Phase response')
plt.show()







#RESULT
##Enter the input sequence x[n]=[0,1,2,3]
##Discrete Fourier Transform X[k] =
## [ 6.+0.j -2.+2.j -2.+0.j -2.-2.j]
##Inverse Discrete Fourier Transform x[n]=
## [0.+0.j 1.+0.j 2.+0.j 3.+0.j]
##Real values of x[n]=
## [0. 1. 2. 3.]
##Magnitude response |X(K)|=
## [6.         2.82842712 2.         2.82842712]
##Phase response <X(K)=
## [ 0.          2.35619449  3.14159265 -2.35619449]
