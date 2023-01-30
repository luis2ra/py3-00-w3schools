# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_ml_scale.asp

'''
Machine Learning - Scale


Scale Features

When your data has different values, and even different measurement units, it can be difficult to compare them. What is 
kilograms compared to meters? Or altitude compared to time?

The answer to this problem is scaling. We can scale data into new values that are easier to compare.

Take a look at the data set in "files/data_2.csv", it contains some information about cars.

It can be difficult to compare the volume 1.0 with the weight 790, but if we scale them both into comparable values, we 
can easily see how much one value is compared to the other.

There are different methods for scaling data, in this tutorial we will use a method called "standardization".

The standardization method uses this formula:

z = (x - u) / s

Where z is the new value, x is the original value, u is the mean and s is the standard deviation.


If you take the weight column from the data set above, the first value is 790, and the scaled value will be:

(790 - 1292.23) / 238.74 = -2.1
If you take the volume column from the data set above, the first value is 1.0, and the scaled value will be:

(1.0 - 1.61) / 0.38 = -1.59

Now you can compare -2.1 with -1.59 instead of comparing 790 with 1.0.

You do not have to do this manually, the Python sklearn module has a method called StandardScaler() which returns 
a Scaler object with methods for transforming data sets.

'''
import pandas
from sklearn.preprocessing import StandardScaler


scale = StandardScaler()

df = pandas.read_csv("./6-machine-learning/files/data_2.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)
