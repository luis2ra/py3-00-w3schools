# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_string_formatting.asp

# Demo Python String Formatting - Multiple Values
'''
Python String Formatting - Multiple Values


The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method.

'''
# If you want to use more values, just add more values to the format() method:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
