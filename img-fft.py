import numpy as np
import pylab as plt
import Image
import os


def getImgList(dn): 
  fnList = []
  for file in os.listdir(dn): 
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.tif') or file.endswith('.bmp'): 
      fnList.append(file)
  return fnList

def imgFFT(srcFn):

  #Read image 
  img = Image.open(srcFn).convert('L') 
  y = np.asarray(img) 

  #Find the max side length
  size = y.shape[0] if y.shape[0] >= y.shape[1] else y.shape[1]

  #FFT process
  Y = np.fft.fft2(y, [size, size])
  Y = np.fft.fftshift(Y)
  Y = np.log(abs(Y))

  #Get destination filename
  dstFn = 'fft-' + srcFn

  #Save figure
  plt.imshow(Y)
  plt.savefig(dstFn, dpi=96)

dn = 'img'
fnList = getImgList(dn)

for fn in fnList:
  tmp = dn + '/' + fn
  imgFFT(tmp)
