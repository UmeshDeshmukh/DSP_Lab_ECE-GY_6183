# blur_video.py
# Demonstrates 2D spatial filtering

import numpy as np 
import cv2

# cap = cv2.VideoCapture(0)

print("Switch to video window. Then press 'p' to save image, 'q' to quit")
matrix_1 = np.ones((3, 3))
matrix_1[1,1] = 1
kernel = matrix_1 - np.ones((3, 3))/9
#kernel = np.ones((9, 9))/81

#kernel = np.ones((31, 31))/(31 * 31)

#kernel = np.ones((9,9), np.float32)/81    # alternately, explicitly specify the data type
img = cv2.imread('tiger.jpg', 1);


#[ok, frame] = cap.read()          # Read one frame

# print(type(frame))

img2 = cv2.filter2D(img, -1, kernel)
# -1 means the output will have the same data type as input frame

# Alternately, use cv2.GaussianBlur()
# Arguments: frame, kernal size, spread in X and Y directions.
#frame = cv2.GaussianBlur(frame, (9, 9), sigmaX = 10, sigmaY = 10)

cv2.imshow('Live video', img2)

key = cv2.waitKey(10000)
# key = key & 0xFF      # (May not be necessary)

# if key == ord('p'):
    # cv2.imwrite('blurred.jpg', frame)              
    
# if key == ord('q'):
    # break

#cap.release()
cv2.destroyAllWindows()
