# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_ml_train_test.asp

'''
Machine Learning - Train/Test


Display the Testing Set

To make sure the testing set is not completely different, we will take a look at the testing set as well.

Example
plt.scatter(test_x, test_y)
plt.show()

Result:
The testing set also looks like the original data set:

'''
# Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('TkAgg')

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)  # The x axis represents the number of minutes before making a purchase.
y = numpy.random.normal(150, 40, 100) / x  # The y axis represents the amount of money spent on the purchase.

# train_x = x[:80]
# train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

plt.scatter(test_x, test_y)
plt.show()

# Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
