# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_sets_join.asp

# Demo Join Sets
'''
Python Sets - Join Sets


Join Two Sets

There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets, or 
the update() method that inserts all the items from one set into another.

Note: Both union() and update() will exclude any duplicate items.

'''
# The union() method returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 


# The update() method inserts the items in set5 into set4:
set4 = {"x", "y", "z"}
set5 = {7, 8, 9}

set4.update(set5)
print(set4)


'''
Keep ONLY the Duplicates

The intersection_update() method will keep only the items that are present in both sets.

The intersection() method will return a new set, that only contains the items that are present in both sets.

'''
# Keep the items that exist in both set x, and set y:
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}

x1.intersection_update(y1)

print(x1)

# Return a set that contains the items that exist in both set x, and set y:
xx = {"apple", "banana", "cherry"}
yy = {"google", "microsoft", "apple"}
z = xx.intersection(yy) 

print(z)


'''
Keep All, But NOT the Duplicates

The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

'''
# Keep the items that are not present in both sets:
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}

x2.symmetric_difference_update(y2)

print(x2)


# Return a set that contains all items from both sets, except items that are present in both:
x3 = {"apple", "banana", "cherry"}
y3 = {"google", "microsoft", "apple"}

z2 = x3.symmetric_difference(y3)

print(z2)
