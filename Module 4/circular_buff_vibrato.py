import pyaudio
import struct
import math 
import wave

def clip16(x):
 if(x > 32767):
  x = 32767
 elif(x< -32768):
  x = -32768
 else:
  x = x
 return x  

 
#wf = wave.open('decay_cosine_mono.wav','rb')
wf = wave.open('author.wav','rb')
CHANNELS = wf.getnchannels()
WIDTH = wf.getsampwidth()
Sampling_Rate = wf.getframerate()
LENGTH = wf.getnframes()

delay_sec = 0.05
N = int(Sampling_Rate * delay_sec)
#buffer = buffer_len *[0] 
buffer_len = 10000
buffer = buffer_len *[0] 
w_index = 0
r_index = int(0.5 * buffer_len)
G_Delay = 1.0
b0 = 1.0

# vibrato formula y = x(t - Tau) , Tau = T + W sin(2 pi f0 t)
T = 0.5
W = 0.6
f0 = 2

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,
                channels = CHANNELS,
                rate = Sampling_Rate,
                input = False,
                output = True)

input_bytes = wf.readframes(1)                

for n in range(0,LENGTH):
 x = struct.unpack('h',input_bytes)
 x0 = x[0]
 #compute output values
 #y0 = b0 * x0 + G_Delay * buffer[int(r_index)]
 y0 = buffer[int(r_index)]
 r_index = r_index + 1 + (W * math.sin(2*math.pi*f0*n/Sampling_Rate))
 
 if r_index >= buffer_len:
  r_index = r_index - buffer_len
  
 buffer[w_index] = x0
 w_index = (w_index + 1)% buffer_len
 ouput_value = int(clip16(y0))

  
 output_bytes = struct.pack('h',ouput_value)
 stream.write(output_bytes)
 input_bytes = wf.readframes(1) 
 
 

   
 
 
 

 
  
 





 
 
 
  