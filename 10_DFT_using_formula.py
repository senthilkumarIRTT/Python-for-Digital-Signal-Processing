#Program to find Discrete Fourier Transform
#using own function
import numpy as np
import math
import cmath
from numpy.fft import fft,ifft
import scipy as sy
from matplotlib import pyplot as plt

#input sequences

x = eval(input('Enter the input sequence x[n]='))
N = len(x)

print('N=\n',N)

X = eval(input('Assigna N complex zeros 0+0j to X[K]='))
x_mag_res =  eval(input('Assign N zeros 0 to |X[K]|='))

print('X=\n',X)

def dft(x,N):
    print('x=\n',x)
    print('N=\n',N)
    for K in range(N):
        temp = 0+0j
        for n in range(N):
            temp = temp+x[n]*cmath.exp(-2*cmath.sqrt(-1)*cmath.pi*n*K/N)
        X[K] = temp
        x_mag_res[K] = abs(X[K])
    return;
dft(x,N)


print('Discrete Fourier Transform X[k] =\n',X)

def idft(X,N):
    print('X=\n',X)
    print('N=\n',N)
    for n in range(N):
        temp = 0+0j
        for K in range(N):
            temp = temp+X[K]*cmath.exp(2*cmath.sqrt(-1)*cmath.pi*n*K/N)
        x[n] = temp/N
        
    return;
idft(X,N)
x_n = np.real(x)
x_n = np.round(x_n,decimals=0)
print('Inverse Discrete Fourier Transform x[n]=\n',x_n)
#x_mag_res = abs(X)
x_phase_res = np.angle(X)
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
##N=
## 4
##Assigna N complex zeros 0+0j to X[K]=[0+0j,0+0j,0+0j,0+0j]
##Assign N complex zeros 0+0j to |X[K]|=[0,0,0,0]
##X=
## [0j, 0j, 0j, 0j]
##x=
## [0, 1, 2, 3]
##N=
## 4
##Discrete Fourier Transform X[k] =
## [(6+0j), (-2.0000000000000004+1.9999999999999998j), (-2-7.34788079488412e-16j), (-1.9999999999999984-2.000000000000001j)]
##X=
## [(6+0j), (-2.0000000000000004+1.9999999999999998j), (-2-7.34788079488412e-16j), (-1.9999999999999984-2.000000000000001j)]
##N=
## 4
##Inverse Discrete Fourier Transform x[n]=
## [0. 1. 2. 3.]
##Magnitude response |X(K)|=
## [6.0, 2.8284271247461903, 2.0, 2.82842712474619]
##Phase response <X(K)=
## [ 0.          2.35619449 -3.14159265 -2.35619449]
##
