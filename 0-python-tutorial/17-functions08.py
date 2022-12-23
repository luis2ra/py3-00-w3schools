# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_functions.asp

# Demo Python Functions - Default Parameter Value
'''
Python Functions - Default Parameter Value

The following example shows how to use a default parameter value.

'''
# If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()           # Asume el valor por defecto
my_function("Brazil")
