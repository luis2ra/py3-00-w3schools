# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_ml_linear_regression.asp

'''
Machine Learning - Linear Regression


Predict Future Values

Now we can use the information we have gathered to predict future values.

Example: Let us try to predict the speed of a 10 years old car.

To do so, we need the same myfunc() function from the example above:

def myfunc(x):
    return slope * x + intercept

'''
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

speed = myfunc(10)

print(speed)

'''
The example predicted a speed at 85.6, which we also could read from the diagram.

'''
