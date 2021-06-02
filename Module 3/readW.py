from math import pi, sin
import wave
import pyaudio
import struct


def clip16bit(x):
 if x > 32767:
  x = 32767;
 elif x < -32768:
  x = -32768;
 else:
  x = x
 return x
 
 
#gain = 0.98
gain = 9.8 
 
wfile = wave.open('Recorded_Audio_Clip_16b_PCM.wav','rb')
n_channels = wfile.getnchannels()
F_s = wfile.getframerate()
sig_len = wfile.getnframes()
width = wfile.getsampwidth()

print('No. of channels->',n_channels)
print('Sampling Rate->',F_s)
print('Signal length->',sig_len)
print('bit width->',width)

p = pyaudio.PyAudio()
stream = p.open( format = pyaudio.paInt16,
                 channels =  n_channels,
                 rate = F_s,
                 input = False,
                 output = True)
                 
                 
input_string = wfile.readframes(1)
  
print(input_string)  
while len(input_string)>0:
 inTuple = struct.unpack('h',input_string)
 #inputString = inTuple[0]
 output_value = clip16bit(int(inTuple[0] * gain))  
 out_string = struct.pack('h',output_value)
 stream.write(out_string) 
 input_string = wfile.readframes(1) 
  
stream.stop_stream()
stream.close()
p.terminate()            
                 
                 
