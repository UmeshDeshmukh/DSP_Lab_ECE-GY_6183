# demo_filter_blocks_corrected.py
# Block filtering of a wave file, save the output to a wave file.
# Corrected version.

import pyaudio, wave, struct, math
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

duration = 10 #in seconds
RATE = 16000
WIDTH = 2
# Difference equation coefficients
b0 =  0.008442692929081
b2 = -0.016885385858161
b4 =  0.008442692929081
b = [b0, 0.0, b2, 0.0, b4]

# a0 =  1.000000000000000
a1 = -3.580673542760982
a2 =  4.942669993770672
a3 = -3.114402101627517
a4 =  0.757546944478829
a = [1.0, a1, a2, a3, a4]

p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = 1,
    rate        = RATE,
    input       = True,
    output      = True )

SigLen = RATE*duration
BLOCKLEN = 64
MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

# Get first set of frame from microphone
binary_data = stream.read(BLOCKLEN, exception_on_overflow = False)

ORDER = 4   # filter is fourth order
states = np.zeros(ORDER)

plt.ion()  
plt.figure(1)
[g0, g1] = plt.plot([],[],[],[])
# plt.legend
g0.set_color('orange')
g0.set_label('Input Signal')
g1.set_color('blue')
g1.set_label('Output Signal')
g0.set_xdata(range(0,BLOCKLEN))
g1.set_xdata(range(0,BLOCKLEN))
while len(binary_data) == WIDTH * BLOCKLEN:

    # convert binary data to numbers
    input_block = struct.unpack('h' * BLOCKLEN, binary_data) 

    # filter
    [output_block, states] = scipy.signal.lfilter(b, a, input_block, zi = states)

    # clipping
    output_block = np.clip(output_block, -MAXVALUE, MAXVALUE)

    # convert to integer
    output_block = output_block.astype(int)

    # Convert output value to binary data
    binary_data = struct.pack('h' * BLOCKLEN, *output_block)

    # Write binary data to audio stream
    stream.write(binary_data)
    g0.set_ydata(input_block)
    g1.set_ydata(output_block)
    # Get next frame from wave file
    binary_data = stream.read(BLOCKLEN)
    plt.pause(0.001)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()

plt.ioff()           # Turn off interactive mode
plt.show()

# Close wavefiles
# wf.close()
# output_wf.close()