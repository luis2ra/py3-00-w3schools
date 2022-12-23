# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_functions.asp

# Demo Python Functions - The pass Statement
'''
Python Functions - The pass Statement

function definitions cannot be empty, but if you for some reason have a function definition 
with no content, put in the "pass" statement to avoid getting an error.

'''
# Example:
def myfunction():
    pass

# having an empty function definition like this, would raise an error without the pass statement

print('antes de invocar la función')
print(myfunction())  # In this case, return None
print('después de invocar la función')
