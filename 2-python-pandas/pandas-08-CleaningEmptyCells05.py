# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp

'''
Pandas - Cleaning Empty Cells


Replace Using Mean, Median, or Mode

A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column.

'''
import pandas as pd


df = pd.read_csv('2-python-pandas/data_to_clean.csv')

# Calculate the MEAN, and replace any empty values with it:
x = df["Calories"].mean()  # Mean = the average value (the sum of all values divided by number of values).

df["Calories"].fillna(x, inplace = True)

print(df.to_string())
