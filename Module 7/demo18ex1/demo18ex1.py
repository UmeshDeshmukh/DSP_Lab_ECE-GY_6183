# keyboard_demo_06.py
# Play a note using a second-order difference equation
# when the user presses a key on the keyboard.

import pyaudio, struct
import numpy as np
from scipy import signal
from math import sin, cos, pi
import tkinter as Tk    

BLOCKLEN   = 64        # Number of frames per block
WIDTH       = 2         # Bytes per sample
CHANNELS    = 1         # Mono
RATE        = 8000      # Frames per second

MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

# Parameters
Ta = 2      # Decay time (seconds)
f1 = 440    # Frequency (Hz)

# Pole radius and angle
r = 0.01**(1.0/(Ta*RATE))       # 0.01 for 1 percent amplitude
om1 = 2.0 * pi * float(f1)/RATE

a2 = r**2
# Filter coefficients (second-order IIR)
a = [1, -2*r*cos(om1), r**2]
b = [r*sin(om1)]
ORDER = 2   # filter order
statesa = np.zeros(ORDER)
statess = np.zeros(ORDER)
statesd = np.zeros(ORDER)
statesf = np.zeros(ORDER)
statesg = np.zeros(ORDER)
statesh = np.zeros(ORDER)
statesj = np.zeros(ORDER)
statesk = np.zeros(ORDER)
statesl = np.zeros(ORDER)
statesb = np.zeros(ORDER)
statesn = np.zeros(ORDER)
statesm = np.zeros(ORDER)

x  = np.zeros(BLOCKLEN)
xa = np.zeros(BLOCKLEN)
xs = np.zeros(BLOCKLEN)
xd = np.zeros(BLOCKLEN)
xf = np.zeros(BLOCKLEN)
xg = np.zeros(BLOCKLEN)
xh = np.zeros(BLOCKLEN)
xj = np.zeros(BLOCKLEN)
xk = np.zeros(BLOCKLEN)
xl = np.zeros(BLOCKLEN)
xb = np.zeros(BLOCKLEN)
xn = np.zeros(BLOCKLEN)
xm = np.zeros(BLOCKLEN)
y = 0.0



# Open the audio output stream
p = pyaudio.PyAudio()
PA_FORMAT = pyaudio.paInt16
stream = p.open(
        format      = PA_FORMAT,
        channels    = CHANNELS,
        rate        = RATE,
        input       = False,
        output      = True,
        frames_per_buffer = 128)
# specify low frames_per_buffer to reduce latency

CONTINUE = True
KEYPRESS = False

def my_function(event):
    global CONTINUE
    global KEYPRESS
    print('You pressed ' + event.char)
    
    if event.char == 'q':
      print('Good bye')
      CONTINUE = False
    
    Ch.set(event.char)
     
    if event.char == 'a':
     xa[0] = 10000.0#[y0, states] = signal.lfilter([b1[0]],[1,a1[0],a2],x, zi = states)
    if event.char == 's':
     xs[0] = 10000.0 #[y1, states] = signal.lfilter([b1[1]],[1,a1[1],a2],x, zi = states)
    if event.char == 'd':
     xd[0] = 10000.0 # [y2, states] = signal.lfilter([b1[2]],[1,a1[2],a2],x, zi = states)
    if event.char == 'f':
     xg[0] = 10000.0 # [y3, states] = signal.lfilter([b1[3]],[1,a1[3],a2],x, zi = states)
    if event.char == 'g':
     xg[0] = 10000.0 # [y4, states] = signal.lfilter([b1[4]],[1,a1[4],a2],x, zi = states)
    if event.char == 'h':
     xh[0] = 10000.0 # [y5, states] = signal.lfilter([b1[5]],[1,a1[5],a2],x, zi = states)  
    if event.char == 'j':
     xj[0] = 10000.0 # [y6, states] = signal.lfilter([b1[6]],[1,a1[6],a2],x, zi = states)
    if event.char == 'k':
     xk[0] = 10000.0 # [y7, states] = signal.lfilter([b1[7]],[1,a1[7],a2],x, zi = states)
    if event.char == 'l':
     xl[0] = 10000.0 # [y8, states] = signal.lfilter([b1[8]],[1,a1[8],a2],x, zi = states) 
    if event.char == 'b':
     xb[0] = 10000.0 # [y9, states] = signal.lfilter([b1[9]],[1,a1[9],a2],x, zi = states)
    if event.char == 'n':
     xn[0] = 10000.0 # [y10, states] = signal.lfilter([b1[10]],[1,a1[10],a2],x, zi = states)
    if event.char == 'm':
     xm[0] = 10000.0 # [y11, states] = signal.lfilter([b1[11]],[1,a1[11],a2],x, zi = states)
    # f2 = (2**(k/12))*f1  
    # om2 = 2.0 * pi * float(f2)/RATE 
    # a1 = [1, -2*r*cos(om2), r**2]
    # b1 = [r*sin(om2)]    
    KEYPRESS = True
    
    
root = Tk.Tk()
root.bind("<Key>", my_function)
Ch = Tk.StringVar()

 
print('Press keys a,s,d,f,g,h,j,k,l,b,n,m for sound.')
print('Press "q" to quit')
b1 = 12 *[0] 
a1 = 12 *[0] 
for n in range(0,12):
 f2 = (2**(n/12))*f1  
 om2 = 2.0 * pi * float(f2)/RATE
 a1[n] = -2*r*cos(om2)
 b1[n] = r*sin(om2)

while CONTINUE:
    root.update()

    if KEYPRESS and CONTINUE:
        # Some key (not 'q') was pressed
        x[0] = 10000.0
    #y0 = 0, y2 = 0 , y3 = 0 , y4 = 0 , y5 = 0 , y6 = 0 , y7 = 0 , y8 = 0 , y9 = 0 , y10 = 0 , y11 = 0  
    
    
    [y0, statesa] = signal.lfilter([b1[0]],[1,a1[0],a2],xa, zi = statesa)
    
    [y1, statess] = signal.lfilter([b1[1]],[1,a1[1],a2],xs, zi = statess)
   
    [y2, statesd] = signal.lfilter([b1[2]],[1,a1[2],a2],xd, zi = statesd)
    
    [y3, statesf] = signal.lfilter([b1[3]],[1,a1[3],a2],xf, zi = statesf)

    [y4, statesg] = signal.lfilter([b1[4]],[1,a1[4],a2],xg, zi = statesg)
    
    [y5, statesh] = signal.lfilter([b1[5]],[1,a1[5],a2],xh, zi = statesh)  
    
    [y6, statesj] = signal.lfilter([b1[6]],[1,a1[6],a2],xj, zi = statesj)
    
    [y7, statesk] = signal.lfilter([b1[7]],[1,a1[7],a2],xk, zi = statesk)
   
    [y8, statesl] = signal.lfilter([b1[8]],[1,a1[8],a2],xl, zi = statesl) 
    
    [y9, statesb] = signal.lfilter([b1[9]],[1,a1[9],a2],xb, zi = statesb)
   
    [y10, statesn] = signal.lfilter([b1[10]],[1,a1[10],a2],xn, zi = statesn)
    
    [y11, statesm] = signal.lfilter([b1[11]],[1,a1[11],a2],xm, zi = statesm)
    
    y = y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11
    x[0] = 0.0 
    #print(y)
    xa[0] = 0.0
    xs[0] = 0.0
    xd[0] = 0.0
    xf[0] = 0.0
    xg[0] = 0.0
    xh[0] = 0.0
    xj[0] = 0.0
    xk[0] = 0.0
    xl[0] = 0.0
    xb[0] = 0.0
    xn[0] = 0.0
    xm[0] = 0.0
    
    KEYPRESS = False

    y = np.clip(y.astype(int), -MAXVALUE, MAXVALUE)     # Clipping

    binary_data = struct.pack('h' * BLOCKLEN, *y);    # Convert to binary binary data
    stream.write(binary_data, BLOCKLEN)               # Write binary binary data to audio output

print('* Done.')

# Close audio stream
stream.stop_stream()
stream.close()
p.terminate()
