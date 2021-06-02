import matplotlib.pyplot as plt
import wave
import struct
import pyaudio
from math import pi, cos


wf = wave.open('author.wav','rb')
RATE = wf.getframerate()
CHANNELS = wf.getnchannels()
N = wf.getnframes()
WIDTH = wf.getsampwidth()

print('RATE=',RATE)
print('CHANNELS=',CHANNELS)
print('WIDTH=',WIDTH)
# x = [1,3,4,5,6,7,8] 
# y = [23,45,65,75,45,77,99]
# z = [123,345,765,475,445,277,399]

# plt.figure(1)

# plt.title('Plot')
# plt.plot(x,y,'green',label = 'Apple',linestyle = '--')
# plt.plot(x,z,'orange',label = 'Citrus',linestyle = ':')
# plt.xlabel('Time')
# plt.ylabel('Value')
# plt.xlim([32,5])
# plt.ylim([50,100])
# plt.legend()
# plt.grid()
# plt.show()

# x1 = [1,3,4,5,6,7,8] 
# y1 = [3,4.5,60,70,50,7,9]
# z1 = [12.3,3.45,70.65,47.5,4.45,2.77,3.99]

# plt.figure(2)
# [g0,g1] = plt.plot(x1,y1,x1,z1)
# plt.setp(g0,color = 'red',linestyle = '-')
# plt.setp(g1,color = 'orange',linestyle = ':')
# plt.grid()
# plt.show()


Blocklen = 1000
plt.ion()
plt.figure(1)
[g] = plt.plot([],[])

input_bytes = wf.readframes(Blocklen)
while len(input_bytes)>=(Blocklen*WIDTH):
 in_signal_block = struct.unpack('h'*Blocklen,input_bytes)
 g.set_ydata(in_signal_block)
 plt.pause(0.1)
 #plt.draw()
 input_bytes = wf.readframes(Blocklen)  
# g.set_xdata(range(0,Blocklen))
# g.set_ydata()
# plt.figure(1)
# plt.ylim(2**(WIDTH-1), 2**(WIDTH-1)-1)
# plt.xlim(0,Blocklen)
# if x>0:
 # for n in range(0,N):
  # plt.set_xdata
wf.close()  
plt.ioff()
plt.show()