# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_strings_modify.asp

# Demo Python Strings - Modify Strings
'''
Python Strings - Modify Strings


Python has a set of built-in methods that you can use on strings.

'''
# The upper() method returns the string in upper case:
a = "Hello, World!"
print("string original: ", a)
print(a.upper())

# The lower() method returns the string in lower case:
a = "Hello, World!"
print("string original: ", a)
print(a.lower())

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print("string original: ", a)
print(a.strip())

# The replace() method replaces a string with another string:
a = "Hello, World!"
print("string original: ", a)
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print("string original: ", a)
print(a.split(","))  # returns ['Hello', ' World!']

'''
Split String

The split() method returns a list where the text between the specified separator becomes the list items.
'''
