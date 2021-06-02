# Example of pyplot

from matplotlib import pyplot

x = [1, 3, 9, 8, 4, 6]
y = [6, 3, 6, 8, 5, 9]

# One plot
pyplot.figure(1)
pyplot.plot(x, y)
pyplot.xlabel('Time (n)')
pyplot.ylabel('Amplitude')
pyplot.title('Data plot')
  
pyplot.show()

