'''
Python MySQL Create Table


Creating a Table

To create a table in MySQL, use the "CREATE TABLE" statement.
Make sure you define the name of the database when you create the connection


Check if Table Exists

You can check if a table exist by listing all tables in your database with the "SHOW TABLES" statement.


Primary Key

When creating a table, you should also create a column with a unique key for each record.
This can be done by defining a PRIMARY KEY.
We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1, and increased by one for each record.

'''
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="userdemo",
    password="123",
    database="mydatabase1"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#If this page is executed with no error, you have successfully created a table named "customers".