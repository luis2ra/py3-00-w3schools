# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_try_except.asp

# Demo Python Try Except - Raise an exception
'''
Python Try Except - Raise an exception (part 2)


The "raise" keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.

'''
# Raise a TypeError if x is not an integer:
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
