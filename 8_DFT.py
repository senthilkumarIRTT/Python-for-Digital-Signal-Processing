#Program to Discrete Fourier Transform

import numpy as np
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
x_real = np.real(x_n)
print('Real values of x[n]=\n',x_real)




#RESULT
##Enter the input sequence x[n]=[0,1,2,3]
##Discrete Fourier Transform X[k] =
## [ 6.+0.j -2.+2.j -2.+0.j -2.-2.j]
##Inverse Discrete Fourier Transform x[n]=
## [0.+0.j 1.+0.j 2.+0.j 3.+0.j]
##Real values of x[n]=
## [0. 1. 2. 3.]
