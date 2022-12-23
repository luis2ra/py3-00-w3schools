# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_functions.asp

# Demo Python Functions - Arbitrary Keyword Arguments
'''
Python Functions - Arbitrary Keyword Arguments, **kwargs

If you do not know how many keyword arguments that will be passed into your 
function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly.

'''
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Luis", lname = "Altuve") 


# Arbitrary Keyword Arguments are often shortened to **kwargs in Python documentations.
