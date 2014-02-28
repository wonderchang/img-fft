import numpy as np
import pylab as plt
import math
 
x = 300
y = np.zeros(x)
y[240:260] = 200
Y = np.fft.fft(y, 600)
Y = np.fft.fftshift(Y)
Y = abs(Y)

plt.figure(1)
plt.subplot(211)
plt.plot(y)
plt.subplot(212)
plt.plot(Y)
plt.show()
  
