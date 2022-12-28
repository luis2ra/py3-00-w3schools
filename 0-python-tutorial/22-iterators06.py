# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_iterators.asp

# Demo Python Iterators - StopIteration
'''
Python Iterators - StopIteration

The example preview would continue forever if you had enough next() statements, or if it was used in a "for" loop.

To prevent the iteration to go on forever, we can use the "StopIteration" statement.

In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times.

'''
# Stop after 10 iterations:
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
