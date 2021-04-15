# Demo python variables - Global Variables
'''
Global Variables

Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

If you create a variable with the same name inside a function, this variable will be local, and 
can only be used inside the function. The global variable with the same name will remain as it was,
global and with the original value.

'''
# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)