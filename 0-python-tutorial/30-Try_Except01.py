# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_try_except.asp

# Demo Python Try Except - Exception Handling
'''
Python Try Except


The "try" block lets you test a block of code for errors.

The "except" block lets you handle the error.

The "else" block lets you execute code when there is no error.

The "finally" block lets you execute code, regardless of the result of the try- and except blocks.


Exception Handling

When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the "try" statement.

'''
# The try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print("An exception occurred")


'''
Without the try block, the program will crash and raise an error:

print(x)


Traceback (most recent call last):
  File "demo_try_except_error.py", line 3, in <module>
    print(x)
NameError: name 'x' is not defined
'''
