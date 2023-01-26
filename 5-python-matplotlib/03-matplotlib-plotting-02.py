# @author: https://github.com/luis2ra from https://www.w3schools.com/python/matplotlib_pyplot.asp

'''
Python Matplotlib - Matplotlib Plotting


Plotting Without Line

To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

'''
# Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

# Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):
plt.plot(xpoints, ypoints, 'o')
plt.show()

# Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
