import numpy
import cv2

n = numpy.arange(27)
# print(n)

# Creating two dimension from numpy list
# print(n.reshape(3, 9))

# Reading in grayscale instead of BGR
im_g = cv2.imread("smallgray.png", 0)
print(im_g)
print(im_g.shape)

# Write new image based on first one
cv2.imwrite("newsmallgray.png", im_g)
print(im_g[0:2, 2:4])

# Iterating through each index
print([each_index for each_index in im_g.flat])

# Concatenating arrays horizontally
ims = numpy.hstack((im_g, im_g, im_g))
print(ims)

# Concatenating arrays vertically
ims = numpy.vstack((im_g, im_g, im_g))
print(ims)