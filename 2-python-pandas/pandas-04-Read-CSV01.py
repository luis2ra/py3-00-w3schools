# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_csv.asp

'''
Pandas Read CSV


Read CSV Files

A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

In our examples we will be using a CSV file called 'data.csv'.

'''
import pandas as pd


# Load a comma separated file (CSV file) into a DataFrame:
df = pd.read_csv('2-python-pandas/data.csv')

print(df.to_string())
