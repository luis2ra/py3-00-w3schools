# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_conditions.asp

# Demo Python If ... Else - Short Hand If ... Else
'''
Short Hand If ... Else

You can also have multiple else statements on the same line.

'''
# One line if else statement, with 3 conditions:
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")


'''
Reescribiendo la expresion condicional anidada
'''
if a > b:
    print("A")
else:
    if a == b:
        print("=")
    else:
        print("B")
