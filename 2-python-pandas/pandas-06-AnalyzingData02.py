# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_analyzing.asp

'''
Pandas - Analyzing DataFrames


Viewing the Data


There is also a tail() method for viewing the last rows of the DataFrame.

The tail() method returns the headers and a specified number of rows, starting from the bottom.

'''
import pandas as pd


df = pd.read_csv('2-python-pandas/data_large.csv')

print(df.tail(12))  # Note: if the number of rows is not specified, the head() method will return the last 5 rows.
