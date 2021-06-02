# demo_04_diffeq.py
# Play and plot a note (using a second-order difference equation)
# when the user presses a key on the keyboard.
# Uses Tkinter and Pyaudio.

import pyaudio, struct
import numpy as np
from scipy import signal
from math import sin, cos, pi
import tkinter as Tk    
from matplotlib import pyplot

BLOCKLEN   = 512*2        # Number of frames per block
WIDTH       = 2         # Bytes per sample
CHANNELS    = 1         # Mono
RATE        = 8000      # Frames per second

MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

# Parameters
Ta = 0.5    # Decay time (seconds)
f1 = 350    # Frequency (Hz)

# Pole radius and angle
r = 0.01**(1.0/(Ta*RATE))       # 0.01 for 1 percent amplitude
om1 = 2.0 * pi * float(f1)/RATE

# Filter coefficients (second-order IIR)
a = [1, -2*r*cos(om1), r**2]
b = [sin(om1)]
ORDER = 2   # filter order
states = np.zeros(ORDER)
x = np.zeros(BLOCKLEN)

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
    # global KEY
    print('You pressed ' + event.char)
    if event.char == 'q':
      print('Good bye')
      CONTINUE = False
    KEYPRESS = True
    # KEY = event.char

root = Tk.Tk()
root.bind("<Key>", my_function)

L1 = Tk.Label(root, text = 'Press keys')
L1.pack()

print('Press keys for sound.')
print('Press "q" to quit')

t = [1000.*i/RATE for i in range(BLOCKLEN)]

pyplot.ion()           # Turn on interactive mode so plot gets updated
my_fig = pyplot.figure(1)
my_plot = my_fig.add_subplot(1, 1, 1)
[my_line] = my_plot.plot(t, x)
my_plot.set_ylim(-32000, 32000)
my_plot.set_xlim(0, BLOCKLEN*1000.0/RATE)   # Time axis in milliseconds 
my_plot.set_xlabel('Time (milliseconds)')

M = int(BLOCKLEN/2.0)

while CONTINUE:
    root.update()

    if KEYPRESS and CONTINUE:
        # Some key (not 'q') was pressed
        x[M] = 10000.0
        # my_plot.set_title('Key: ' + KEY)

    [y, states] = signal.lfilter(b, a, x, zi = states)

    x[M] = 0.0        
    KEYPRESS = False

    my_line.set_ydata(y)

    y = np.clip(y.astype(int), -MAXVALUE, MAXVALUE)     # Clipping

    binary_data = struct.pack('h' * BLOCKLEN, *y);    # Convert to binary binary_data
    stream.write(binary_data, BLOCKLEN)               # Write binary binary_data to audio output

print('* Done.')

# Close audio stream
stream.stop_stream()
stream.close()
p.terminate()
