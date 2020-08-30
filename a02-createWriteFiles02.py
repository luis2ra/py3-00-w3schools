'''

Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content

'''

f = open("files/demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("files/demofile3.txt", "r")
print(f.read())
