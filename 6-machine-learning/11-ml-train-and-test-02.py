# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_ml_train_test.asp

'''
Machine Learning - Train/Test


Split Into Train/Test

The training set should be a random selection of 80% of the original data.

The testing set should be the remaining 20%.

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]


Display the Training Set

Display the same scatter plot with the training set:

Example
plt.scatter(train_x, train_y)
plt.show()

Result:
It looks like the original data set, so it seems to be a fair selection:

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

train_x = x[:80]
train_y = y[:80]

# test_x = x[80:]
# test_y = y[80:]

plt.scatter(train_x, train_y)
plt.show()

# Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
