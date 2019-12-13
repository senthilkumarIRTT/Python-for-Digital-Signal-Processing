#Program to perform linear convolution
import numpy as np
import scipy as sy
from matplotlib import pyplot as plt
#impulse response
h = [1,2,3,3,2,1];
#input response
x = [1,2,3,4,5];
N1 = len(x)
N2 = len(h)
N = N1+N2-1
y = np.zeros(N)
#x = [[x],[np.zeros(N-N1)]]
#h = [h,np.zeros(N-N2)]
#Linear convolution using built-in function in NumPy
y1 = np.convolve(x,h)
m = N-N1
n = N-N2
#Padding zeros to x and h to make their length to N
x =np.pad(x,(0,m),'constant')
h =np.pad(h,(0,n),'constant')

#Linear convolution using convolution sum formula
for n in range (N):
    for k in range (N):
        if n >= k:
             y[n] = y[n]+x[n-k]*h[k]
         

print('Linear convolution using convolution sum formula output response y =\n',y)
print('Linear convolution using NumPy built-in function output response y=\n',y1)

#RESULT
#Linear convolution using convolution sum formula output response y =
#[ 1.  4. 10. 19. 30. 36. 35. 26. 14.  5.]
#Linear convolution using NumPy built-in function output response y=
#[ 1  4 10 19 30 36 35 26 14  5]
