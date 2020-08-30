# Python File Open

'''
Open a File on the Server

To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file.

'''


f = open("files/demofile.txt", "r")
print(f.read())
f.close()

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
f = open("files/demofile.txt", "r")
print(f.read(5))
f.close()

# Read Lines
# You can return one line by using the readline() method:
f = open("files/demofile.txt", "r")
print(f.readline())
f.close()

# By calling readline() two times, you can read the two first lines:
f = open("files/demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()

# By looping through the lines of the file, you can read the whole file, line by line:
f = open("files/demofile.txt", "r")
for x in f:
    print(x)
f.close()