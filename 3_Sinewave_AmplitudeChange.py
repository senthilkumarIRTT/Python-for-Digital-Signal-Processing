#Python program for continuous and discrete sine wave plot
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
#Plot a continuous sine wave
fig, axs = plt.subplots(1,2)
axs[0].plot(t,a)
#Give a title for the sine wave
axs[0].set_title('Continuous Sine wave')
#X-axis label
axs[0].set(xlabel='Time')
#Y-axis label
axs[0].set(ylabel='Amplitude')
axs[0].grid(True, which='both')
axs[0].axhline(y=0, color='k')
axs[1].plot(t,a,'--r')
#Give a title for the sine wave
axs[1].set_title('Discrete Sine wave')
#X-axis label
axs[1].set(xlabel='Time')
#Y-axis label
axs[1].set(ylabel='Amplitude')
axs[1].grid(True, which='both')
axs[1].axhline(y=0, color='k')
#Display the sine wave
plt.show()
