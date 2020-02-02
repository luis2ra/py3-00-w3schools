# Demo Python Dictionaries - Dictionary
'''
Nested Dictionaries

A dictionary can also contain many dictionaries, this is called nested dictionaries.

Or, if you want to nest three dictionaries that already exists as dictionaries.

'''

# Create three dictionaries, than create one dictionary that will contain the other three dictionaries:
child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
} 

print(myfamily)