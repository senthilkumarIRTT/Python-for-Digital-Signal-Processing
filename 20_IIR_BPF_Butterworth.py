#IIR Analog and Digital Butterworth BPF filter design
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from pylab import clf
#Analog Band pass butterworth filter, order =3, fc1=100Hz, fc2=300Hz
#b = numerator coefficients, a = denominator coefficients
#w = frequency variable, h= frequency response

b,a = signal.iirfilter(3,[100,300],btype ='bandpass',analog=True, ftype ='butter')
w,h = signal.freqs(b,a,1000)

fig1 = plt.figure(1)
ax = fig1.add_subplot(1,1,1)
ax.semilogx(w,20*np.log10(np.maximum(abs(h),1e-5)))
ax.set_title('Butterworth IIR Analog BPF frequency response')
ax.set_xlabel('Frequency in Hz---->')
ax.set_ylabel('Amplitude in dB----->')
#ax.axis((10,1000,-100,10))
ax.grid(which='both',axis='both')
plt.show()


#Digital Band pass butterworth filter, order =3, fc1=100Hz, fc2=300Hz
fs =1000
sos = signal.iirfilter(3,[100/fs,300/fs],btype ='bandpass',analog=False, ftype ='butter',output='sos')
w,h = signal.sosfreqz(sos,1000)


fig2 = plt.figure(2)
clf()
ax = fig2.add_subplot(1,1,1)
ax.plot(w/np.pi,20*np.log10(np.maximum(abs(h),1e-5)))
ax.set_title('Butterworth IIR Digital BPF frequency response')
ax.set_xlabel('Normalized Digital Frequency ---->')
ax.set_ylabel('Amplitude in dB----->')
#ax.axis((10,1000,-100,10))
ax.grid(which='both',axis='both')
plt.show()

#Result
##>>> b
##array([8000000.,       0.,       0.,       0.])
##>>> a
##array([1.0e+00, 4.0e+02, 1.7e+05, 3.2e+07, 5.1e+09, 3.6e+11, 2.7e+13])
##>>> sos
##array([[ 0.01809893,  0.03619787,  0.01809893,  1.        , -1.28407904,
##         0.50952545],
##       [ 1.        ,  0.        , -1.        ,  1.        , -1.0263941 ,
##         0.65079467],
##       [ 1.        , -2.        ,  1.        ,  1.        , -1.73866033,
##         0.83854915]])
