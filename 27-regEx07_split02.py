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

txt2 = "invoices/pdf/R-20605469958-03-B001-104.zip"
y = re.split("\-", txt2, 3)
print(y[3])
res = re.split("\.", y[3], 1)
print(res[0])
print('------------------------------------------')