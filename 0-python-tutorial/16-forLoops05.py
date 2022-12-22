# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_for_loops.asp

# Demo Python For Loops - The continue Statement
'''
The continue Statement

With the "continue" statement we can stop the current iteration of the loop, and continue with the next.

'''
# Do not print banana:
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        continue
    print(x)
print("the end...")
