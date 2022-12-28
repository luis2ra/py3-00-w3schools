# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_math.asp

# Demo Python Math
'''
Python Math - The Math Module


Python has also a built-in module called "math", which extends the list of mathematical functions.

To use it, you must import the math module:

import math


When you have imported the "math" module, you can start using methods and constants of the module.

The math.sqrt() method for example, returns the square root of a number.

The math.ceil() method rounds a number upwards to its nearest integer, and 
the math.floor() method rounds a number downwards to its nearest integer, and returns the result.

The math.pi constant, returns the value of PI (3.14...).

'''
import math


x = math.sqrt(64)  # The math.sqrt() method returns the square root of a number

print(x)


y = math.ceil(1.4)  # The math.ceil() method rounds a number upwards to its nearest integer
z = math.floor(1.4)  # the math.floor() method rounds a number downwards to its nearest integer

print(y) # returns 2
print(z) # returns 1


number_pi = math.pi  # The math.pi constant, returns the value of PI (3.14...)

print(number_pi)
