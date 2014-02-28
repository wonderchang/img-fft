import numpy as np
import pylab as py
from scipy import misc, fftpack
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import Image

fname = 'pic.jpg'
image = Image.open(fname).convert("L")
arr = np.asarray(image)
print arr
plt.imshow(arr, cmap = cm.Greys_r)
plt.show()
