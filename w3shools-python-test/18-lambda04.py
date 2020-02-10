# Demo Python Lambda - Why Use Lambda Functions?
'''
Why Use Lambda Functions? - Part 1

The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
    return lambda a : a * n

Use that function definition to make a function that always doubles the number you send in.

'''

# A lambda function that sums argument a, b, and c and print the result:
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# Use lambda functions when an anonymous function is required for a short period of time.