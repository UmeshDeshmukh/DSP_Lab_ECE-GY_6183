# plot_microphone_input_spectrum.py

"""
Using Pyaudio, get audio input and plot real-time FFT of blocks.
Ivan Selesnick, October 2015
Based on program by Gerald Schuller
"""

import pyaudio
import struct, math
from matplotlib import pyplot as plt
import numpy as np

plt.ion()           # Turn on interactive mode so plot gets updated

WIDTH     = 2         # bytes per sample
CHANNELS  = 1         # mono
RATE      = 8000     # Sampling rate (samples/second)
BLOCKSIZE = 1024      # length of block (samples)
DURATION  = 15        # Duration (seconds)

f0 = 1000
om = 2*math.pi*f0/RATE
theta = 0
output_block = BLOCKSIZE * [0]
output_block_FFT = BLOCKSIZE * [0]
NumBlocks = int( DURATION * RATE / BLOCKSIZE )

print('BLOCKSIZE =', BLOCKSIZE)
print('NumBlocks =', NumBlocks)
print('Running for ', DURATION, 'seconds...')

DBscale = False
# DBscale = True

# Initialize plot window:
fig = plt.figure(1)
fig,axs = plt.subplots(2) 
if DBscale:
    axs[0].set_ylim(0, 150)
    axs[1].set_ylim(0, 150)
else:
    axs[0].set_ylim(0, 20*RATE)
    axs[1].set_ylim(0, 20*RATE)

# Frequency axis (Hz)
axs[0].set_xlim(0, 0.5*RATE)         # set x-axis limits
axs[1].set_xlim(0, 0.5*RATE)         # set x-axis limits
# plt.xlim(0, 2000)         # set x-axis limits
plt.xlabel('Frequency (Hz)')
f = RATE/BLOCKSIZE * np.arange(0, BLOCKSIZE)

line1, = axs[0].plot([],[])
axs[0].set_title('Input Signal')
line2, = axs[1].plot([],[])
axs[1].set_title('AM Output Signal')

line, = plt.plot([], [], color = 'blue')  # Create empty line
line1.set_xdata(f)                         # x-data of plot (frequency)
line2.set_xdata(f)

# line1.set_title('Input Signal')
# line1.set_title('AM Output Signal')

# Open audio device:
p = pyaudio.PyAudio()
PA_FORMAT = p.get_format_from_width(WIDTH)

stream = p.open(
    format    = PA_FORMAT,
    channels  = CHANNELS,
    rate      = RATE,
    input     = True,
    output    = True)


for i in range(0, NumBlocks):
    input_bytes = stream.read(BLOCKSIZE)                     # Read audio input stream
    input_tuple = struct.unpack('h' * BLOCKSIZE, input_bytes)  # Convert
    X = np.fft.fft(input_tuple)
    for n in range(0,BLOCKSIZE):
     output_block[n] = int(input_tuple[n]* 1.0*math.cos(2* math.pi*f0*n/RATE))
     
     # # Update y-data of plot
     # if DBscale:
         # line1.set_ydata(20 * np.log10(np.abs(X)))
         # line2.set_ydata(20 * np.log10(np.abs(output_block)))
     # else:
         # line1.set_ydata(np.abs(X)) 
         # line2.set_ydata(np.abs(output_block))
    output_block_FFT = np.fft.fft(output_block)
    line1.set_ydata(np.abs(X)) 
    line2.set_ydata(np.abs(output_block_FFT))    
    output_bytes = struct.pack('h' * BLOCKSIZE, *output_block)    
    stream.write(output_bytes)    
    plt.pause(0.001)
    # plt.draw()

plt.close()

stream.stop_stream()
stream.close()
p.terminate()

print('* Finished')
