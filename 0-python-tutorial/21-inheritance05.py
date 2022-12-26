# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_inheritance.asp

# Demo Python Inheritance - Add Properties
'''
Python Inheritance - Add Properties (Part 1)

'''
# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Create a class named Student, add a property called "graduationyear":
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        # Add a property called graduationyear to the Student class:
        self.graduationyear = 2020


# create an instance of Student
x = Student("Guido", "Van Rossum")
x.printname()
print(x.graduationyear)  # checking new property for Student class
