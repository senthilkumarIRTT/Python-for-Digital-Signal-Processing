#Program to perform cross correlation

import numpy as np
import scipy as sy
from matplotlib import pyplot as plt

#input sequences

x = eval(input('Enter the input sequence x[n]='))
N1 = len(x)
h = eval(input('Enter the input sequence h[n]='))
N2 = len(h)
N = N1+N2-1
y = np.zeros(N)
for i in range (N2):
    h[N2-1-i]=h[i]
    

#Correlation using Linear convolution built-in function in NumPy
y1 = np.convolve(x,h)
#Correlation using Correlation built-in function in NumPY
y2 = np.correlate(x,h,'full')
print('Auto correlation using NumPy Linear convolution built-in function -correlation result y=\n',y1)
print('Auto correlation using NumPy correlation built-in function - correlation result  y=\n',y2)

m = N-N1
n = N-N2
#Padding zeros to x and h to make their length to N
x =np.pad(x,(0,m),'constant')
h =np.pad(h,(0,n),'constant')

#correlation using formula
for n in range (N):
    for k in range (N):
        if n >= k:
             y[n] = y[n]+x[n-k]*h[k]
         

print('correlation using formula - correlation result y =\n',y)


#RESULT
##Enter the input sequence x[n]=[1,2,1,1]
##Enter the input sequence h[n]=[1,1,2,1]
##Auto correlation using NumPy Linear convolution built-in function -correlation result y=
## [1 3 4 5 4 2 1]
##Auto correlation using NumPy correlation built-in function - correlation result  y=
## [1 3 4 5 4 2 1]
##correlation using formula - correlation result y =
## [1. 3. 4. 5. 4. 2. 1.]
