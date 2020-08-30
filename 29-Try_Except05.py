# Demo Python Try Except - Finally
'''
Finally

The finally block, if specified, will be executed regardless if the try block raises an error or not.

This can be useful to close objects and clean up resources.
'''

# The try block will raise an error when trying to write to a read-only file:
# NOTA: VERIFICAR QUE ESTA OCURRIENDO CON EL ARCHIVO
try:
    f = open("files/demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

# The program can continue, without leaving the file object open