# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_dataframes.asp

'''
Pandas DataFrames


Load Files Into a DataFrame

If your data sets are stored in a file, Pandas can load them into a DataFrame.

'''
import pandas as pd


# Load a comma separated file (CSV file) into a DataFrame:
df = pd.read_csv('2-python-pandas/data.csv')  # ojo desde donde se invoca

print(df) 
