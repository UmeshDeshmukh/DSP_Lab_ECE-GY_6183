# AM_blocks.py
# Play a wave file with amplitude modulation. 
# Assumes wave file is mono.
# This implementation reads and plays a block at a time.
# Assignment: modify file so it works for both mono and stereo wave files
#  (where does this file have an error when the wave file is stereo and why? )
# Original by Gerald Schuller, 2013

import pyaudio
import struct
import wave
import math

f0 = 400    # Modulation frequency (Hz)

BLOCKLEN = 64      # Number of frames per block

# Open wave file (mono)
input_wavefile = 'author.wav'
# input_wavefile = 'sin01_mono.wav'
# input_wavefile = 'sin01_stereo.wav'

wf          = wave.open( input_wavefile, 'rb')
RATE        = wf.getframerate()
WIDTH       = wf.getsampwidth()
LEN         = wf.getnframes() 
CHANNELS    = wf.getnchannels() 

print('The sampling rate is %d samples per second' % RATE)
print('Each sample is %d bytes' % WIDTH)
print('The signal is %d samples long' % LEN)
print('The signal has %d channel(s)' % CHANNELS)

# Open audio stream
p = pyaudio.PyAudio()
stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = CHANNELS,
    rate        = RATE,
    input       = False,
    output      = True)

# Create block (initialize to zero)
output_block = BLOCKLEN * [0]

# Number of blocks in wave file
num_blocks = int(math.floor(LEN/BLOCKLEN))

print('* Playing...')

# Loop through wave file 
for i in range(0, num_blocks):

    # Get block of samples from wave file
    input_bytes = wf.readframes(BLOCKLEN)     # BLOCKLEN = number of frames to read

    # Convert binary data to tuple of numbers    
    input_tuple = struct.unpack('h' * BLOCKLEN, input_bytes)
            # (h: two bytes per sample (WIDTH = 2))

    # Go through block
    for n in range(0, BLOCKLEN):
        # Amplitude modulation  (frequency f0)
        output_block[n] = int(input_tuple[n] * math.cos(2*math.pi*n*f0/RATE))
        # output_block[n] = input_tuple[n]  # for no processing

    # Convert values to binary data
    output_bytes = struct.pack('h' * BLOCKLEN, *output_block)

    # Write binary data to audio output stream
    stream.write(output_bytes)

print('* Finished *')

stream.stop_stream()
stream.close()
p.terminate()

# Close wavefiles
wf.close()
# output_wf.close()
