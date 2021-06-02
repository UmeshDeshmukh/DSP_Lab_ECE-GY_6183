import wave
from struct import pack
from math import sin, pi

Fs = 8000
Amp = 2**7 - 1.0
F = 443.0
t = int(8000/2)

sine_file = wave.open('sine_8bit.wav','w')
sine_file.setnchannels(1)
sine_file.setsampwidth(1)
sine_file.setframerate(Fs)
for n in range(1,t):
 val = Amp * sin(2 *pi*F/Fs*n)
 byte_array = pack('B',int(val+128))
 sine_file.writeframesraw(byte_array)

sine_file.close()



