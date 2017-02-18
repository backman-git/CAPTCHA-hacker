from digitSet import load_intData
import matplotlib.pyplot as plt

from PIL import Image
import numpy as np

def aryToImg(X):
	return Image.fromarray(X)


(X,Y) = load_intData()


plt.subplot(221)
plt.imshow(aryToImg(X[0]), cmap=plt.get_cmap('gray'))
plt.subplot(222)
plt.imshow(aryToImg(X[1]), cmap=plt.get_cmap('gray'))
plt.subplot(223)
plt.imshow(aryToImg(X[2]), cmap=plt.get_cmap('gray'))
plt.subplot(224)
plt.imshow(aryToImg(X[3]), cmap=plt.get_cmap('gray'))
# show the plot
plt.show()