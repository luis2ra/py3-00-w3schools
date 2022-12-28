# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_string_formatting.asp

# Demo Python String Formatting - Index Numbers
'''
Python String Formatting - Index Numbers (part 2)

Also, if you want to refer to the same value more than once, use the index number.

'''
# Also, if you want to refer to the same value more than once, use the index number:
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
