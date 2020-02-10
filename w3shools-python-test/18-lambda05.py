# Demo Python Lambda - Why Use Lambda Functions?
'''
Why Use Lambda Functions? - Part 2

Or, use the same function definition to make a function that always triples the number you send in:

'''

# Example:
def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

# Use lambda functions when an anonymous function is required for a short period of time.