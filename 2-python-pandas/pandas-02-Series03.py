# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_series.asp

'''
Pandas Series


Key/Value Objects as Series

You can also use a key/value object, like a dictionary, when creating a Series.

Note: The keys of the dictionary become the labels.

'''
import pandas as pd


calories = {"day1": 420, "day2": 380, "day3": 390}

# Create a simple Pandas Series from a dictionary:
myvar = pd.Series(calories)

print(myvar)

# Return the value of "day1":
print(myvar["day1"])
