# Demo Python Iterators - Looping Through an Iterator
'''
Looping Through an Iterator - Part 1

We can also use a for loop to iterate through an iterable object.

The for loop actually creates an iterator object and executes the next() method for each loop.

'''

# Iterate the values of a tuple:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x) 