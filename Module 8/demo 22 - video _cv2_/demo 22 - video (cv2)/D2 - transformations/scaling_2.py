# scaling_2.py

import cv2

img = cv2.imread('cat.jpg')

scaled_image = cv2.resize(img, None, fx = 0.4, fy = 0.4)

cv2.imshow('Resized image', scaled_image)
cv2.imwrite('cat_scaled_2.jpg', scaled_image)

print('Original image size:', img.shape)
print('After resizing:', scaled_image.shape)

print('Switch to image view. Then press any key to close')

cv2.waitKey(0)
cv2.destroyAllWindows()

