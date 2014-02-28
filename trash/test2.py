import numpy as np
import pylab as py
from scipy import misc, fftpack
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import Image

n = 2**10
I = np.arange(1, n)
x = I - n / 2
y = n / 2 - I

R = 10
print "n = ", n
print "I = ", I
print "x = ", x
print "y = ", y
print "R = ", R



fname = 'plot.png'
image = Image.open(fname).convert("L")
arr = np.asarray(image)
plt.imshow(arr, cmap = cm.Greys_r)
#plt.show()


X = x[:, np.newaxis]
Y = y[np.newaxis, :]

M = X**2 + Y**2 < R**2

plt.figure()
plt.imshow(M)
plt.show()


'''
D1 = fftpack.fft2(M)
D2 = fftpack.fftshift(D1)

abs_image = np.abs(D2)
#plt.plot(abs_image)
#plt.savefig("plot2.png", dpi=96)

plt.figure()
plt.title("Target")
plt.imshow(abs_image)
plt.show()
'''
