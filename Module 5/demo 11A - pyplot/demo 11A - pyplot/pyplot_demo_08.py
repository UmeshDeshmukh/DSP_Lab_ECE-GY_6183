# Set parameters after initial plot command using pyplot.setp()

from matplotlib import pyplot

x = [1, 3, 9, 8, 4, 6]
y = [6, 3, 6, 8, 5, 9]
z = [5, 1, 4, 2, 2, 4]

pyplot.figure(1)

[g1] = pyplot.plot(x, y)
[g2] = pyplot.plot(x, z)

# setp : set parameter
pyplot.setp(g1, linewidth = 3)
pyplot.setp(g1, color = 'red')

pyplot.setp(g2, linewidth = 2, color = 'blue',
	linestyle = '--', marker = 'o', markersize = 8)

# To display line properties you can set: 
# pyplot.setp(g1)

pyplot.show()

