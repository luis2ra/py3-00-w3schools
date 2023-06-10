# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_ml_train_test.asp

'''
Machine Learning - Train/Test


Evaluate Your Model

In Machine Learning we create models to predict the outcome of certain events, like in the previous chapter where we predicted the CO2 emission of a car when we knew the weight and engine size.

To measure if the model is good enough, we can use a method called "Train/Test".


What is Train/Test?

Train/Test is a method to measure the accuracy of your model.

It is called Train/Test because you split the data set into two sets: a training set and a testing set.

80% for training, and 20% for testing.

You train the model using the training set. You test the model using the testing set.

Train the model means create the model. Test the model means test the accuracy of the model.


Start With a Data Set

Start with a data set you want to test.

Our data set illustrates 100 customers in a shop, and their shopping habits.

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

plt.scatter(x, y)
plt.show()

# Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
