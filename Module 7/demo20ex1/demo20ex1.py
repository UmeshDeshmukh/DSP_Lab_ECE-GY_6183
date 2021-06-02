import pyaudio, struct, math
import numpy as np
from myfunctions import clip16 

# y(n) = x(n) + K/2 y(n-N) + K/2 y(n-N-1)
N = 60
K = 0.93
# a = [1 zeros(1, N-1) -K/2 -K/2];
# b = 1;

Fs = 8000
CHANNELS = 1
WIDTH = 2
T = 1.1
gain = 1000
# BLOCKLEN = 512
# output_block = BLOCKLEN*[0]
# theta = 0

BUFFER_LEN =  5000          # Set buffer length.  Must be more than N!
buffer = BUFFER_LEN * [0]
kr = 1  
kw = N+1  

p = pyaudio.PyAudio()
stream = p.open(format = p.get_format_from_width(WIDTH),
                rate = Fs,
                channels = CHANNELS,
                input = False,
                output = True
                )
                
np.random.seed(10)
#rand_array = np.random.rand(N)
rand_array = np.random.randint(5, size=(N))

# zero_array = np.zeros(np.round(T*Fs))
zero_array = np.zeros(int(T*Fs))
#x0 = np.array(int(np.random.rand(N)), int(np.zeros(1,np.round(T*Fs)))) 
x0 = np.hstack((rand_array,zero_array))
#print('x0=',x0)
LEN = len(x0)
sigLen = LEN*WIDTH

#while(sigLen>0):
 
 
for n in range(0,LEN):
 #buffer[kw] = int(x0[n]*1 + buffer[kr-N]*(K/2) + buffer[kr-(N+1)]*(K/2)) 
 y0 = int(x0[n]*1 + buffer[kr]*(K/2) + buffer[kr-1]*(K/2))
 #print(buffer[kw])
 buffer[kw]= y0
 y1 = gain*y0
 binary_data = struct.pack('h',clip16(y1))   # 'h' for 16 bits
 stream.write(binary_data)
 #print(y0)
 kr = kr + 1
 if kr == BUFFER_LEN:
  # End of buffer. Circle back to front.
  kr = 1
 
   # Increment write index    
 kw = kw + 1
 if kw == BUFFER_LEN:
  # End of buffer. Circle back to front.
  kw = 0  
 

stream.stop_stream()
stream.close()
p.terminate()
