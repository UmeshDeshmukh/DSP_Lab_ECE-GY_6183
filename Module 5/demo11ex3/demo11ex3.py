# plot_microphone_input.py
from myfunctions import clip16
import pyaudio
import struct
from matplotlib import pyplot

WIDTH = 2           # bytes per sample
CHANNELS = 1        # mono
RATE = 8000         # frames per second
BLOCKLEN = 1024     # block length in samples
DURATION = 5       # Duration in seconds

K = int( DURATION * RATE / BLOCKLEN )   # Number of blocks

print('Block length: %d' % BLOCKLEN)
print('Number of blocks to read: %d' % K)
print('Duration of block in milliseconds: %.1f' % (1000.0 * BLOCKLEN/RATE))

# Set up plotting...

pyplot.ion()           # Turn on interactive mode
pyplot.figure(1)
[g1] = pyplot.plot([], [], 'blue')  # Create empty line

n = range(0, BLOCKLEN)
pyplot.xlim(0, BLOCKLEN)         # set x-axis limits
pyplot.xlabel('Time (n)')
g1.set_xdata(n)                   # x-data of plot (discrete-time)

# --- Time axis in units of milliseconds ---
# t = [n*1000/float(RATE) for n in range(BLOCKLEN)]
# pyplot.xlim(0, 1000.0 * BLOCKLEN/RATE)         # set x-axis limits
# pyplot.xlabel('Time (msec)')
# g1.set_xdata(t)                   # x-data of plot (time)

pyplot.ylim(-10000, 10000)        # set y-axis limits

# Open the audio stream

p = pyaudio.PyAudio()
PA_FORMAT = p.get_format_from_width(WIDTH)
stream = p.open(
    format = PA_FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True)

# Read microphone, plot audio signal
# y0 = 0.0
# y1 = 0.0 
# y2 = 0.0
# y3 = 0.0
# x0 = 0.0
# x1 = 0.0 
# x2 = 0.0
# x3 = 0.0

# Difference equation coefficients
b0 =  0.008442692929081
b2 = -0.016885385858161
b4 =  0.008442692929081

# a0 =  1.000000000000000
a1 = -3.580673542760982
a2 =  4.942669993770672
a3 = -3.114402101627517
a4 =  0.757546944478829

w1 = 0.0
w2 = 0.0
w3 = 0.0
w4 = 0.0

y = [0]* BLOCKLEN

for i in range(K):

    # Read audio input stream
    input_bytes = stream.read(BLOCKLEN)

    # In case of run-time errors, try using instead:
    # input_bytes = stream.read(BLOCKLEN, exception_on_overflow = False)
    signal_block = struct.unpack('h' * BLOCKLEN, input_bytes)  # Convert
    x = signal_block[0]
    #y0 = x0*0.0084 + x1*0 + x2*(-0.0169) + x3*(0) + x4*(0.0084) 
    for n in range(0, BLOCKLEN):
      
     w0 = x - (a1*w1 + a2*w2 + a3*w3 + a4*w4)
     y[n] = b0*w0 + b2*w2 + b4*w4
     
     w4 = w3
     w3 = w2
     w2 = w1
     w1 = w0
     
     y[n] = int(clip16(y[n]))
    
    output_bytes = struct.pack('h'*BLOCKLEN, *y)
    g1.set_ydata(signal_block)   # Update y-data of plot
    stream.write(output_bytes,BLOCKLEN)
    pyplot.pause(0.0001)

stream.stop_stream()
stream.close()
p.terminate()

pyplot.ioff()           # Turn off interactive mode
pyplot.show()           # Keep plot showing at end of program

pyplot.close()
print('* Finished')
