# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_for_loops.asp

# Demo Python For Loops - The break Statement
'''
The break Statement

With the "break" statement we can stop the loop before it has looped through all the items.

'''
# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
    if x == "banana":
        break
print("the end...")
