# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_string_formatting.asp

# Demo Python String Formatting - String format()
'''
Python String Formatting


To make sure a string will display as expected, we can format the result with the format() method.


String format()

The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method.

'''
# Add a placeholder where you want to display the price:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
