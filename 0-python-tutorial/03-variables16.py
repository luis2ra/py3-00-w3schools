# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_variables_global.asp

# Demo Python Variables - Global Variables
'''
Python Variables - Global Variables


Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

'''
# Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
