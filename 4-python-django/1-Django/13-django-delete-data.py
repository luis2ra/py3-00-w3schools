# @author: https://github.com/luis2ra from https://www.w3schools.com/django/django_delete_data.php

'''
Django Delete Data


Delete Records

To delete a record in a table, start by getting the record you want to delete:

>>> from members.models import Member
>>> x = Member.objects.all()[5]

Now we can delete the record:

>>> x.delete()
(1, {'members.Member': 1})

'''
print("Django Delete Data")
