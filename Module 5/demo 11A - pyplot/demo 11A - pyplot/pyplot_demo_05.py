# Set parameters after initial plot command

from matplotlib import pyplot

x = [1, 3, 9, 8, 4, 6]
y = [6, 3, 6, 8, 5, 9]

pyplot.figure(1)

[g1] = pyplot.plot(x, y)   # one graph

g1.set_color('red')
g1.set_linewidth('1')
g1.set_linestyle('--')
g1.set_marker('o')

pyplot.show()

