# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_while_loops.asp

# Demo Python While Loops - The break Statement
'''
The break Statement

With the "break" statement we can stop the loop even if the while condition is true.

'''
# Exit the loop when i is 3:
i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
