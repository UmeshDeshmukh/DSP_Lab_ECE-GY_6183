# filtering_ver2.py

import numpy as np
from scipy.signal import butter, filtfilt
from matplotlib import pyplot
import tkinter as Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk.Tk()
root.title('Filter GUI, version 2')

N = 500
n = np.arange(0, N)
x = np.sin(5 * np.pi * n/N) + 0.4 * np.random.randn(N)

my_fig = pyplot.figure()
my_plot = my_fig.add_subplot(1, 1, 1)
my_plot.plot(n, x, label = 'Noisy data', marker = '.', markersize = 5, linestyle = 'None', color = 'gray')
[my_line] = my_plot.plot(n, x, label = 'Filtered data', linewidth = 2, color = 'black')
my_plot.legend()
my_plot.set_xlim(0, N)
my_plot.set_ylim(-3, 3)

# Turn fig into a Tkinter widget
canvas = FigureCanvasTkAgg(my_fig, master = root)
my_fig.canvas.draw()

W1 = canvas.get_tk_widget()
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

def my_quit():
  global CONTINUE
  CONTINUE = False
  print('Good bye')
  root.quit()     # stops mainloop
  root.destroy()  # This prevents an error on Windows

# Define slider
S1 = Tk.Scale(root,
  length = 200, orient = Tk.HORIZONTAL, 
  from_ = 0.01, to = 0.49,
  resolution = 0.005,
  command = updatePlot,
  variable = cutoff_freq, label = 'Cut-off frequency')

B1 = Tk.Button(root, text = 'Quit', command = my_quit)

# Place widgets in the GUI window
S1.pack()
B1.pack()

updatePlot(None)

CONTINUE = True
while CONTINUE:
  root.update()

