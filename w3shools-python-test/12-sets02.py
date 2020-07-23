# Demo Python Sets
'''
Access Items

You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

'''

# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


# Check if "banana" is present in the set:
print("banana" in thisset)


