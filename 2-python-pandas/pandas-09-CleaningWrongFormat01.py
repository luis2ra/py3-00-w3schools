# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_format.asp

'''
Pandas - Cleaning Data of Wrong Format


Data of Wrong Format

Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

'''
import pandas as pd


df = pd.read_csv('2-python-pandas/data_to_clean.csv')

# Convert to date:
df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())


### As you can see from the result, the date in row 26 was fixed, but the empty date in 
### row 22 got a NaT (Not a Time) value, in other words an empty value. One way to deal 
### with empty values is simply removing the entire row.
