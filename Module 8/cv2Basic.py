import cv2
import numpy as np

img = cv2.imread('tiger.jpg',255)
cap = cv2.VideoCapture(0)

cv2.imshow('Waghoba',img)

print(type(img)) # numpy n dimentional array
print(img.shape)
print(np.shape(img))
print(img.size)
print(img.dtype)

scaled_image = cv2.resize(img, None, fx = 0.6, fy = 0.6)
cv2.imshow('Image Scaled',scaled_image)

while cap.isOpened():
 [ok, frame] = cap.read();
 if ok == True:
  
 else:
  break
key = cv2.waitKey(0)
cv2.destroyAllWindows()