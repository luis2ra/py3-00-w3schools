# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_dataframes.asp

'''
Pandas DataFrames


What is a DataFrame?

A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.


'''
import pandas as pd


data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 
