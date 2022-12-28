# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_classes.asp

# Demo Python Classes and Objects - Modify Object Properties
'''
Python Classes & Objects - Modify Object Properties

You can modify properties on objects like this:

'''
# Set the age of p1 to 40:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)

p1.age = 40
print(p1.age)
