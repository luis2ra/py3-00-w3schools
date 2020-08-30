# Demo Python Functions - Number of Arguments
'''
Number of Arguments - Part 2

By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less. 

If you try to call the function with 1 or 3 arguments, you will get an error.

'''

# This function expects 2 arguments, but gets only 1:
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil")             # Esta sentencia arroja un error.

my_function("Luis", "Altuve")   # Esta sentencia nunca se ejecuta
