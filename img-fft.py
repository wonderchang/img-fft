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
  print 'Image read:', srcDn + srcFn, 'fft processing ...'
  img = Image.open(srcDn + '/' + srcFn).convert('L') 
  y = np.asarray(img) 

  #FFT process
  Y = np.fft.fft2(y, [512, 512])
  Y = np.fft.fftshift(Y)
  Y = np.log(abs(Y))

  #Get destination filename
  dstFn = srcDn + 'fft-' + srcFn

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
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.tif') or file.endswith('.bmp'):
	  array = file.split('/');
	  if len(array) == 1:
	    file = './' + file
	    array = array = file.split('/')
	  fn = array[len(array) - 1]
	  array = file.split(fn)
	  dn = array[0];
	  imgFFT(dn, fn) 
      elif os.path.isdir(file):
	fnList = getImgList(file)
	if not file.endswith('/'):
	  file = file + '/'
	print file
	for fn in fnList:
	  imgFFT(file, fn)



