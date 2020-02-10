# Demo Python Inheritance - Add Properties
'''
Add Properties

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
    def __init__(self, fname, lname):
        # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
        super().__init__(fname, lname)
        # Add a property called graduationyear to the Student class:
        self.graduationyear = 2020

# Now the Student class has the same properties and methods as the Person class.
x = Student("Guido", "Van Rossum")
x.printname()   # Usa el método printname heredado de la clase Person.
print(x.graduationyear)