# Demo Python Lambda
'''
Python Lambda

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.


Syntax

    lambda arguments : expression

The expression is executed and the result is returned:

'''

# A lambda function that sums argument a, b, and c and print the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))