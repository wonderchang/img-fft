import numpy as np
import pylab as py
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import Image
from scipy import misc, fftpack

fname = 'pic.jpg'
image = Image.open(fname).convert("L")
arr = np.asarray(image)
pic = Image.new('L', (99, 99))
picarr = np.asarray(pic)
picarr.flags.writeable = True


picarr[50][50] = 255
print picarr


plt.imshow(picarr)
plt.show()


D1 = fftpack.fft2(picarr)
D2 = fftpack.fftshift(D1)
abs_image = np.abs(D2)
plt.figure()
plt.title("Target")
plt.imshow(abs_image)
plt.show()

