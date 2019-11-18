# Python program using NumPy 
# for some basic mathematical 
# operations 

import numpy as np 

# Creating two arrays of rank 2 
x = np.array([[1, 2], [3, 4]]) 
y = np.array([[5, 6], [7, 8]]) 

# Creating two arrays of rank 1 
v = np.array([9, 10]) 
w = np.array([11, 12]) 

# Inner product of vectors 
print(np.dot(v, w), "\n") 

# Matrix and Vector product 
print(np.dot(x, v), "\n") 

# Matrix and matrix product 
print(np.dot(x, y)) 
---------------------------------------------------------------------------------------------------------

# Python script using Scipy 
# for image manipulation 

from scipy.misc import imread, imsave, imresize 

# Read a JPEG image into a numpy array 
img = imread('D:/Programs / cat.jpg') # path of the image 
print(img.dtype, img.shape) 

# Tinting the image 
img_tint = img * [1, 0.45, 0.3] 

# Saving the tinted image 
imsave('D:/Programs / cat_tinted.jpg', img_tint) 

# Resizing the tinted image to be 300 x 300 pixels 
img_tint_resize = imresize(img_tint, (300, 300)) 

# Saving the resized tinted image 
imsave('D:/Programs / cat_tinted_resized.jpg', img_tint_resize
