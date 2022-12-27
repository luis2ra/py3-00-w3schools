# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_string_formatting.asp

# Demo Python String Formatting - String format()
'''
Python String Formatting - String format()


You can add parameters inside the curly brackets to specify how to convert the value.

'''
# Format the price to be displayed as a number with two decimals:
price = 49
txt = "The price is {:.9f} dollars"
print(txt.format(price))
