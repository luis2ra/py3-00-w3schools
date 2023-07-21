# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp

'''
Pandas - Cleaning Empty Cells


Replace Empty Values

Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value.

'''
import pandas as pd


df = pd.read_csv('2-python-pandas/data_to_clean.csv')

df.fillna(130, inplace = True)

print(df.to_string())
