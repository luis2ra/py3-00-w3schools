# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp

'''
Pandas - Cleaning Empty Cells


Replace Only For Specified Columns

The example above replaces all empty cells in the whole Data Frame.

To only replace empty values for one column, specify the column name for the DataFrame.

'''
import pandas as pd


df = pd.read_csv('2-python-pandas/data_to_clean.csv')

df["Calories"].fillna(130, inplace = True)

print(df.to_string())
