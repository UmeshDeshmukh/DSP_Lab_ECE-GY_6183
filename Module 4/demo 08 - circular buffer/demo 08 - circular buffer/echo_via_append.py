# echo_via_append.py
# Reads a specified wave file (mono) and plays it with an echo.
# This implementation appends and removes values of a list. 

import pyaudio
import wave
import struct
from myfunctions import clip16

wavfile = 'author.wav'
print('Play the wave file %s.' % wavfile)

# Open the wave file
wf = wave.open( wavfile, 'rb')

# Read the wave file properties
num_channels    = wf.getnchannels()     # Number of channels
RATE            = wf.getframerate()     # Sampling rate (frames/second)
signal_length   = wf.getnframes()       # Signal length
width           = wf.getsampwidth()     # Number of bytes per sample

print('The file has %d channel(s).'            % num_channels)
print('The frame rate is %d frames/second.'    % RATE)
print('The file has %d frames.'                % signal_length)
print('There are %d bytes per sample.'         % width)

# Set parameters of delay system
b0 = 1.0    # Gain for direct path
G = 0.8
delay_sec = 0.05 # 50 milliseconds
N = int( RATE * delay_sec )   # delay in samples

print('The delay of %.3f seconds is %d samples.' %  (delay_sec, N))

# Create a buffer to store past values. Initialize to zero.
BUFFER_LEN = N              # length of buffer
buffer = BUFFER_LEN * [0]   # list of zeros

# Open an output audio stream
p = pyaudio.PyAudio()
stream = p.open(format      = pyaudio.paInt16,
                channels    = 1,
                rate        = RATE,
                input       = False,
                output      = True )

# Get first frame (sample)
input_bytes = wf.readframes(1)

print('* Start')

while len(input_bytes) > 0:

    # Convert binary data to number
    x0, = struct.unpack('h', input_bytes)

    # Compute output value
    # y(n) = b0 x(n) + G x(n-N)
    y0 = b0 * x0 + G * buffer[0]

    # Update buffer
    buffer.append(x0)
    del buffer[0]       # remove first value

    # Convert output value to binary data
    output_bytes = struct.pack('h', int(clip16(y0)))

    # Write output value to audio stream
    stream.write(output_bytes)

    # Get next frame (sample)
    input_bytes = wf.readframes(1)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
wf.close()
