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

def imgFFT(srcDn, srcFn, optionMode):

  #Read image
  print 'Image read:', srcDn + srcFn, 'fft processing ...'
  img = Image.open(srcDn + '/' + srcFn).convert('L') 
  y = np.asarray(img) 

  #FFT process
  Y = np.fft.fft2(y, [512, 512])
  Y = np.fft.fftshift(Y)
  Y = np.log(abs(Y))

  #Make the output filename
  figureFn = srcDn + 'fft-' + srcFn
  array = srcFn.split('.')
  dataFn = ''
  for name in array[:len(array) - 1]:
    dataFn += name
  dataFn = srcDn + 'fft-data-' + dataFn + '.matrix'
  
  #Save Output
  plt.imshow(Y).set_clim(0.0, 16.0)
  if optionMode == 'both' or option == 'figure': 
    plt.savefig(figureFn, dpi=96) 
    print figureFn, 'output.'
  if optionMode == 'both' or option == 'data': 
    np.savetxt(dataFn, Y, fmt='%.3f', delimiter=',')
    print dataFn, 'output.'

if len(sys.argv) < 2:
  print 'Usage: python img-fft.py [option] [(filename|directory)+]\n'
  print 'Options:'
  print '  -f, --figure\tOnly output the FFT figure file'
  print '  -d, --data\tOnly output the FFT data file'
  print ''
  print 'The document and the source can be download at https://github.com/wonderchang/img-fft'
else:
  if sys.argv[1].startswith('-'): 
    if sys.argv[1].startswith('--'):
      if sys.argv[1].endswith('figure'):
	option = 'figure'
      elif sys.argv[1].endswith('data'):
	option = 'data'
      else:
	print 'Error: Unexpected option argument in command line.'
	sys.exit()
      src = sys.argv[2:] 
    else:
      if sys.argv[1].endswith('f'):
	option = 'figure'
      elif sys.argv[1].endswith('d'):
	option = 'data'
      else:
	print 'Error: Unexpected option argument in command line.'
	sys.exit()
      src = sys.argv[2:] 
  else:
    src = sys.argv[1:] 
    option = 'both'

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
	  imgFFT(dn, fn, option) 

      elif os.path.isdir(path):

	#Complete the file
	if path.endswith('/'):
	  dn = path
	else: 
	  dn = path + '/'

	#Get the file list in the directory
	for fn in os.listdir(path): 
	  if getFileExtension(fn):
	    imgFFT(dn, fn, option)

