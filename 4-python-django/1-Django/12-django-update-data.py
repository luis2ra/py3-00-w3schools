# @author: https://github.com/luis2ra from https://www.w3schools.com/django/django_update_data.php

'''
Django Update Data


Update Records

To update records that are already in the database, we first have to get the record we want to update:

>>> from members.models import Member
>>> x = Member.objects.all()[4]

x will now represent the member at index 4, which is "Carlos Duran", but to make sure, let us see if that is correct:

>>> x.firstname
'Carlos'

Now we can change the values of this record:

>>> x.firstname = "Carlos Eduardo"
>>> x.save()

Execute this command to see if the Member table got updated:

>>> Member.objects.all().values()

'''
print("Django Update Data")
