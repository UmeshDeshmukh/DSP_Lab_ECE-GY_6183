# play_randomly_plots.py
"""
Generate random pulses with a recursive filter of 2nd order.
It sounds like pings from a Sonar or from a Geiger Counter.
Gerald Schuller, March 2015 
"""

import pyaudio, struct
import random
from math import sin, cos, pi
from myfunctions import clip16
from matplotlib import pyplot as plt

BLOCKLEN = 1024    # Number of frames per block
WIDTH = 2          # Bytes per sample
CHANNELS = 1       # Number of channels
RATE = 8000        # Sampling rate in Hz (samples/second)

# Parameters
T = 10       # Total play time (seconds)
Ta = 0.5    # Decay time (seconds)
f1 = 350    # Frequency (Hz)

NumBlocks = int( T * RATE / BLOCKLEN )

# Make second-order recursive filter

# Pole radius and angle
om1 = 2.0 * pi * float(f1) / RATE
r = 0.01 ** ( 1.0 / (Ta * RATE))    # 0.01 for 1 percent amplitude

# Filter coefficients
a1 = -2*r*cos(om1)
a2 = r**2
b0 = sin(om1)

y = BLOCKLEN * [0]

plt.ion()           # Turn on interactive mode so plot gets updated
fig = plt.figure(1)
[line] = plt.plot(y)
plt.ylim(-32000, 32000)
plt.xlim(0, BLOCKLEN)
plt.xlabel('Time (n)')
# plt.show()

# Open the audio output stream
p = pyaudio.PyAudio()
PA_FORMAT = p.get_format_from_width(WIDTH)
stream = p.open(format = PA_FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = False,
                output = True,
                frames_per_buffer = 256)

print('Playing for %f seconds ...' % T)

THRESHOLD = 2.5 / RATE          # For a rate of 2.5 impulses per second

# Loop through blocks
for i in range(NumBlocks):

    # Do difference equation for block
    for n in range(BLOCKLEN):

        rand_val = random.random()
        if rand_val < THRESHOLD:
            x = 15000
        else:
            x = 0

        y[n] = b0 * x - a1 * y[n-1] - a2 * y[n-2]  
        # What happens when n = 0?
        # In Python negative indices cycle to end, so this works!

        y[n] = int(clip16(y[n]))

    line.set_ydata(y)
    plt.title('Block %d' % i)
    plt.pause(0.0001)

    # Convert numeric list to binary data
    output_bytes = struct.pack('h' * BLOCKLEN, *y);

    # Write binary data to audio output stream
    stream.write(output_bytes, BLOCKLEN)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
