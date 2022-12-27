# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_regex.asp

# Demo Python RegEx - The split() Function
'''
Python RegEx - The split() Function


The split() function returns a list where the string has been split at each match.

'''
import re


txt = "The rain in Spain"
# Split the string at every white-space character:
x = re.split("\s", txt)
print(x)
