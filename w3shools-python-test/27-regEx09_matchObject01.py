# Demo Python RegEx - Match Object
'''

Match Object

A Match Object is an object containing information about the search and the result.

Note: If there is no match, the value None will be returned, instead of the Match Object.

The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match

'''

import re

# The search() function returns a Match object:

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)                # this will print an object 