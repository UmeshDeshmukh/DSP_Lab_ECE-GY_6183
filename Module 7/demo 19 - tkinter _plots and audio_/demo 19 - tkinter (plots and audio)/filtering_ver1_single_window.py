# filtering_gui_single_window.py
# Low-pass filter a signal. Vary the cut-off frequency with a slider. 
# (This is not real-time.)
# This version puts the slider and the plot in the same window.

import numpy as np
from scipy.signal import butter, filtfilt
from matplotlib import pyplot
import tkinter as Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk.Tk()
root.title('Filter GUI, version 1')

N = 500
n = np.arange(0, N)
x = np.sin(5 * np.pi * n/N) + 0.4 * np.random.randn(N)

my_fig = pyplot.figure(1)
my_plot = my_fig.add_subplot(1, 1, 1)
[my_line] = my_plot.plot(n, x)
my_plot.set_title('Noisy signal')
my_plot.set_xlim(0, N)
my_plot.set_ylim(-3, 3)

# Turn fig into a Tkinter widget
my_canvas = FigureCanvasTkAgg(my_fig, master = root)
# my_fig.canvas.draw()

W1 = my_canvas.get_tk_widget()
W1.pack()

cutoff_freq = Tk.DoubleVar()			# Define Tk variable
cutoff_freq.set(0.25)  					# Initilize

# Update plot when slider is moved
def updatePlot(event):
	[b, a] = butter(2, 2*cutoff_freq.get())
	y = filtfilt(b, a, x)
	my_line.set_ydata(y)
	my_plot.set_title('Cut-off frequency = %f' % cutoff_freq.get() )
	my_fig.canvas.draw()

# Define slider
S1 = Tk.Scale(root,
  length = 200, orient = Tk.HORIZONTAL, from_ = 0.01, to = 0.49, resolution = 0.005,
  command = updatePlot,
  variable = cutoff_freq)

def my_quit():
	global CONTINUE
	CONTINUE = False
	print('Good bye')

B1 = Tk.Button(root, text = 'Quit', command = my_quit)

# Place widgets in the GUI window
S1.pack()			
B1.pack()

CONTINUE = True
while CONTINUE:
	root.update()

