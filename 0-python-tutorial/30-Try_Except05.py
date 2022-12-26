# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_try_except.asp

# Demo Python Try Except - Finally
'''
Python Try Except - Finally (part 2)


The "finally" block, if specified, will be executed regardless if the "try" block raises an error or not.

This can be useful to close objects and clean up resources.

'''
# The try block will raise an error when trying to write to a read-only file:
# NOTA: VERIFICAR QUE ESTA OCURRIENDO CON EL ARCHIVO
try:
    f = open("files/demofile2.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening to the file")

# The program can continue, without leaving the file object open
