# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_datetime.asp

# Demo Python Datetime - Date Output
'''
Python Datetime - Date Output

When we execute the code from the example above the result will be:
2020-01-26 14:21:59.952569

The date contains year, month, day, hour, minute, second, and microsecond.

The "datetime" module has many methods to return information about the date object.

'''
# Return the year and name of weekday:
from datetime import datetime  # otra forma de importar la funcion "datetime" del modulo "datetime"

x = datetime.now()

print(x.year)
print(x.strftime("%A"))
