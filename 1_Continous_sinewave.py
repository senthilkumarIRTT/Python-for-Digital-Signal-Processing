import numpy as np
import scipy as sy
from matplotlib import pyplot as plt

t = np.arange(0,1,0.01)
#frequency = 2 Hz
f = 2
#Amplitude of sine wave = 1
PI = 22/7
a = np.sin(2*PI*2*t)
#Plot a continuous sine wave
plt.plot(t,a)
#Give a title for the sine wave
plt.title('Sine wave')
#X-axis label
plt.xlabel('Time')
#Y-axis label
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
#Display the sine wave
plt.show()
