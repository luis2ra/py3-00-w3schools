# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_string_formatting.asp

# Demo Python String Formatting - Named Indexes
'''
Python String Formatting - Named Indexes


You can also use named indexes by entering a name inside the curly brackets {carname}, but 
then you must use names when you pass the parameter values txt.format(carname = "Ford").

'''
# Example
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
