# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_classes.asp

# Demo Python Classes and Objects - Delete Object Properties
'''
Python Classes & Objects - Delete Object Properties

You can delete properties on objects by using the "del" keyword.
'''
# Delete the age property from the p1 object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age
print(p1.age)  # AttributeError: 'Person' object has no attribute 'age'
