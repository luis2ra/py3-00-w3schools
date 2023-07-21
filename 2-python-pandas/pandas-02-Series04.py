# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_series.asp

'''
Pandas Series


Part 2 - Key/Value Objects as Series

To select only some of the items in the dictionary, use the "index" argument and 
specify only the items you want to include in the Series.

'''
import pandas as pd


calories = {"day1": 420, "day2": 380, "day3": 390}

# Create a Series using only data from "day1" and "day2":
myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
