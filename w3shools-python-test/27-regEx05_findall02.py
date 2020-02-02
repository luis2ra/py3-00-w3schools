# Demo Python RegEx - The findall() Function
'''

The findall() Function

The findall() function returns a list containing all matches.

The list contains the matches in the order they are found.

If no matches are found, an empty list is returned.

'''

import re

txt = "The rain in Spain"

# Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)

if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")