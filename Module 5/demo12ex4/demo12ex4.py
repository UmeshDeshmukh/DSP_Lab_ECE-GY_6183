# play_vibrato_interpolation.py
# Reads a specified wave file (mono) and plays it with a vibrato effect.
# (Sinusoidally time-varying delay)
# Uses linear interpolation

import pyaudio
import wave
import struct
import math
from myfunctions import clip16

wavfile = 'decay_cosine_mono.wav'
wavfile2 = 'demo12ex4.wav'
# wavfile = 'cosine_200_hz.wav'

print('Play the wave file: %s.' % wavfile)

# Open wave file
wf = wave.open( wavfile, 'rb')
wf2 = wave.open( wavfile2, 'wb')
# Read wave file properties
RATE        = wf.getframerate()     # Frame rate (frames/second)
WIDTH       = wf.getsampwidth()     # Number of bytes per sample
LEN         = wf.getnframes()       # Signal length
CHANNELS    = wf.getnchannels()     # Number of channels

wf2.setframerate(RATE)     # Frame rate (frames/second)
wf2.setsampwidth(WIDTH)     # Number of bytes per sample
wf2.setnframes(LEN)       # Signal length
wf2.setnchannels(CHANNELS)     # Number of channels


print('The file has %d channel(s).'         % CHANNELS)
print('The file has %d frames/second.'      % RATE)
print('The file has %d frames.'             % LEN)
print('The file has %d bytes per sample.'   % WIDTH)

# Vibrato parameters
f0 = 3
W = 0.6   # W = 0 for no effect

# f0 = 2; W = 0.2

# OR
# f0 = 2
# ratio = 2.06
# W = (ratio - 1.0) / (2 * math.pi * f0 )
# print(W)



# Buffer (delay line) indices


#print('The buffer is %d samples long.' % BUFFER_LEN)

# Open an output audio stream
p = pyaudio.PyAudio()
stream = p.open(format      = pyaudio.paInt16,
                channels    = 1,
                rate        = RATE,
                input       = False,
                output      = True )

print ('* Playing...')

##########################
BLOCKLEN = 64
N_Blocks = int(math.floor(LEN/BLOCKLEN))
output_block = BLOCKLEN * [0]

kr = 0  # read index
# kw = int(0.5 * BUFFER_LEN)  # write index (initialize to middle of buffer)
kw = int(0.5 * BLOCKLEN)

# Buffer to store past signal values. Initialize to zero.
# BUFFER_LEN =  10000          # Set buffer length.
# buffer = BUFFER_LEN * [0]   # list of zeros
BUFFER_LEN =  BLOCKLEN          # Set buffer length.
buffer = BUFFER_LEN * [0]

##########################
# Loop through wave file 

for i in range(0,N_Blocks):
 input_bytes = wf.readframes(BLOCKLEN)   
 input_tuple = struct.unpack('h'*BLOCKLEN,input_bytes)
 for n in range(0, BLOCKLEN):
        
    # Get sample from wave file
    #input_bytes = wf.readframes(1)

    # Convert string to number
    #x0, = struct.unpack('h', input_bytes)

    # Get previous and next buffer values (since kr is fractional)
    kr_prev = int(math.floor(kr))
    frac = kr - kr_prev    # 0 <= frac < 1
    kr_next = kr_prev + 1
    if kr_next == BLOCKLEN:
        kr_next = 0

    # Compute output value using interpolation
    output_block[n] = int(clip16((1-frac) * buffer[kr_prev] + frac * buffer[kr_next]))

    # Update buffer
    buffer[kw] = input_tuple[n]

    # Increment read index
    kr = kr + 1 + W * math.sin( 2 * math.pi * f0 * n / RATE )
        # Note: kr is fractional (not integer!)

    # Ensure that 0 <= kr < BUFFER_LEN
    if kr >= BLOCKLEN:
        # End of buffer. Circle back to front.
        kr = kr - BLOCKLEN

    # Increment write index    
    kw = kw + 1
    if kw == BLOCKLEN:
        # End of buffer. Circle back to front.
        kw = 0

 # Clip and convert output value to binary data
 output_bytes = struct.pack('h'*BLOCKLEN, *output_block)

 # Write output to audio stream
 stream.write(output_bytes)
 wf2.writeframes(output_bytes)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
wf.close()
wf2.close()