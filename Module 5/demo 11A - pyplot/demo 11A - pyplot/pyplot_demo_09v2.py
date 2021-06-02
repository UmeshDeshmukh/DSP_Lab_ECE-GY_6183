# Set data after initial plot command

from matplotlib import pyplot

pyplot.figure(1)

[g1] = pyplot.plot([], [], 'blue')  # Create empty graph
[g2] = pyplot.plot([], [], 'red')   # Create empty graph

x = [1, 3, 9, 8, 4, 6]
y = [6, 3, 6, 8, 5, 9]
z = [5, 1, 4, 2, 2, 4]

g1.set_xdata( x )
g1.set_ydata( y )

g2.set_xdata( x )
g2.set_ydata( z )

pyplot.xlim(0, 10)
pyplot.ylim(0, 10)

pyplot.show()

