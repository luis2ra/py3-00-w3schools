# Demo Python RegEx - The sub() Function
'''

The sub() Function

The sub() function replaces the matches with the text of your choice.

You can control the number of replacements by specifying the count parameter.

'''

import re

# Replace the first two occurrences of a white-space character with the digit 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)