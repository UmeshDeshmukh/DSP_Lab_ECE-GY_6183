# Set parameters after initial plot command
# of two graphs in one axis

from matplotlib import pyplot

x = [1, 3, 9, 8, 4, 6]
y = [6, 3, 6, 8, 5, 9]
z = [5, 1, 4, 2, 2, 4]

pyplot.figure(1)

# Two graphs in one axis
graph_list = pyplot.plot(x, y, x, z)

g1 = graph_list[0]
g2 = graph_list[1]

# Set parameters of first graph
g1.set_color('red')
g1.set_linewidth(2)
g1.set_linestyle('--')

# Set parameters of second graph
g2.set_color('blue')
g2.set_marker('o')
g2.set_markersize('6')

pyplot.show()
