from __future__ import division
import math
import Image
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from scipy import misc, fftpack, interpolate
import scipy.ndimage.interpolation

N = 256             # the number of points
Fs = 8000.          # the sampling rate
Ts = 1./Fs          # the sampling period
freqStep = Fs/N     # resolution of the frequency in frequency domain
f = 10*freqStep     # frequency of the sine wave; folded by integer freqStep
t = np.arange(N)*Ts    # x ticks in time domain, t = n*Ts
y = np.cos(2*np.pi*f*t)   # Signal to analyze
Y = fftpack.fft(y)          # Spectrum
Y = fftpack.fftshift(Y)     # middles the zero-point's axis

figure(figsize=(8,8))
subplots_adjust(hspace=.4)

# Plot time data
subplot(3,1,1)
plot(t, y, '.-')
grid("on")
xlabel('Time (seconds)')
ylabel('Amplitude')
title('Sinusoidal signals')
axis('tight')

freq = freqStep * arange(-N/2, N/2)  # x ticks in frequency domain

# Plot spectral magnitude
subplot(3,1,2)
plot(freq, abs(Y), '.-b')
grid("on")
xlabel('Frequency')
ylabel('Magnitude (Linear)')

# Plot phase
subplot(3,1,3)
plot(freq, angle(Y), '.-b')
grid("on")
xlabel('Frequency')
ylabel('Phase (Radian)')

show()

