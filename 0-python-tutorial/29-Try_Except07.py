# Demo Python Try Except - Raise an exception
'''
Raise an exception

As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.

'''

# Raise a TypeError if x is not an integer:
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")