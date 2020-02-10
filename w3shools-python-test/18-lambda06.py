# Demo Python Lambda - Why Use Lambda Functions?
'''
Why Use Lambda Functions? - Part 3

Or, use the same function definition to make both functions, in the same program:

'''

# Example:
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Use lambda functions when an anonymous function is required for a short period of time.
