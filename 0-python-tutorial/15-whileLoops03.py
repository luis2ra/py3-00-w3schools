# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_while_loops.asp

# Demo Python While Loops - The continue Statement
'''
The continue Statement

With the "continue" statement we can stop the current iteration, and continue with the next.

'''
# Continue to the next iteration if i is 3:
i = 0

while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
