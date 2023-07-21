# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp

'''
Pandas - Cleaning Empty Cells


Empty Cells

Empty cells can potentially give you a wrong result when you analyze data.


Remove Rows - Parte 2

One way to deal with empty cells is to remove rows that contain empty cells.

This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

'''
import pandas as pd


df = pd.read_csv('2-python-pandas/data_to_clean.csv')

df.dropna(inplace = True)

print(df.to_string())

### Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows 
### containing NULL values from the original DataFrame.
