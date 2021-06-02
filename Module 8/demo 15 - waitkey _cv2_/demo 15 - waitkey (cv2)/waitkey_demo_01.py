# waitkey_demo_01.py

import cv2

print("ord('a') =", ord('a'))
print("ord('b') =", ord('b'))
print("ord('c') =", ord('c'))

img = cv2.imread('image_01.png')

cv2.imshow('image', img)

print('Select the image window, then press a key on the keyboard')

key = cv2.waitKey(0)    # Wait until a key is pressed

print('You pressed key number', key)

print('Good bye')

cv2.destroyAllWindows()
