# Update plot using interactive mode (ion)

from matplotlib import pyplot
import math

pyplot.ion()  # Turn on interactive mode  

pyplot.figure(1)
pyplot.xlim(0, 100)
pyplot.ylim(-1.2, 1.2)

for x in range(100):
	pyplot.plot(x, math.sin(x/10), 'ro')  # plot each point as a red dot
	# pyplot.draw()        	 # Show result (not always needed)
	pyplot.pause(0.0001)

pyplot.ioff()	# Turn off interactive mode
pyplot.show()
