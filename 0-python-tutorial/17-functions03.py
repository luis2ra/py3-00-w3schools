# Demo Python Functions - Parameters or Arguments?
'''
Parameters or Arguments?

The terms parameter and argument can be used for the same thing: information that are passed into a function.


From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that are sent to the function when it is called.


Number of Arguments

By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less. 

'''

# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes") 
