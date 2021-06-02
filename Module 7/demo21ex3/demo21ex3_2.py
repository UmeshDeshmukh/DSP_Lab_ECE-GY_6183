# plot_microphone_input_spectrum.py

"""
Using Pyaudio, get audio input and plot real-time FFT of blocks.
Ivan Selesnick, October 2015
Based on program by Gerald Schuller
"""

import pyaudio
import struct, math
from matplotlib import pyplot as plt
from scipy import signal
import numpy as np

# plt.ion()           # Turn on interactive mode so plot gets updated

WIDTH     = 2         # bytes per sample
CHANNELS  = 1         # mono
RATE      = 8000     # Sampling rate (samples/second)
BLOCKSIZE = 1024      # length of block (samples)
DURATION  = 15        # Duration (seconds)

f1 = 400

theta = 0
output_block = BLOCKSIZE * [0]

NumBlocks = int( DURATION * RATE / BLOCKSIZE )

print('BLOCKSIZE =', BLOCKSIZE)
print('NumBlocks =', NumBlocks)
print('Running for ', DURATION, 'seconds...')



# Open audio device:
p = pyaudio.PyAudio()
PA_FORMAT = p.get_format_from_width(WIDTH)

stream = p.open(
    format    = PA_FORMAT,
    channels  = CHANNELS,
    rate      = RATE,
    input     = True,
    output    = True)

b = [0.0423 + 0.0000i 0.0000 + 0.1193i -0.2395 + 0.0000i 0.0000 - 0.3208i 0.3208 + 0.0000i 0.0000 + 0.2395i -0.1193 + 0.0000i 0.0000 - 0.0423i];
a = [1.0000 + 0.0000i 0.0000 - 1.2762i -2.6471 + 0.0000i 0.0000 + 2.2785i 2.1026 + 0.0000i 0.0000 - 1.1252i -0.4876 + 0.0000i 0.0000 + 0.1136i]; 
  
b0 = complex(0.0423 ,0.0000) 
b1 = complex(0.0000 ,0.1193)
b2 = complex(-0.2395, 0.0000)
b3 = complex(0.0000 ,0.3208)
b4 = complex(0.3208 ,0.0000)
b5 = complex(0.0000 ,0.2395)
b6 = complex(-0.1193, 0.0000)
b7 = complex(0.0000 ,0.0423)
a0 = complex(1.0000 ,0.0000)
a1 = complex(0.0000 ,1.2762)
a2 = complex(-2.6471, 0.0000)
a3 = complex(0.0000 ,2.2785)
a4 = complex(2.1026 ,0.0000)
a5 = complex(0.0000 ,1.1252)
a6 = complex(-0.4876, 0.0000)
a7 = complex(0.0000 ,0.1136)
i  = complex(0.0000, 1.0000)
out = complex(0,0)
theta = 0

ORDER = 7   # filter is fourth order
states = np.zeros(ORDER)
MAXVALUE = 2**15-1
for n in range(0, NumBlocks):
 input_bytes = stream.read(BLOCKSIZE)                     # Read audio input stream
 input_tuple = struct.unpack('h' * BLOCKSIZE, input_bytes)  # Convert

 om1 = 2.0 * math.pi * f1 / RATE
 #for n in range(0,BLOCKSIZE):
  # out = ((input_tuple[n]*b0 + input_tuple[n-1]*b1 + input_tuple[n-2]*b2
  # + input_tuple[n-3]*b3 + input_tuple[n-4]*b4 + input_tuple[n-5]*b5 + input_tuple[n-6]*b6
  # + input_tuple[n-7]*b7)- (output_block[n]*a0 + output_block[n-1]*a1 + output_block[n-2]*a2
  # + output_block[n-3]*a3 + output_block[n-4]*a4 + output_block[n-5]*a5 + output_block[n-6]*a6
  # + output_block[n-7]*a7))* math.exp(i*theta)
 [output_block, states] = scipy.signal.lfilter(b, a, input_tuple, zi = states)
 output_block = np.clip(output_block, -MAXVALUE, MAXVALUE)
 output_block = np.real(output_block)
 output_block = output_block* math.exp(i*theta)
 theta = theta + om1
 while theta > math.pi:
  theta = theta - 2.0 * math.pi
   
 output_bytes = struct.pack('h' * BLOCKSIZE, *output_block)    
 stream.write(output_bytes)    


stream.stop_stream()
stream.close()
p.terminate()

print('* Finished')
