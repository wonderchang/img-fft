import numpy as np
import pylab as plt
import Image
import scipy
import os
import sys 
import glob

def getFileExtension(fn):
  if fn.endswith('.png') or fn.endswith('.jpg') or fn.endswith('.jpeg') or fn.endswith('.tif') or fn.endswith('.bmp'): 
    return True
  else: 
    return False

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
  for path in src:

    #Check the file exist or not
    if os.path.exists(path): 

      #Make sure the path is completed
      if not path.startswith('./'):
	path = './' + path

      #Check the file or directory
      if os.path.isfile(path): 

	#Check the file extension
	if getFileExtension(path):

	  #Get the filename and folder
	  array = path.split('/')
	  fn = array[len(array) - 1]
	  dn = ''
	  for subPath in array[0:len(array) - 1]:
	    dn += subPath + '/'

	  #Do the FFT
	  imgFFT(dn, fn) 

      elif os.path.isdir(path):

	#Complete the file
	if path.endswith('/'):
	  dn = path
	else: 
	  dn = path + '/'

	#Get the file list in the directory
	for fn in os.listdir(path): 
	  if getFileExtension(fn):
	    imgFFT(dn, fn)

