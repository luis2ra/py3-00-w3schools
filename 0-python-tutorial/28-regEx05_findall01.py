# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_regex.asp

# Demo Python RegEx - The findall() Function
'''
Python RegEx - The findall() Function


The findall() function returns a list containing all matches.

'''
import re


# Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
