# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_string_formatting.asp

# Demo Python String Formatting - Index Numbers
'''
Python String Formatting - Index Numbers (part 1)

You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders.

'''
# Example
quantity = 3
itemno = 567
price = 1
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


'''
Other example:

Reference link: https://mkaz.blog/code/python-string-format-cookbook/

'''
my_format = "{:0>4d} - {:0>4x}"
print(my_format.format(price, price))
price = 15
my_format = "{:0>2d} - {:0>2x}"
print(my_format.format(price, price))

index = 0
print('{:0>4d}'.format(index+1))
