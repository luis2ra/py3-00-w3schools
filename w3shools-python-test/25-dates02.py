# Demo Python Datetime - Date Output
'''
Date Output

When we execute the code from the example above the result will be:
2020-01-26 14:21:59.952569

The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.


'''

import datetime

# Return the year and name of weekday:
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))