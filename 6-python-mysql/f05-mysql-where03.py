'''
Python MySQL Where


Select With a Filter

When selecting records from a table, you can filter the selection by using the "WHERE" statement.


Wildcard Characters

You can also select the records that starts, includes, or ends with a given letter or phrase.

Use the %  to represent wildcard characters.


Prevent SQL Injection

When query values are provided by the user, you should escape the values.

This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

The mysql.connector module has methods to escape query values.


'''
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="userdemo",
    password="123",
    database="mydatabase1"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

'''
Una forma de combinar mas de un elemento de busqueda
'''
sql = "SELECT * FROM customers WHERE address IN %s"
val = ('Yellow Garden 2', 'Highway 21')

mycursor.execute(sql, val)

myresult = mycursor.fetchall()

print('\n')
for x in myresult:
    print(x)