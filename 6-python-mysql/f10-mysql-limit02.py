'''
Python MySQL Limit


Limit the Result

You can limit the number of records returned from the query, by using the "LIMIT" statement:


Start From Another Position

If you want to return five records, starting from the third record, you can use the "OFFSET" keyword.

'''
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="userdemo",
    password="123",
    database="mydatabase1"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)