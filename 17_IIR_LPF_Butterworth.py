#IIR Analog and Digital Butterworth LPF filter design
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from pylab import clf
#Analog low pass butterworth filter, order =3, fc=50Hz
#b = numerator coefficients, a = denominator coefficients
#w = frequency variable, h= frequency response

b,a = signal.iirfilter(3,50,btype ='low',analog=True, ftype ='butter')
w,h = signal.freqs(b,a,1000)

fig1 = plt.figure(1)
ax = fig1.add_subplot(1,1,1)
ax.semilogx(w,20*np.log10(np.maximum(abs(h),1e-5)))
ax.set_title('Butterworth IIR Analog LPF frequency response')
ax.set_xlabel('Frequency in Hz---->')
ax.set_ylabel('Amplitude in dB----->')
#ax.axis((10,1000,-100,10))
ax.grid(which='both',axis='both')
plt.show()

#Digital low pass butterworth filter, order =3, fc=50Hz
fs =1000
sos = signal.iirfilter(3,50/fs,btype ='low',analog=False, ftype ='butter',output='sos')
w,h = signal.sosfreqz(sos,1000)


fig2 = plt.figure(2)
clf()
ax = fig2.add_subplot(1,1,1)
ax.plot(w/np.pi,20*np.log10(np.maximum(abs(h),1e-5)))
ax.set_title('Butterworth IIR Digital LPF frequency response')
ax.set_xlabel('Normalized Digital Frequency ---->')
ax.set_ylabel('Amplitude in dB----->')
#ax.axis((10,1000,-100,10))
ax.grid(which='both',axis='both')
plt.show()

#Result
##>>> b
##array([125000.])
##>>> a
##array([1.00e+00, 1.00e+02, 5.00e+03, 1.25e+05])
##>>> sos
##array([[ 4.16546139e-04,  8.33092278e-04,  4.16546139e-04,
##         1.00000000e+00, -8.54080685e-01,  0.00000000e+00],
##       [ 1.00000000e+00,  1.00000000e+00,  0.00000000e+00,
##         1.00000000e+00, -1.83207671e+00,  8.54913778e-01]])
##>>> 
