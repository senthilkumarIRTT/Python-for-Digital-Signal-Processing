#Python program for stem plot
#with Amplitude = 5 units
import numpy as np
import scipy as sy
from matplotlib import pyplot as plt

t = np.arange(0,1,0.01)
#frequency = 2 Hz
f = 2
#Amplitude of sine wave = 1
PI = 22/7
a = np.sin(2*PI*2*t)
a = 5*a;
#plt.stem(t,a,linefmt='grey',markerfmt='C',bottom =0.0)
plt.stem(t,a,linefmt='grey',markerfmt='D',bottom =0.0)
plt.xlabel('Time')
#Y-axis label
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.title('Discrete Time Sine Wave')
plt.show()
