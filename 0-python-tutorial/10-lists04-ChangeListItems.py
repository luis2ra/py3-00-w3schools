# Demo Change List Items
'''
List

A list is a collection which is ordered and changeable. Allows duplicate members.


Change Item Value

To change the value of a specific item, refer to the index number:


Change a Range of Item Values

To change the value of items within a specific range, define a list with the new values, 
and refer to the range of index numbers where you want to insert the new values.

If you insert more items than you replace, the new items will be inserted where you specified, and 
the remaining items will move accordingly.

Note: The length of the list will change when the number of items inserted does not match the number of items replaced.


Insert Items

To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index.

'''

# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
list2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list2[1:3] = ["blackcurrant", "watermelon"]
print(list2)


# Change the second value by replacing it with two new values:
list3 = ["apple", "banana", "cherry"]
list3[1:2] = ["blackcurrant", "watermelon"]
print(list3)


# Change the second and third value by replacing it with one value:
list4 = ["apple", "banana", "cherry"]
list4[1:3] = ["watermelon"]
print(list4)


# Insert "watermelon" as the third item:
list5 = ["apple", "banana", "cherry"]
list5.insert(2, "uva")
print(list5)