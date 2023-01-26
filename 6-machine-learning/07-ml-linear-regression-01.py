# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_ml_linear_regression.asp

'''
Machine Learning - Linear Regression


Regression

The term regression is used when you try to find the relationship between variables.

In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.


Linear Regression

Linear regression uses the relationship between the data-points to draw a straight line through all them.

This line can be used to predict future values.

In Machine Learning, predicting the future is very important.


How Does it Work?

Python has methods for finding a relationship between data-points and to draw a line of linear regression. We will 
show you how to use these methods instead of going through the mathematic formula.

In the example below, the x-axis represents age, and the y-axis represents speed. We have registered the age and speed 
of 13 cars as they were passing a tollbooth. Let us see if the data we collected could be used in a linear regression:

'''
# Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

'''
Scatter Plot Explained

Import the modules you need:

import matplotlib.pyplot as plt
from scipy import stats


Create the arrays that represent the values of the x and y axis:

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]


Execute a method that returns some important key values of Linear Regression:

slope, intercept, r, p, std_err = stats.linregress(x, y)


Create a function that uses the slope and intercept values to return a new value. This new value represents 
where on the y-axis the corresponding x value will be placed:

def myfunc(x):
    return slope * x + intercept


Run each value of the x array through the function. This will result in a new array with new values for the y-axis:

mymodel = list(map(myfunc, x))


Draw the original scatter plot:

plt.scatter(x, y)


Draw the line of linear regression:

plt.plot(x, mymodel)


Display the diagram:

plt.show()

'''
