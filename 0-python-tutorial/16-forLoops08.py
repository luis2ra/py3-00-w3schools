# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_for_loops.asp

# Demo Python For Loops - The range() Function
'''
The range() Function - Part 3

The range() function defaults to increment the sequence by 1, however it is 
possible to specify the increment value by adding a third parameter: range(2, 30, 3).

'''
# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print(x)

print()

# Decrement the sequence with 2 (default is 1):
for x in range(30, 0, -2):
    print(x)
