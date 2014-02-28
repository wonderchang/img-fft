from __future__ import division
import math
import Image
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from scipy import misc, fftpack, interpolate
import scipy.ndimage.interpolation

S = 8  # Size of target, and resolution of Fourier space
A = 359  # Number of sinogram exposures

# Construct a simple test target
target = np.zeros((S,S))
target[S / 3 : 2 * S / 3, S / 3 : 2 * S / 3] = 128
#target[8 : 9, 8 : 9] = 255

'''
#fname = 'py-tongue/pic.jpg'
fname = 'problem.png'
image = Image.open(fname).convert("L")
arr = np.asarray(image)
print "max = ", arr.max()
print "min = ", arr.min()
'''

plt.figure()
plt.imshow(target)

D1 = fftpack.fft2(target, [7, 7], axes=(-2, -1))
D2 = fftpack.fftshift(D1)
abs_image = np.abs(D2)
print abs_image
print abs_image.shape

plt.figure()
plt.imshow(abs_image)

D1 = fftpack.fft2(target)
D2 = fftpack.fftshift(D1)
abs_image = np.abs(D2)
print abs_image
print abs_image.shape

plt.figure()
plt.imshow(abs_image)

plt.show()


'''
# Project the sinogram
sinogram=np.array([
  np.sum(
    scipy.ndimage.interpolation.rotate(
      target,a,order=1,reshape=False,mode='constant',cval=0.0
      )
    ,axis=1
    ) for a in xrange(A)
  ])

plt.figure()
plt.title("Sinogram")
plt.imshow(sinogram)

# Fourier transform the rows of the sinogram
sinogram_fft_rows=scipy.fftpack.fftshift(
    scipy.fftpack.fft(sinogram),
    axes=1
    )

plt.figure()
plt.subplot(121)
plt.title("Sinogram rows FFT (real)")
plt.imshow(np.real(np.real(sinogram_fft_rows)),vmin=-50,vmax=50)
plt.subplot(122)
plt.title("Sinogram rows FFT (imag)")
plt.imshow(np.real(np.imag(sinogram_fft_rows)),vmin=-50,vmax=50)

# Coordinates of sinogram FFT-ed rows' samples in 2D FFT space
a=(2.0*math.pi/A)*np.arange(A)
r=np.arange(S)-S/2
r,a=np.meshgrid(r,a)
r=r.flatten()
a=a.flatten()
srcx=(S/2)+r*np.cos(a)
srcy=(S/2)+r*np.sin(a)

# Coordinates of regular grid in 2D FFT space
dstx,dsty=np.meshgrid(np.arange(S),np.arange(S))
dstx=dstx.flatten()
dsty=dsty.flatten()

# Let the central slice theorem work its magic!
# Interpolate the 2D Fourier space grid from the transformed sinogram rows
fft2_real=scipy.interpolate.griddata(
    (srcy,srcx),
    np.real(sinogram_fft_rows).flatten(),
    (dsty,dstx),
    method='cubic',
    fill_value=0.0
    ).reshape((S,S))
fft2_imag=scipy.interpolate.griddata(
    (srcy,srcx),
    np.imag(sinogram_fft_rows).flatten(),
    (dsty,dstx),
    method='cubic',
    fill_value=0.0
    ).reshape((S,S))

plt.figure()
plt.suptitle("FFT2 space")
plt.subplot(221)
plt.title("Recon (real)")
plt.imshow(fft2_real,vmin=-10,vmax=10)
plt.subplot(222)
plt.title("Recon (imag)")
plt.imshow(fft2_imag,vmin=-10,vmax=10)

# Show 2D FFT of target, just for comparison
expected_fft2=scipy.fftpack.fftshift(scipy.fftpack.fft2(target))

plt.subplot(223)
plt.title("Expected (real)")
plt.imshow(np.real(expected_fft2),vmin=-10,vmax=10)
plt.subplot(224)
plt.title("Expected (imag)")
plt.imshow(np.imag(expected_fft2),vmin=-10,vmax=10)

# Transform from 2D Fourier space back to a reconstruction of the target
fft2=scipy.fftpack.ifftshift(fft2_real+1.0j*fft2_imag)
recon=np.real(scipy.fftpack.ifft2(fft2))

plt.figure()
plt.title("Reconstruction")
plt.imshow(recon,vmin=0.0,vmax=1.0)

plt.show()
'''

