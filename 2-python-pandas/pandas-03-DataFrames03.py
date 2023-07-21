# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_dataframes.asp

'''
Pandas DataFrames


Named Indexes

With the index argument, you can name your own indexes.


Locate Named Indexes

Use the named index in the loc attribute to return the specified row(s). 

'''
import pandas as pd


data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# Add a list of names to give each row a name:
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
print('\n')

# refer to the name index / return "day2":
print(df.loc["day2"])
print('\n')

# use a list of name indexes / return row day and day3:
print(df.loc[["day1", "day3"]])
