# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_regex.asp

# Demo Python RegEx - The sub() Function
'''
Python RegEx - The sub() Function


The sub() function replaces the matches with the text of your choice.

You can control the number of replacements by specifying the "count" parameter.

'''
# Example of use for Blooz
import re


txt = "Vìlla María del Triunfo"
# Replace all "ì" or "í" characters with the character "i":
x = re.sub("[ì,í]", "i", txt)
print(x)
