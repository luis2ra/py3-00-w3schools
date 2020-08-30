# Demo Python Functions - Default Parameter Value
'''
Default Parameter Value

The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value.

'''

# Example:
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()           # Asume el valor por defecto
my_function("Brazil")

