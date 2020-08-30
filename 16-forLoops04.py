# Demo Python For Loops - The break Statement
'''
The break Statement

With the break statement we can stop the loop before it has looped through all the items.

'''

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        break
    print(x)
print("fin...")