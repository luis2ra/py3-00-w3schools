# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_format.asp

'''
Pandas - Cleaning Data of Wrong Format


Removing Rows

The result from the converting in the example above gave us a NaT value, which can be handled 
as a NULL value, and we can remove the row by using the dropna() method.

'''
import pandas as pd


df = pd.read_csv('2-python-pandas/data_to_clean.csv')

# Convert to date:
df['Date'] = pd.to_datetime(df['Date'])

df.dropna(subset=['Date'], inplace = True)

print(df.to_string())
