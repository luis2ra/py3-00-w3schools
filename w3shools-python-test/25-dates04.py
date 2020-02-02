# Demo Python Datetime - The strftime() Method
'''
The strftime() Method

The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string.

'''

import datetime

# Display the name of the month:
x = datetime.datetime(2020, 2, 1)

print(x.strftime("%B"))