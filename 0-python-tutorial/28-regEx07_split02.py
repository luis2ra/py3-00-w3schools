# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_regex.asp

# Demo Python RegEx - The split() Function
'''
Python RegEx - The split() Function


The split() function returns a list where the string has been split at each match.

You can control the number of occurrences by specifying the "maxsplit" parameter.

'''
import re


txt = "The rain in Spain"
# Split the string at the first white-space character:
x = re.split("\s", txt, 1)
print(x)

print('------------------------------------------')

txt2 = "invoices/pdf/R-20605469958-03-B001-104.zip"
y = re.split("\-", txt2, 3)
print(y[3])
res = re.split("\.", y[3], 1)
print(res[0])

print('------------------------------------------')

txt3= "/usr/src/app/config"
y = re.split("\/", txt3, 1)
print(y)
print("The first character is located in position:", y)
