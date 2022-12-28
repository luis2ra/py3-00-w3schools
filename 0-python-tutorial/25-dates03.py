# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_datetime.asp

# Demo Python Datetime - Creating Date Objects
'''
Python Datetime - Creating Date Objects

To create a date, we can use the datetime() class (constructor) of the "datetime" module.

The datetime() class requires three parameters to create a date: year, month, day.

'''
import datetime
import pytz

# Create a date object:
x = datetime.datetime(2020, 3, 2)  
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but 
# they are optional, and has a default value of 0, (None for timezone).

print(x)

# other example
COL = pytz.timezone("America/Bogota")
y = datetime.datetime(2022, 12, 31, 11, 11, 11, 00000, tzinfo = COL)  # revisar esto si es correcto el manejo del timezone
print(y)
