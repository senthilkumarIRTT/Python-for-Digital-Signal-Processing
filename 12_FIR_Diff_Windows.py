#Windows for FIR filter Design

from numpy import pi, arange
from scipy import signal
import matplotlib.pyplot as plt

N = eval(input('Number of taps=\n'))
Hamm_window = signal.hamming(N)
Hann_window = signal.get_window('hanning',N)
Barlett_window = signal.get_window('bartlett',N)
Blackman_window = signal.get_window('blackman',N)
n = arange(0,N,1)
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(n,Hamm_window,'grey',label='Hamming Window')
ax.plot(n,Hann_window,'red',label='Hanning Window')
ax.plot(n,Barlett_window,'green',label='Bartlett Window')
ax.plot(n,Blackman_window,'blue',label = 'Blackman Window')
plt.xlabel('samples n------>')
plt.ylabel('Window Amplitude W------->')
plt.title('FIR Filter Window functions ------>')
plt.grid(True, which='both')
ax.legend()
#plt.legend(loc='upper center',bbox_to_anchor=(1.45,0.8),shadow=True,ncol=1)
plt.show()
