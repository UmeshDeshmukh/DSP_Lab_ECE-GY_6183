# AM_demo.py
# Play a wave file with amplitude modulation. 
# Assumes wave file is mono.
# This implementation reads and plays one frame at a time. 
# Original by Gerald Schuller, 2013

# f0 = 0      # Normal audio
f0 = 400    # Modulation frequency (Hz)

import pyaudio
import struct
import wave
import math

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

print('* Playing...')

# Loop through wave file 
for n in range(0, LEN):

    # Get sample from wave file
    input_bytes = wf.readframes(1)

    # Convert binary data to tuple of numbers
    input_tuple = struct.unpack('h', input_bytes)   # h: 2 bytes per sample

    # Use first value (of two if stereo)
    x = input_tuple[0]

    # Amplitude modulation  (frequency f0)
    # y(n) = x(n) cos( 2 pi f0 n / Fs)
    y = x * math.cos(2.0 * math.pi * f0 * n / RATE)

    # Convert value to binary data
    output_bytes = struct.pack('h', int(y))

    # Write binary data to audio output stream
    stream.write(output_bytes)

print('* Finished *')

stream.stop_stream()
stream.close()
p.terminate()

# Close wavefile
wf.close()
