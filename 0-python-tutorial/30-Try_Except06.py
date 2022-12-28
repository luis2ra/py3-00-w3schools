# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_try_except.asp

# Demo Python Try Except - Raise an exception
'''
Python Try Except - Raise an exception (part 1)


As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the "raise" keyword.
'''
# Raise an error and stop the program if x is lower than 0:
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")
print("the end (no visible)")
