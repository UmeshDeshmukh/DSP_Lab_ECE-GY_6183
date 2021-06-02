# filtering_ver1.py
# Low-pass filter a signal. Vary the cut-off frequency with a slider. 
# (This is not real-time.)

import numpy as np
from scipy.signal import butter, filtfilt
from matplotlib import pyplot
import tkinter as Tk

root = Tk.Tk()
root.title('Filter GUI, version 1')

cutoff_freq = Tk.DoubleVar()			# Define Tk variable
cutoff_freq.set(0.25)  					# Initilize

N = 500
n = np.arange(0, N)
x = np.sin(5 * np.pi * n/N) + 0.4 * np.random.randn(N)

pyplot.ion()           # Turn on interactive mode so plot gets updated
my_fig = pyplot.figure(1)
my_plot = my_fig.add_subplot(1, 1, 1)
[my_line] = my_plot.plot(n, x)
my_plot.set_title('Noisy signal')
my_plot.set_xlim(0, N)
my_plot.set_ylim(-3, 3)

# Update plot when slider is moved
def updatePlot(event):
	[b, a] = butter(2, 2*cutoff_freq.get())
	y = filtfilt(b, a, x)
	my_line.set_ydata(y)
	my_plot.set_title('Cut-off frequency = %f' % cutoff_freq.get() )

def my_quit():
	global CONTINUE
	CONTINUE = False
	print('Good bye')

# Define slider
S1 = Tk.Scale(root,
  length = 200, orient = Tk.HORIZONTAL, from_ = 0.01, to = 0.49, resolution = 0.005,
  command = updatePlot,
  variable = cutoff_freq)

B1 = Tk.Button(root, text = 'Quit', command = my_quit)

# Place widgets in the GUI window
S1.pack()			
B1.pack()

CONTINUE = True
while CONTINUE:
	root.update()
