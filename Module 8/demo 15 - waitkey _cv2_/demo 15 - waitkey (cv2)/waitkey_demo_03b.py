# waitkey_demo_03b.py

import cv2

img = cv2.imread('image_01.png')

cv2.imshow('image', img)

print('Select the image window, then press a key on the keyboard')
print('Press q key to quit')

i = 0

while True:

	key = cv2.waitKey(10)				# Try 100, 1000, 5000, what happens?
	# Wait up to 1 millisecond for a key to be pressed
	# If no key is pressed in 1 millisecond, then -1 is returned

	if key != -1:
		print('You pressed key', key)
	# else:									# Try uncommenting this part. What happens?
	# 	print('You did not press a key')

	if key == ord('q'):
		break

	i = i + 1
	print(i)

print('Good bye')

cv2.destroyAllWindows()
