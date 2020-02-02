# Demo Python RegEx - The split() Function
'''

The split() Function

The split() function returns a list where the string has been split at each match.

You can control the number of occurrences by specifying the maxsplit parameter.

'''

import re

# Split the string at the first white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)