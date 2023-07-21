# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_json.asp

'''
Pandas Read JSON


Read JSON

Big data sets are often stored, or extracted as JSON.

JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

In our examples we will be using a JSON file called 'data.json'.

'''
import pandas as pd


# Load the JSON file into a DataFrame:
df = pd.read_json('2-python-pandas/data.json')

print(df.to_string())  # Tip: use to_string() to print the entire DataFrame.
