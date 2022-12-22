# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_dictionaries_nested.asp

# Demo Nested Dictionaries
'''
Python Dictionaries - Nested Dictionaries


Nested Dictionaries

A dictionary can contain dictionaries, this is called nested dictionaries.
'''
# Create a dictionary that contain three dictionaries:
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
print('my family: ', myfamily)


'''

Or, if you want to add three dictionaries into a new dictionary.
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

myfamily2 = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
} 

print('my family (other way): ', myfamily2)
