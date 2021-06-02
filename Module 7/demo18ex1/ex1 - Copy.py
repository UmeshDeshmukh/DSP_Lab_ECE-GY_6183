# keyboard_demo_06.py
# Play a note using a second-order difference equation
# when the user presses a key on the keyboard.

import pyaudio, struct
import numpy as np
from scipy import signal
from math import sin, cos, pi
import tkinter as Tk    

BLOCKLEN   = 64        # Number of frames per block
WIDTH       = 2         # Bytes per sample
CHANNELS    = 1         # Mono
RATE        = 8000      # Frames per second

MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

# Parameters
Ta = 2      # Decay time (seconds)
# f1 = 250    # Frequency (Hz)
f1 = 440
k = 0
# Pole radius and angle
r = 0.01**(1.0/(Ta*RATE))       # 0.01 for 1 percent amplitude
om1 = 2.0 * pi * float(f1)/RATE



# Filter coefficients (second-order IIR)
a = [1, -2*r*cos(om1), r**2]
b = [r*sin(om1)]
ORDER = 2   # filter order
states = np.zeros(ORDER)
states_l = np.zeros(ORDER)
x = np.zeros(BLOCKLEN)
y = np.zeros(BLOCKLEN)
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

CONTINUE = True
KEYPRESS = False

def my_function(event):
    global CONTINUE
    global KEYPRESS
    global k, y
    global states_l
    print('You pressed ' + event.char)
    if event.char == 'q':
      print('Good bye')
      CONTINUE = False
      
    #update_frequency(event)
    
    x[0] = 10000.0
    
    if event.char == 'i':
     k = k + 1
     print('k=',k)
    elif event.char == 'd':
     k = k - 1
     print('k=',k)
    f1_l = (2**(k/12))*f1
    print('f',f1_l)
    om1_l = 2.0 * pi * float(f1_l)/RATE
    a_l = [1, -2*r*cos(om1_l), r**2]
    b_l = [r*sin(om1_l)]    
    [y_l, states_l] = signal.lfilter(b_l, a_l, x, zi = states_l)    
    y = y + y_l
    x[0] = 0.0
    KEYPRESS = False
    
# def update_frequency(event):
    # global k
    # if event.char == 'i':
     # k = k + 1
    # elif event.char == 'd':
     # k = k - 1
    # f1_l = (2**(k/12))*f1
    # r_l = 0.01**(1.0/(Ta*RATE))       
    # om1_l = 2.0 * pi * float(f1)/RATE
    # a_l = [1, -2*r*cos(om1), r**2]
    # b_l = [r*sin(om1)]    
    # [y_l, states_l] = signal.lfilter(b_l, a_l, x, zi = states_l)
    
    
root = Tk.Tk()
root.bind("<Key>", my_function)

print('Press keys for sound.')
print('Press "q" to quit')

while CONTINUE:
    root.update()

    # if KEYPRESS and CONTINUE:
        # Some key (not 'q') was pressed
        #x[0] = 10000.0

    #[y, states] = signal.lfilter(b, a, x, zi = states)
     
    #x[0] = 0.0        
    KEYPRESS = False

    y = np.clip(y.astype(int), -MAXVALUE, MAXVALUE)     # Clipping

    binary_data = struct.pack('h' * BLOCKLEN, *y);    # Convert to binary binary data
    stream.write(binary_data, BLOCKLEN)               # Write binary binary data to audio output

print('* Done.')

# Close audio stream
stream.stop_stream()
stream.close()
p.terminate()
