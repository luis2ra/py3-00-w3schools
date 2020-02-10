# Demo Python Functions - The pass Statement
'''
The pass Statement

function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

'''

# Example:
def myfunction():
    pass

# having an empty function definition like this, would raise an error without the pass statement

print('antes de invocar la función')
print(myfunction())
print('después de invocar la función')

