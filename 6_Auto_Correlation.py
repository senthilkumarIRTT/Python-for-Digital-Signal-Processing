#Program to perform auto correlation

import numpy as np
import scipy as sy
from matplotlib import pyplot as plt

#input response
#x = [1,0,0,2]
x = eval(input('Enter the input sequence x[n]='))
N1 = len(x)
h=np.zeros(N1)
N2 = len(x)
N = N1+N2-1
y = np.zeros(N)
for i in range (N1):
    h[N1-1-i]=x[i]
    

#Correlation using Linear convolution built-in function in NumPy
y1 = np.convolve(x,h)
#Correlation using Correlation built-in function in NumPY
y2 = np.correlate(x,x,'full')
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
##Auto correlation using NumPy Linear convolution built-in function -correlation result y=
## [2. 0. 0. 5. 0. 0. 2.]
##Auto correlation using NumPy correlation built-in function - correlation result  y=
## [2 0 0 5 0 0 2]
##correlation using formula - correlation result y =
## [2. 0. 0. 5. 0. 0. 2.]
