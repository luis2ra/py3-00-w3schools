# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_ml_linear_regression.asp

'''
Machine Learning - Multiple Regression


Multiple Regression

Multiple regression is like linear regression, but with more than one independent value, meaning that we try to predict 
a value based on two or more variables.

Take a look at the data set in "files/data.csv", it contains some information about cars.

We can predict the CO2 emission of a car based on the size of the engine, but with multiple regression we can throw in 
more variables, like the weight of the car, to make the prediction more accurate.

'''
import pandas
from sklearn import linear_model


df = pandas.read_csv("./6-machine-learning/files/data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300g, and the volume is 1300ccm:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)


'''
How Does it Work?

In Python we have modules that will do the work for us. Start by importing the Pandas module.

import pandas


The Pandas module allows us to read csv files and return a DataFrame object (to use files/data.csv).

df = pandas.read_csv("./6-machine-learning/files/data.csv")


Then make a list of the independent values and call this variable X. Put the dependent values in a variable called y.

X = df[['Weight', 'Volume']]
y = df['CO2']


We will use some methods from the sklearn module, so we will have to import that module as well:

from sklearn import linear_model


From the sklearn module we will use the LinearRegression() method to create a linear regression object.

This object has a method called fit() that takes the independent and dependent values as parameters and fills the regression 
object with data that describes the relationship:

regr = linear_model.LinearRegression()
regr.fit(X, y)


Now we have a regression object that are ready to predict CO2 values based on a car's weight and volume:

predictedCO2 = regr.predict([[2300, 1300]])

'''
