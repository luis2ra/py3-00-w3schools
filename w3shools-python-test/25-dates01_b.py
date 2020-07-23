# Demo Python Datetime - Python Dates
'''
Python Dates

A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

'''

# Import the datetime module and display the current date:
import datetime
import time

x = datetime.datetime(2019, 11, 18, 22, 26, 33, 58094)

def utc_to_local(dt):
    return dt - datetime.timedelta(seconds = time.timezone)

print('fecha')
print(x)
print('timezone: ', time.timezone)
print('nueva fecha')
print(utc_to_local(x))