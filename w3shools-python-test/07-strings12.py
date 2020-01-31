# Demo Python Strings - Escape Character
'''
Escape Character

To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

Example with Error:
    txt = "We are the so-called "Vikings" from the north." 

To fix this problem, use the escape character \"

'''

# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

# Example of Single Quote
txt2 = 'It\'s alright.'
print(txt2) 

# Example of Backslash
txt3 = "This will insert one \\ (backslash)."
print(txt3) 

# Example of New Line
txt4 = "Hello\nWorld!"
print(txt4) 

# Example of Carriage Return
txt5 = "Hello\rWorld!"
print(txt5) 

# Example of Tab
txt6 = "Hello\tWorld!"
print(txt6) 

# Example of Backspace
txt7 = "Hello \bWorld!"     # This example erases one character (backspace)
print(txt7) 

# Example of Octal value
txt8 = "\110\145\154\154\157"    # A backslash followed by three integers will result in a octal value
print('Example of Octal value:')
print(txt8) 

# Example of Hex value
txt9 = "\x48\x65\x6c\x6c\x6f"    # A backslash followed by an 'x' and a hex number represents a hex value
print('Example of Hex value:')
print(txt9)