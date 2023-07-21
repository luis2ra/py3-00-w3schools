# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_series.asp

'''
Pandas Series


DataFrames

Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.

'''
import pandas as pd


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# Create a DataFrame from two Series
myvar = pd.DataFrame(data)

print(myvar)
