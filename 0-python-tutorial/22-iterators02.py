# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_iterators.asp

# Demo Python Iterators - Iterator vs Iterable
'''
Python Iterators - Iterator vs Iterable

Even strings are iterable objects, and can return an iterator:

'''
# Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
