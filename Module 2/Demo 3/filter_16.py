# 16 bit filter 
# Implement the second order recursive difference equation 
# y(n)= x(n)- a1* y(n-1) - a2* y(n-2)
# 16 bit/sample

from math import cos, pi
import pyaudio
import struct

# Fs: Sampling frequency 
#Fs = 8000
Fs = 16000
#Fs = 24000
#Fs = 32000
#Fs = 5000

# Time period of signal in seconds
T = 1

# No of samples
N = T* Fs

# Difference equation coeffiecients
a1 = -1.9
a2 = 0.998


#Intialization
y1 = 0.0 #y(n-1)
y2 = 0.0 #y(n-2)

#gain = 1000.0
gain = 10000.0
#gain = 1500.0
#gain = 7770.0


#create pyaudio object
p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,   #16 bits/sample
                channels = 1,
                rate = Fs,
                input = False,
                output = True)


for n in range(0, N):
    if n == 0:
     x0 = 1;
    else:
     x0 = 0;
    
    #Difference equation
    y0 = x0 - a1 * y1 - a2 * y2  
    
    #Delays
    y2 = y1
    y1 = y0
    
    out_val = y0 * gain
    out_string = struct.pack('h', int(out_val))
    stream.write(out_string)
    
print('finished')

stream.stop_stream()
stream.close()
p.terminate()    
     