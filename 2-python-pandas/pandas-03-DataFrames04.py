'''
Pandas DataFrames


Load Files Into a DataFrame

If your data sets are stored in a file, Pandas can load them into a DataFrame.

'''
import pandas as pd

# Load a comma separated file (CSV file) into a DataFrame:
df = pd.read_csv('data.csv')

print(df) 
