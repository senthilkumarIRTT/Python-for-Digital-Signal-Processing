#IIR Analog and Digital Butterworth HPF filter design
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from pylab import clf
#Analog High pass butterworth filter, order =3, fc=100Hz
#b = numerator coefficients, a = denominator coefficients
#w = frequency variable, h= frequency response
b,a = signal.iirfilter(3,100,btype ='high',analog=True, ftype ='butter')
w,h = signal.freqs(b,a,1000)

fig1 = plt.figure(1)
ax = fig1.add_subplot(1,1,1)
ax.semilogx(w,20*np.log10(np.maximum(abs(h),1e-5)))
ax.set_title('Butterworth IIR Analog HPF frequency response')
ax.set_xlabel('Frequency in Hz---->')
ax.set_ylabel('Amplitude in dB----->')
#ax.axis((10,1000,-100,10))
ax.grid(which='both',axis='both')
plt.show()

#Digital High pass butterworth filter, order =3, fc=100Hz
fs =1000
sos = signal.iirfilter(3,100/fs,btype ='high',analog=False, ftype ='butter',output='sos')
w,h = signal.sosfreqz(sos,1000)


fig2 = plt.figure(2)
clf()
ax = fig2.add_subplot(1,1,1)
ax.plot(w/np.pi,20*np.log10(np.maximum(abs(h),1e-5)))
ax.set_title('Butterworth IIR Digital HPF frequency response')
ax.set_xlabel('Normalized Digital Frequency ---->')
ax.set_ylabel('Amplitude in dB----->')
#ax.axis((10,1000,-100,10))
ax.grid(which='both',axis='both')
plt.show()

#Result
##>>> b
##array([1., 0., 0., 0.])
##>>> a
##array([1.e+00, 2.e+02, 2.e+04, 1.e+06])
##>>> sos
##array([[ 0.72944072, -0.72944072,  0.        ,  1.        , -0.72654253,
##         0.        ],
##       [ 1.        , -2.        ,  1.        ,  1.        , -1.64755222,
##         0.73233892]])
##>>> 
