# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_tuples_unpack.asp

# Demo Unpack Tuples
'''
Python Tuples - Unpack Tuples


Unpacking a Tuple

When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

fruits = ("apple", "banana", "cherry")

But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

'''
# Packing a tuple:
fruits1 = ("apple", "banana", "cherry")

# Unpacking a tuple:
(green, yellow, red) = fruits1

print(green)
print(yellow)
print(red)

print()


'''

Note: The number of variables must match the number of values in the tuple, if not, 
you must use an asterisk to collect the remaining values as a list.


Using Asterisk (*)

If the number of variables is less than the number of values, you can add an * to the 
variable name and the values will be assigned to the variable as a list:

'''
# Assign the rest of the values as a list called "red":
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits2

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values 
# to the variable until the number of values left matches the number of variables left.
fruits3 = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits3

print(green)
print(tropic)
print(red)
