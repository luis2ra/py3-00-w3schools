# Demo Python String Formatting - String format()
'''
String format()

The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method.
'''

# You can add parameters inside the curly brackets to specify how to convert the value.
# Format the price to be displayed as a number with two decimals:
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))