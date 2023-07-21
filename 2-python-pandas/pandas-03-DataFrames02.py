# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_dataframes.asp

'''
Pandas DataFrames


Locate Row

As you can see from the result above (in the previous practice), the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)

'''
import pandas as pd


data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 

# refer to the row index / return row 1:
print(df.loc[1])
# Note: This example returns a Pandas Series.


# use a list of indexes / return row 0 and 1::
print(df.loc[[0, 1]])
# Note: When using [], the result is a Pandas DataFrame.
