import numpy as np
import pylab as plt
import Image
import scipy
import os
import sys 
import glob


def getImgList(dn): 
  fnList = []
  for file in os.listdir(dn): 
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.tif') or file.endswith('.bmp'): 
      fnList.append(file)
  return fnList

def imgFFT(srcDn, srcFn):
  #Read image
  print 'Image read:', srcDn + '/' + srcFn, 'fft processing ...'
  img = Image.open(srcDn + '/' + srcFn).convert('L') 
  y = np.asarray(img) 

  #Find the max side length
  size = y.shape[0] if y.shape[0] >= y.shape[1] else y.shape[1]

  #FFT process
  Y = np.fft.fft2(y, [512, 512])
  Y = np.fft.fftshift(Y)
  Y = np.log(abs(Y))

  #Get destination filename
  dstFn = srcDn + '/fft-' + srcFn

  #Save figure
  plt.imshow(Y).set_clim(0.0, 16.0)
  plt.savefig(dstFn, dpi=96)
  print dstFn, 'output.'



if len(sys.argv) < 2:
  print 'Usage: python img-fft.py [(filename|directory)+]'
else:
  src = sys.argv[1:] 
  for file in src:
    if os.path.exists(file): 
      if os.path.isfile(file): 
	imgFFT('.', file) 
      elif os.path.isdir(file):
	fnList = getImgList(file)
	for fn in fnList:
	  imgFFT(file, fn)



