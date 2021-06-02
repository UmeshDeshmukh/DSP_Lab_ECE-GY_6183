# Set data after initial plot command

from matplotlib import pyplot

pyplot.figure(1)

[g1] = pyplot.plot([], [])   # Create empty graph

x = [1, 3, 9, 8, 4, 6]
y = [6, 3, 6, 8, 5, 9]

pyplot.xlim(0, 10)
pyplot.ylim(0, 10)

pyplot.setp(g1, xdata = x, ydata = y)

# OR 
# pyplot.setp(g1, xdata = x)
# pyplot.setp(g1, ydata = y)

# OR
# g1.set_xdata( x )
# g1.set_ydata( y )

pyplot.show()

