# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_regex.asp

# Demo Python RegEx - The search() Function
'''
Python RegEx - The search() Function


The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned.

If no matches are found, the value "None" is returned.

'''
import re


txt = "The rain in Spain"

# Make a search that returns no match:
x = re.search("Portugal", txt)
print(x)
