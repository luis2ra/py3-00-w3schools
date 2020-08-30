# Demo Python Inheritance
'''
Create a Parent Class

Any class can be a parent class, so the syntax is the same as creating any other class.


Create a Child Class

To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class.

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
    pass    # Note: Use the 'pass' keyword when you do not want to add any other properties or methods to the class.


# Now the Student class has the same properties and methods as the Person class.
x = Student("Mike", "Olsen")
x.printname()   # Usa el método printname heredado de la clase Person.
