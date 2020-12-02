# Demo Python Strings - Check String
'''
Check String

To check if a certain phrase or character is present in a string, we can use the keywords 'in'.


Check if NOT

To check if a certain phrase or character is NOT present in a string, we can use the keyword 'not in'.

'''

# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("original: ", txt)
x = "free" in txt
print(x)

# Print only if "free" is present:
txt2 = "The rain in Spain stays mainly in the plain"
print("original: ", txt2)
if "rain" in txt2:
    print("Yes, 'rain' is present in the text.")

# Check if "expensive" is NOT present in the following text:
txt3 = "The life is beautiful!"
print("original: ", txt3)
print("expensive" not in txt3)

# print only if "expensive" is NOT present:
txt4 = "You are a wild flower!"
print("original: ", txt4)
if "beautiful" not in txt4:
  print("Yes, 'beautiful' is NOT present.")
