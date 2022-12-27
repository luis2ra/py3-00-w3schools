# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_regex.asp

# Demo Python RegEx - The sub() Function
'''
Python RegEx - The sub() Function


The sub() function replaces the matches with the text of your choice.

'''
import re

# Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
