'''
Pandas Series


Create Labels

With the index argument, you can name your own labels.

'''
import pandas as pd

a = [1, 7, 2]

# Create a simple Pandas Series from a list:
myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# Return the value of "y":
print(myvar[y])
