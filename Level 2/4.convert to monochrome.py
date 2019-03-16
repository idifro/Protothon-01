import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('image.png')
arr = 0.2126* img[...,0] + 0.7152* img[...,1] + 0.0722 * img[...,2]
plt.imshow(arr, cmap=plt.get_cmap('gray'))
plt.show()  
