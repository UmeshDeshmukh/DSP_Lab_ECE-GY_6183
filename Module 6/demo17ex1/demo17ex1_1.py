# Tk_demo_04_slider.py
# TKinter demo
# Play a sinusoid using Pyaudio. Use two sliders to adjust the frequency and gain.

from math import cos, pi 
import pyaudio, struct
import tkinter as Tk   	

def fun_quit():
  global CONTINUE
  print('Good bye')
  CONTINUE = False

Fs = 8000     # rate (samples/second)
gain = 0.2 * 2**15

# Define Tkinter root
root = Tk.Tk()

# Define Tk variables
f1 = Tk.DoubleVar()
gain = Tk.DoubleVar()

# Initialize Tk variables
f1.set(200)   # f1 : frequency of sinusoid (Hz)
gain.set(0.2 * 2**15)

# Define widgets
S_freq = Tk.Scale(root, label = 'Frequency', variable = f1, from_ = 100, to = 400, tickinterval = 100)
S_gain = Tk.Scale(root, label = 'Gain', variable = gain, from_ = 0, to = 2**15-1)
B_quit = Tk.Button(root, text = 'Quit', command = fun_quit)

# Place widgets
B_quit.pack(side = Tk.BOTTOM, fill = Tk.X)
S_freq.pack(side = Tk.LEFT)
S_gain.pack(side = Tk.LEFT)

# Create Pyaudio object
p = pyaudio.PyAudio()
stream = p.open(
  format = pyaudio.paInt16,  
  channels = 1, 
  rate = Fs,
  input = False, 
  output = True,
  frames_per_buffer = 128)            
  # specify low frames_per_buffer to reduce latency

BLOCKLEN = 256
# BLOCKLEN = 10000
output_block = [0] * BLOCKLEN
theta = 0
CONTINUE = True
old_gain =0.0
print('* Start')
while CONTINUE:
  root.update()
  om1 = 2.0 * pi * f1.get() / Fs
  for i in range(0, BLOCKLEN):
    new_gain = (old_gain + gain.get())/2  
    output_block[i] = int( new_gain * cos(theta) )
    old_gain = gain.get()
    theta = theta + om1
  if theta > pi:
  	theta = theta - 2.0 * pi
  binary_data = struct.pack('h' * BLOCKLEN, *output_block)   # 'h' for 16 bits
  stream.write(binary_data)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
