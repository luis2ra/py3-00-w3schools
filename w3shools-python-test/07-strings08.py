# Demo Python Strings - String Methods
'''
String Methods

Python has a set of built-in methods that you can use on strings.

'''

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print("string orinal: ", a)
print(a.strip())

# The lower() method returns the string in lower case:
a = "Hello, World!"
print("string orinal: ", a)
print(a.lower())

# The upper() method returns the string in upper case:
a = "Hello, World!"
print("string orinal: ", a)
print(a.upper())

# The replace() method replaces a string with another string:
a = "Hello, World!"
print("string orinal: ", a)
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print("string orinal: ", a)
print(a.split(",")) # returns ['Hello', ' World!']
