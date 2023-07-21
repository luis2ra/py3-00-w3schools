# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_csv.asp

'''
Pandas Read CSV


Read CSV Files - Part 2

If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows.

'''
import pandas as pd


# defaul value for the DataFrame
pd.options.display.max_rows = 60

# Load a comma separated file (CSV file) into a DataFrame:
df = pd.read_csv('2-python-pandas/data_large.csv')

print(df.to_string())  # Tip: use to_string() to print the entire DataFrame.
