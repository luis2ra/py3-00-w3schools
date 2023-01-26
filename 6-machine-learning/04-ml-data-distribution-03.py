# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_ml_data_distribution.asp

'''
Machine Learning - Data Distribution


Big Data Distributions

An array containing 250 values is not considered very big, but now you know how to create a random set of values, 
and by changing the parameters, you can create the data set as big as you want.

'''
# Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('TkAgg')

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()

# Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
