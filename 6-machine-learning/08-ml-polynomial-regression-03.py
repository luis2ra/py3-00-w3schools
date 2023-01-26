# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_ml_linear_regression.asp

'''
Machine Learning - Polynomial Regression


Predict Future Values

Now we can use the information we have gathered to predict future values.

Example: Let us try to predict the speed of a car that passes the tollbooth at around the time 17:00:

To do so, we need the same mymodel array from the previous example:

'''
import numpy
from sklearn.metrics import r2_score


x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

speed = mymodel(17)
print(speed)

'''
The example predicted a speed to be 88.87, which we also could read from the diagram.

'''
