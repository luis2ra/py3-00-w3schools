# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_regex.asp

# Demo Python RegEx - The sub() Function
'''
Python RegEx - The sub() Function


The sub() function replaces the matches with the text of your choice.

You can control the number of replacements by specifying the "count" parameter.

'''
import re


txt = "The rain in Spain"
# Replace the first two occurrences of a white-space character with the digit 9:
x = re.sub("\s", "9", txt, 2)
print(x)
