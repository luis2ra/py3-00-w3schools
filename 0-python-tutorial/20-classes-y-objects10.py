# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_classes.asp

# Demo Python Classes and Objects - The pass Statement
'''
Python Classes & Objects - The pass Statement

"class" definitions cannot be empty, but if you for some reason have a "class" definition with no content, put in the "pass" statement to avoid getting an error.
'''
# Example:
class Person:
  pass


print(Person)

# other way
x = Person
print(x)

# having an empty class definition like this, would raise an error without the pass statement
