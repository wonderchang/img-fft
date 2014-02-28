import numpy as np
import pylab as plt
import Image

#Read image
name = 'img/pic.jpg'
img = Image.open(name).convert('L')
y = np.asarray(img)
#print 'y max =', y.max()
#print 'y min =', y.min()
img_width = y.shape[0]
img_height = y.shape[1]

if img_width == img_height:
  size = img_width
elif img_width > img_height:
  size = img_width
else:
  size = img_height

#FFT process
Y = np.fft.fft2(y, [size, size])
Y = np.fft.fftshift(Y)
Y = np.log(abs(Y))
#print 'Y max =', Y.max()
#print 'Y min =', Y.min()

#plt.figure(1)
#plt.imshow(y).set_clim(0.0, 255.0)
plt.figure(2)
plt.imshow(Y)
plt.savefig('output.png', dpi=96)
#plt.show()

  
