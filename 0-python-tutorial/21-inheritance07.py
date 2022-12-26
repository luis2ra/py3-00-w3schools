# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_inheritance.asp

# Demo Python Inheritance - Add Methods
'''
Python Inheritance - Add Methods

If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.

'''
# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    # Add Method to the Student class:
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


# Add a year parameter, and pass the correct year when creating objects:
x = Student("Luis", "Altuve", 2020)
x.welcome()
