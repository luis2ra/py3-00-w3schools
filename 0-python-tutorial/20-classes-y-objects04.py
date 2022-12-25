# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_classes.asp

# Demo Python Classes and Objects - The __str__() Function
'''
Python Classes & Objects - The __str__() Function

The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned.

'''
# The string representation of an object WITHOUT the __str__() function:
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object of Person named p1, and print p1
p1 = Person1("John", 36)
print(p1)

print()


# The string representation of an object WITH the __str__() function:
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

# Create an object of Person named p1, and print the value of name and age
p2 = Person2("Luis", 46)
print(p2)
