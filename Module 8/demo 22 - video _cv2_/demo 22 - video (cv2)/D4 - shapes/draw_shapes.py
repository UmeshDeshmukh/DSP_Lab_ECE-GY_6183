# draw_shapes.py

import cv2

img = cv2.imread('cat.jpg', 1)

cv2.line(img, (101, 555), (555, 101), (25, 255, 0), 25)         
# Draw a diagonal blue line with thickness of 5 pixels,
# and the end points being passed as arguments

cv2.rectangle(img, (384, 0), (510, 128), (12, 255,2), 13)  
# Draw a green rectangle with the the two diaganoal points being passed as argument

cv2.circle(img, (255, 255), 63, (10, 255, 255), 5)
# Draw a red circle centred at (255, 255) and a radius of 63 units.
# Negative thickness indicates that the circle is filled

cv2.imshow('Shapes on image', img)

print('Switch to image view. Then press any key to close')

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('cat_shapes.jpg', img)
cv2.imwrite('cat_shapes.png', img)

# Reference - https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html
# This shows how to draw lines, rectanges, and circles
# The function can draw these shapes on images or on an empty background

