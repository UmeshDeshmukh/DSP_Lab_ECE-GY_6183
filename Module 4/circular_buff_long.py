import pyaudio
import struct
from math import cos, pi
import wave

def clip16(x):
 if(x > 32767):
  x = 32767
 elif(x< -32768):
  x = -32768
 else:
  x = x
 return x  

 
wf = wave.open('Recorded_Audio_Clip_16b_PCM.wav','rb')
#wf = wave.open('author.wav','rb')
CHANNELS = wf.getnchannels()
WIDTH = wf.getsampwidth()
Sampling_Rate = wf.getframerate()
LENGTH = wf.getnframes()

delay_sec = 0.05
N = int(Sampling_Rate * delay_sec)
#buffer = buffer_len *[0] 
buffer_len = 10000
buffer = buffer_len *[0] 
w_index = N
r_index = 0
G_Delay = 1.0
b0 = 1.0

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,
                channels = CHANNELS,
                rate = Sampling_Rate,
                input = False,
                output = True)

input_bytes = wf.readframes(1)                

while len(input_bytes)>0:
 x = struct.unpack('h',input_bytes)
 x0 = x[0]
 #compute output values
 y0 = b0 * x0 + G_Delay * buffer[r_index]
 r_index = (r_index + 1)% buffer_len
 buffer[w_index] = x0
 w_index = (w_index + 1)% buffer_len
 ouput_value = int(clip16(y0))

  
 output_bytes = struct.pack('h',ouput_value)
 stream.write(output_bytes)
 input_bytes = wf.readframes(1) 
 
 
# def write_to_buff(data):
 # if(isFull()):
  # print('Buffer is Full.')
  
 # else:
  # w_index = (w_index + 1)% buffer_len
  # buffer[w_index] = data   
  


# def read_from_buff():
 # if(isEmpty()):
  # print('Buffer is Empty.')
 # else:
  # data = buffer[r_index] 
  

# def isFull():

# def isEmpty():
   
 
 
 

 
  
 





 
 
 
  