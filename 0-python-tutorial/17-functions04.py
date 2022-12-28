# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_functions.asp

# Demo Python Functions - Number of Arguments
'''
Python Functions - Number of Arguments - Part 2

if your function expects 2 arguments and you try to call the function with 1 or 3 arguments, you will get an error.

'''
# This function expects 2 arguments, but gets only 1:
def my_function(fname, lname):
    print(fname + " " + lname)

# Esta sentencia se ejecuta de forma correcta
my_function("Luis", "Altuve")

# Esta sentencia arroja un error.
my_function("Emil")  # TypeError: my_function() missing 1 required positional argument: 'lname'
