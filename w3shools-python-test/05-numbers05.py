# Demo Python Numbers - Type Conversion
'''
Type Conversion

You can convert from one type to another with the int(), float(), and complex() methods:

* float()
* int()
* complex()

Note: You cannot convert complex numbers into another number type.

'''

# Convert from one type to another:

x = 1   # int
y = 2.8 # float
z = 1j  # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))