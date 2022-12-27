# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_regex.asp

# Demo Python RegEx - Match Object
'''
Python RegEx - Match Object


A Match Object is an object containing information about the search and the result.

Note: If there is no match, the value "None" will be returned, instead of the Match Object.

The Match object has properties and methods used to retrieve information about the search, and the result:

.span()     returns a tuple containing the start-, and end positions of the match.
.string     returns the string passed into the function
.group()    returns the part of the string where there was a match

'''
# Use of group()
import re


txt = "The rain in Spain"
# Search for an upper case "S" character in the beginning of a word, and print the word:
x = re.search(r"\bS\w+", txt)
print(x.group())  # Print the part of the string where there was a match.
