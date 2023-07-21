# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_analyzing.asp

'''
Pandas - Analyzing DataFrames


Info About the Data

The DataFrames object has a method called info(), that gives you more information about the data set.


Null Values

The info() method also tells us how many Non-Null values there are present in each column, and in 
our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with 
empty values. This is a step towards what is called cleaning data, and you will learn more about that in 
the next chapters.

'''
import pandas as pd


df = pd.read_csv('2-python-pandas/data_large.csv')

print(df.info())
