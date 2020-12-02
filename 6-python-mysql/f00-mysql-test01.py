'''
Python MySQL

* Python can be used in database applications.
* One of the most popular databases is MySQL.


En w3schools usan el módulo: pip install mysql-connector-python

'''
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="userdemo",
    password="123"
)

print(mydb)
