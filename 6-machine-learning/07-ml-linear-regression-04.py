# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_ml_linear_regression.asp

'''
Machine Learning - Linear Regression


Bad Fit?

Let us create an example where linear regression would not be the best method to predict future values.

'''
# Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from scipy import stats

# These values for the x- and y-axis should result in a very bad fit for linear regression:
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)  # The result: 0.013 indicates a very bad relationship, and tells us that this data set is not suitable for linear regression.

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
