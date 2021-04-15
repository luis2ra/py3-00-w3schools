'''
Pandas Series


What is a Series?

A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type.


Labels

If noting else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
This label can be used to access a specified value.


'''
import pandas as pd

a = [1, 7, 2]

# Create a simple Pandas Series from a list:
myvar = pd.Series(a)

print(myvar)

# Return the first value of the Series:
print(myvar[0])
