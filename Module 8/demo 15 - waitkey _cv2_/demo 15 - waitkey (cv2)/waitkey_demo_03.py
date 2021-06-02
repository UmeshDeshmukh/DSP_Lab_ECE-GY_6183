# waitkey_demo_03.py

import cv2

img = cv2.imread('image_01.png')

cv2.imshow('image', img)

print('Select the image window, then press a key on the keyboard')
print('Press q key to quit')

while True:

	key = cv2.waitKey(1)
	# Wait up to 1 millisecond for a key to be pressed
	# If no key is pressed in 1 millisecond, then -1 is returned

	if key != -1:
		print('You pressed key', key)
	# else:									# Try uncommenting this part. What happens? Why?
	# 	print('You did not press a key')

	if key == ord('q'):
		break

print('Good bye')

cv2.destroyAllWindows()
