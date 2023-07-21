# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_analyzing.asp

'''
Pandas - Analyzing DataFrames


Viewing the Data

One of the most used method for getting a quick overview of the DataFrame, is the head() method.

The head() method returns the headers and a specified number of rows, starting from the top.

'''
import pandas as pd


df = pd.read_csv('2-python-pandas/data_large.csv')

print(df.head(10))
