# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_inheritance.asp

# Demo Python Inheritance
'''
Python Inheritance - Python Inheritance


Python Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.


Create a Parent Class

Any class can be a parent class, so the syntax is the same as creating any other class.

'''
# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()
