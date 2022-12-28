# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_inheritance.asp

# Demo Python Inheritance - Add Properties
'''
Python Inheritance - Add Properties (Part 2)

In this example, the year 2020 should be a variable, and passed into the Student class when creating 
student objects. To do so, add another parameter in the __init__() function:

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
    # add another parameter in the __init__() function:
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        # Add a year parameter, and pass the correct year when creating objects:
        self.graduationyear = year


# Add a year parameter, and pass the correct year when creating objects:
x = Student("Guido", "Van Rossum", 2020)
print(x.graduationyear)
