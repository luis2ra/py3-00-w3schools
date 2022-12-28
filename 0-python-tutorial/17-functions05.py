# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_functions.asp

# Demo Python Functions - Arbitrary Arguments
'''
Python Functions - Arbitrary Arguments, *args

If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

'''
# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])
    print(type(kids))  # se constata que el parametro recibido es una tupla

my_function("Emil", "Tobias", "Linus")


# Arbitrary Arguments are often shortened to *args in Python documentations.
