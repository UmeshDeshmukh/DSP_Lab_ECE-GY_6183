# echo_via_circular_buffer.py
# Reads a specified wave file (mono) and plays it with an echo.
# This implementation uses a circular buffer.

import pyaudio
import wave
import struct
from myfunctions import clip16



wavfile = 'demo8ex6.wav'
# Open the wave file
wf = wave.open( wavfile, 'wb')
RATE = 16000
# Read the wave file properties
wf.setframerate(RATE)     # Sampling rate (frames/second)
wf.setnchannels(1)     # Number of channels
wf.setsampwidth(2)     # Number of bytes per sample

# Set parameters of delay system
b0 = 1.0            # direct-path gain
G = 0.8             # feed-forward gain
delay_sec = 0.05    # delay in seconds, 50 milliseconds   Try delay_sec = 0.02
duration_sec = 2
N = int( RATE * delay_sec )   # delay in samples
M = int(RATE * duration_sec)
print('The delay of %.3f seconds is %d samples.' %  (delay_sec, N))

# Buffer to store past signal values. Initialize to zero.
BUFFER_LEN = N              # length of buffer
buffer = BUFFER_LEN * [0]   # list of zeros

# Open an output audio stream
p = pyaudio.PyAudio()
stream = p.open(format      = pyaudio.paInt16,
                channels    = 1,
                rate        = RATE,
                input       = True,
                output      = False )

# Get first frame
input_bytes = stream.read(1)
# Initialize buffer index (circular index)
k = 0

print('* Start')

for n in range(0, M):

    # Convert binary data to number
    x0, = struct.unpack('h', input_bytes)

    # Compute output value
    # y(n) = b0 x(n) + G x(n-N)
    y0 = b0 * x0 + G * buffer[k]

    # Update buffer
    buffer[k] = x0

    # Increment buffer index
    k = k + 1
    if k >= BUFFER_LEN:
        # The index has reached the end of the buffer. Circle the index back to the front.
        k = 0

    # Clip and convert output value to binary data
    output_bytes = struct.pack('h', int(clip16(y0)))

    # Write output value to audio stream
    wf.writeframesraw(output_bytes)

    # Get next frame
    input_bytes = stream.read(1)     

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
wf.close()