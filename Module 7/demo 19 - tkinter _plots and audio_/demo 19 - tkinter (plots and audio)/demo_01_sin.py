# demo_01_sin.py
# Keyboard control and plotting of a sinusoind using Tkinter.
# Adjust the frequency of the sinusoid by key strokes.

from math import cos, pi 
import tkinter as Tk   	
from matplotlib import pyplot

Fs = 8000           # rate (samples/second)
f1 = 220            # f1 : frequency of sinusoid (Hz)
gain = 0.2 * 2**15
R = 2 ** (1.0/12.0)    # 1.05946309

def my_function(event):
    global CONTINUE
    global f1
    print('You pressed ' + event.char)
    if event.char == 'q':
      print('Good bye')
      CONTINUE = False
    if event.char == 'i':
      f1 = f1 * R       # increase frequency
    if event.char == 'd':
      f1 = f1 / R       # decrease frequency
    print('Frequency = %.2f' % f1)

# Define Tkinter root
root = Tk.Tk()
root.bind("<Key>", my_function)

L1 = Tk.Label(root, text = 'demo_01.py')
L1.pack()

# Switch to Python window.
print('Press i to increase frequency.')
print('Press d to decrease frequency.')
print('Press q to quit.')

BLOCKLEN = 512
output_block = [0] * BLOCKLEN
theta = 0
CONTINUE = True

n = [i for i in range(BLOCKLEN)]

pyplot.ion()           # Turn on interactive mode so plot gets updated

my_fig = pyplot.figure(1)
my_plot = my_fig.add_subplot(1, 1, 1)
[my_line] = my_plot.plot(n, output_block)
my_plot.set_ylim(-32000, 32000)
my_plot.set_xlim(0, BLOCKLEN)

# root.focus_set()        # This activates the keyboard (not always needed)

while CONTINUE:
  root.update()
  om1 = 2.0 * pi * f1 / Fs
  for i in range(0, BLOCKLEN):
    output_block[i] = int( gain * cos(theta) )
    theta = theta + om1
  while theta > pi:
    theta = theta - 2.0 * pi

  my_line.set_ydata(output_block)
  my_plot.set_title('Frequency = %.2f' % f1)
  # pyplot.pause(0.01).   # Not needed due to usage of root.update

print('* Finished')

pyplot.ioff()           # Turn off interactive mode
# pyplot.show()     # Keep plot showing at end of program

