# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_booleans.asp

# Demo Python Booleans - Some Values are False
'''
Some Values are False

One more value, or object in this case, evaluates to False, and that is if you have an 
object that is made from a class with a __len__ function that returns 0 or False.

'''
# definición de una clase con una longitud cero
class myclass():
    def __len__(self):
        return 0

# definición de un objeto
myobj = myclass()
print(bool(myobj))
