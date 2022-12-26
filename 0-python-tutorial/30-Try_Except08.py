# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_try_except.asp

# Demo Python Try Except - Raise an exception
'''
Python Try Except - Raise an exception


Demo Luis para validar un codigo de error en proyecto Blooz

'''

while True:
    try:
        HOST = input('Enter host IP: ')
        if len(HOST.split(".")) != 4:
            raise ValueError("error 1")
        for char in HOST:
            if char not in "0123456789.":
                raise ValueError("error 2")
    except ValueError:
        # print('Error. That is not a valid IP address.')
        continue
    else:
        break

# HOST = input('Enter host IP: ')
# if len(HOST.split(".")) != 4:
#     raise ValueError(_("Superuser must have is_staff=True."))
# for char in HOST:
#     if char not in "0123456789.":
#         raise ValueError("Superuser must have is_superuser=True.")
