# Save figure as pdf file

from matplotlib import pyplot

x = [1, 3, 9, 8, 4, 6]
y = [6, 3, 6, 8, 5, 9]
z = [5, 1, 4, 2, 2, 4]

my_fig = pyplot.figure(1)

pyplot.plot( x, y, 'r--', label = 'apples', linewidth = 2 )
pyplot.plot( x, z, 'y', label = 'bananas', linewidth = 3 )
pyplot.xlabel('Time (n)')
pyplot.legend()
pyplot.show()

my_fig.savefig('pyplot_demo_04_figure.pdf')
