# plot_wave_file.py

import struct
# import wave
from matplotlib import pyplot
import pyaudio

# Specify wave file
#wavfile = 'Recorded_Audio_Clip_16b_PCM.wav'
# wavfile = 'author.wav'
# print('Name of wave file: %s' % wavfile)

# # Open wave file
# wf = wave.open( wavfile, 'rb')

# # Read wave file properties
# RATE        = wf.getframerate()     # Frame rate (frames/second)
# WIDTH       = wf.getsampwidth()     # Number of bytes per sample
# LEN         = wf.getnframes()       # Signal length
# CHANNELS    = wf.getnchannels()     # Number of channels

# print('The file has %d channel(s).'         % CHANNELS)
# print('The file has %d frames/second.'      % RATE)
# print('The file has %d frames.'             % LEN)
# print('The file has %d bytes per sample.'   % WIDTH)

p = pyaudio.PyAudio()

                
RATE = 16000
BLOCKLEN = 600    # Blocksize
duration = 5 #in seconds
no_samples = duration * RATE
WIDTH = 2
# Set up plotting...

k = int(no_samples/BLOCKLEN)

pyplot.ion()           # Turn on interactive mode so plot gets updated
fig = pyplot.figure(1)
[g1] = pyplot.plot([], [])

g1.set_xdata(range(BLOCKLEN))
pyplot.ylim(-32000, 32000)
pyplot.xlim(0, BLOCKLEN)

# Get block of samples from wave file
# input_bytes = wf.readframes(BLOCKLEN)

stream = p.open(format = p.get_format_from_width(WIDTH),
                channels = 1,
                input = True,
                output = False,
                rate = RATE)
                #frames_per_buffer = 256)

#while len(input_bytes) >= BLOCKLEN * WIDTH:
for i in range(k):
    # Convert binary data to sequence (tuple) of numbers
    input_bytes = stream.read(BLOCKLEN,exception_on_overflow = False)
    signal_block = struct.unpack('h' * BLOCKLEN, input_bytes)

    g1.set_ydata(signal_block)
    pyplot.pause(0.001)
    # pyplot.draw()
    
    #stream.write(input_bytes,BLOCKLEN)
    
    # Get block of samples from wave file
    #input_bytes = wf.readframes(BLOCKLEN)
    
#wf.close()
stream.stop_stream()
stream.close()
p.terminate()
pyplot.ioff()           # Turn off interactive mode
pyplot.show()			# Keep plot showing at end of program
