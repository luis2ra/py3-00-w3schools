# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_regex.asp

# Demo Python RegEx - The findall() Function
'''
Python RegEx - The findall() Function


The findall() function returns a list containing all matches.

If no matches are found, an empty list is returned:

'''
import re


txt = "The rain in Spain"

# Check if "Portugal" is in the string:
x = re.findall("Portugal", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")  # Return an empty list if no match was found
    print(type(x))
