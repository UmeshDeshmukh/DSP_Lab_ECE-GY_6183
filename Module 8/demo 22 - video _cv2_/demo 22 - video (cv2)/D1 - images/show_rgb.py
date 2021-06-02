# show_rgb.py
# Show the three components of the RGB representation of a color image.
# The colors are ordered Blue, Green, Red.
# Each color channel is bright where that color is present in the image

import cv2

img = cv2.imread('books.jpg', 1)   
# 1 means import image in color

print(type(img))
print(img.shape)	# number of rows and columns
print(img.dtype)	# data type

cv2.imshow('Original image', img)
cv2.imshow('Channel 0 (Blue)',  img[:, :, 0])
cv2.imshow('Channel 1 (Green)', img[:, :, 1])
cv2.imshow('Channel 2 (Red)',   img[:, :, 2])

print('Switch to images. Then press any key to quit')

# Write the image to a file
cv2.imwrite('books - blue channel.jpg',  img[:, :, 0])
cv2.imwrite('books - green channel.jpg', img[:, :, 1])
cv2.imwrite('books - red channel.jpg',   img[:, :, 2])

cv2.waitKey(0)   # wait until any keystroke
cv2.destroyAllWindows()
