# video_capture_2.py
# Capture video and display it on the screen in real-time
# Reduce size of frame 

import cv2

cap = cv2.VideoCapture(0)
# Initialize video capture. 0 means default web camera

print("Switch to video window. Then press 'q' to quit")

while cap.isOpened():

    [ok, frame] = cap.read()   # Read one video frame (ok is true if it works)

    # frame = cv2.flip(frame, 1)						# Horizontal flip
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # convert to grayscale

    frame = cv2.resize(frame, None, fx = 0.25, fy = 0.25)

    cv2.imshow('Live video', frame)                

    key = cv2.waitKey(1)
    # key = key & 0xFF    	# (Might not be necessary)
    if key == ord('q'):     
        break				# Stop when 'q' key is pressed

cap.release()
cv2.destroyAllWindows()

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html#display-video
