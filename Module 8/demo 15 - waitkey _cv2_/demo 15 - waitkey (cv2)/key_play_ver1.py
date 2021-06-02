# key_play_ver1.py

"""
PyAudio Example: Generate random pulses and input them to an IIR filter of 2nd order.
Original version by Gerald Schuller, March 2015 
Modified by Ivan Selesnick, October 2015
"""

import pyaudio, struct
from math import sin, cos, pi
from myfunctions import clip16
import cv2

BLOCKLEN   = 64        # Number of frames per block
WIDTH       = 2         # Bytes per sample
CHANNELS    = 1         # Mono
RATE        = 8000      # Frames per second

# Parameters
Ta = 1      # Decay time (seconds)
f1 = 400    # Frequency (Hz)

# Pole radius and angle
r = 0.01**( 1.0 / ( Ta * RATE ) )       # 0.01 for 1 percent amplitude
om1 = 2.0 * pi * float(f1)/RATE

# Filter coefficients (second-order IIR)
a1 = -2 * r * cos(om1)
a2 = r ** 2
b0 = sin(om1)

# Open the audio output stream
p = pyaudio.PyAudio()
PA_FORMAT = pyaudio.paInt16
stream = p.open(
        format      = PA_FORMAT,
        channels    = CHANNELS,
        rate        = RATE,
        input       = False,
        output      = True,
        frames_per_buffer = 128)
# specify low frames_per_buffer to reduce latency


print('Select the image window, then press keys for sound.')
print('Press "q" to quit')

y = BLOCKLEN * [0]
x = BLOCKLEN * [0]
output = BLOCKLEN * [0]

img = cv2.imread('image_01.png')
cv2.imshow('image', img)

while True:

    key = cv2.waitKey(1)

    if key == -1:
        # No key was pressed
        x[0] = 0.0        
    elif key == ord('q'):
        # User pressed 'q', so quit
        break
    else:
        # Some key (other than 'q') was pressed
        x[0] = 15000.0

    # Run difference equation for block
    for n in range(BLOCKLEN):
        y[n] = b0 * x[n] - a1 * y[n-1] - a2 * y[n-2]  
        # What happens when n = 0?
        # In Python, negative indices cycle to end, which is appropriate here

        output[n] = int(clip16(y[n]))

    # Convert numeric list to binary data
    data = struct.pack('h' * BLOCKLEN, *output);

    # Write binary data to audio output stream
    stream.write(data, BLOCKLEN)

print('* Done *')

# Close audio stream
stream.stop_stream()
stream.close()
p.terminate()
cv2.destroyAllWindows()
