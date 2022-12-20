# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_lists_change.asp

# Demo Change List Items
'''
Python Lists - Change List Items

A list is a collection which is ordered and changeable. Allows duplicate members.


Change Item Value

To change the value of a specific item, refer to the index number:
'''
# Change the second item:
list1 = ["apple", "banana", "cherry"]
list1[1] = "blackcurrant"
print('list1: ', list1)


'''
Change a Range of Item Values

To change the value of items within a specific range, define a list with the new values, 
and refer to the range of index numbers where you want to insert the new values:
'''
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
list2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list2[1:3] = ["blackcurrant", "watermelon"]
print('list2: ', list2)


'''
If you insert more items than you replace, the new items will be inserted where you specified, and 
the remaining items will move accordingly:
'''
# Change the second value by replacing it with two new values:
list3 = ["apple", "banana", "cherry"]
list3[1:2] = ["blackcurrant", "watermelon"]
print('list3: ', list3)


'''
Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

If you insert less items than you replace, the new items will be inserted where you specified,
and the remaining items will move accordingly:
'''
# Change the second and third value by replacing it with one value:
list4 = ["apple", "banana", "cherry"]
list4[1:3] = ["watermelon"]
print('list4: ', list4)


'''
Insert Items

To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:
'''
# Insert "watermelon" as the third item:
list5 = ["apple", "banana", "cherry"]
list5.insert(2, "uva")
print('list5: ', list5)
# Note: As a result of the example above, the list will now contain 4 items.
