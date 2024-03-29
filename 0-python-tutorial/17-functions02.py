# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_functions.asp

# Demo Python Functions - Arguments
'''
Python Functions - Arguments

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add 
as many arguments as you want, just separate them with a comma.

'''
# The following example has a function with one argument (fname). When the function is 
# called, we pass along a first name, which is used inside the function to print the full name: 
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") 

# Arguments are often shortened to args in Python documentations.
