# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_datetime.asp

# Demo Python Datetime - Python Dates
'''
Python Datetime - Python Dates

A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

'''
# Import the datetime module and display the current date:
import datetime
import time


x = datetime.datetime(2022, 12, 26, 14, 27, 33, 00000)

def utc_to_local(dt):
    return dt - datetime.timedelta(seconds = time.timezone)

print('fecha/hora UTC: ', x)
print('timezone local: ', time.timezone)
print('fecha/hora local: ', utc_to_local(x))
