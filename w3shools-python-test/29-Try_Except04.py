# Demo Python Try Except - Finally
'''
Finally

The finally block, if specified, will be executed regardless if the try block raises an error or not.

'''

# The finally block gets executed no matter if the try block raises any errors or not:

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")