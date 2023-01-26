'''
Python MySQL Create Database

Creating a Database
To create a database in MySQL, use the "CREATE DATABASE" statement.


Check if Database Exists
You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement,
or you can try to access the database when making the connection.

'''
import mysql.connector

db="mydatabase1"

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="userdemo",
        password="123",
        database=db
    )
    print("conexión a", db, "OK")
except mysql.connector.errors.ProgrammingError:
    print("1049 (42000): Unknown database ", db)

# If this page is executed with no error, the database "mydatabase1" exists in your system