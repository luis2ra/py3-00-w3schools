# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_for_loops.asp

# Demo Python For Loops - Else in For Loop
'''
Else in For Loop

The "else" keyword in a "for" loop specifies a block of code to be executed when the loop is finished:

'''
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
    print(x)
else:
    print("Finally finished!")


'''
Note: The else block will NOT be executed if the loop is stopped by a break statement.

'''
# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")
