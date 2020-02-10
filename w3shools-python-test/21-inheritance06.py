# Demo Python Inheritance - Add Properties
'''
Add Properties

In the example below, the year 2020 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:

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
    # Add the __init__() function to the Student class:
    def __init__(self, fname, lname, year):
        # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
        super().__init__(fname, lname)
        # Add a property called graduationyear to the Student class:
        self.graduationyear = year

# Add a year parameter, and pass the correct year when creating objects:
x = Student("Guido", "Van Rossum", 2020)
print(x.graduationyear)