# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_classes.asp

# Demo Python Classes and Objects - Delete Objects
'''
Python Classes & Objects - Delete Objects

You can delete objects by using the "del" keyword.
'''
# Delete the p1 object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1
print(p1)  # NameError: name 'p1' is not defined
