# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_try_except.asp

# Demo Python Try Except - Finally
'''
Python Try Except - Finally (part 1)


The "finally" block, if specified, will be executed regardless if the "try" block raises an error or not.

'''
# The "finally" block gets executed no matter if the "try" block raises any errors or not:
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
