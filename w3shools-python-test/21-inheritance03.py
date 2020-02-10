# Demo Python Inheritance - Add the __init__() Function
'''
Add the __init__() Function

So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object.

When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.


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
        Person.__init__(self, fname, lname)


# Now the Student class has the same properties and methods as the Person class.
x = Student("Luis", "Altuve")
x.printname()   # Usa el método printname heredado de la clase Person.
