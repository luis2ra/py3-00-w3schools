# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_csv.asp

'''
Pandas Read CSV


Read CSV Files - Part 3


max_rows

The number of rows returned is defined in Pandas option settings.

You can check your system's maximum rows with the pd.options.display.max_rows statement.

In my system the number is 60, which means that if the DataFrame contains more than 60 rows, 
the print(df) statement will return only the headers and the first and last 5 rows.

You can change the maximum rows number with the same statement.

'''
import pandas as pd


# Check the number of maximum returned rows:
print(pd.options.display.max_rows) 

# Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows = 9999

df = pd.read_csv('2-python-pandas/data_large.csv')

print(df) 
