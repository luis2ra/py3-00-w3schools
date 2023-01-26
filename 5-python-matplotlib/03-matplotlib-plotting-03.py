# @author: https://github.com/luis2ra from https://www.w3schools.com/python/matplotlib_pyplot.asp

'''
Python Matplotlib - Matplotlib Plotting


Multiple Points

You can plot as many points as you like, just make sure you have the same number of points in both axis.

'''
# Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
plt.plot(xpoints, ypoints)
plt.show()

# Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
