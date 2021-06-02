# plot_wave_file.py

import struct
import wave
from matplotlib import pyplot
import pyaudio

# Specify wave file
#wavfile = 'Recorded_Audio_Clip_16b_PCM.wav'
wavfile = 'author.wav'
print('Name of wave file: %s' % wavfile)

# Open wave file
wf = wave.open( wavfile, 'rb')

# Read wave file properties
RATE        = wf.getframerate()     # Frame rate (frames/second)
WIDTH       = wf.getsampwidth()     # Number of bytes per sample
LEN         = wf.getnframes()       # Signal length
CHANNELS    = wf.getnchannels()     # Number of channels

print('The file has %d channel(s).'         % CHANNELS)
print('The file has %d frames/second.'      % RATE)
print('The file has %d frames.'             % LEN)
print('The file has %d bytes per sample.'   % WIDTH)

p = pyaudio.PyAudio()
stream = p.open(format = p.get_format_from_width(WIDTH),
                channels = CHANNELS,
                input = False,
                output = True,
                rate = RATE,
                frames_per_buffer = 256)
                

BLOCKLEN = 600    # Blocksize

# Set up plotting...

pyplot.ion()           # Turn on interactive mode so plot gets updated

fig = pyplot.figure(1)

[g1] = pyplot.plot([], [])

g1.set_xdata(range(BLOCKLEN))
pyplot.ylim(-32000, 32000)
pyplot.xlim(0, BLOCKLEN)

# Get block of samples from wave file
input_bytes = wf.readframes(BLOCKLEN)

while len(input_bytes) >= BLOCKLEN * WIDTH:

    # Convert binary data to sequence (tuple) of numbers
    signal_block = struct.unpack('h' * BLOCKLEN, input_bytes)

    g1.set_ydata(signal_block)
    pyplot.pause(0.01)
    # pyplot.draw()
    stream.write(input_bytes,BLOCKLEN)
    # Get block of samples from wave file
    input_bytes = wf.readframes(BLOCKLEN)

wf.close()
pyplot.ioff()           # Turn off interactive mode
pyplot.show()			# Keep plot showing at end of program
