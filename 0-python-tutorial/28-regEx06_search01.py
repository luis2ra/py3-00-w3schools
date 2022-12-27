# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_regex.asp

# Demo Python RegEx - The search() Function
'''
Python RegEx - The search() Function


The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned.

'''
import re


txt = "The rain in Spain"
# Search for the first white-space character in the string:
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
