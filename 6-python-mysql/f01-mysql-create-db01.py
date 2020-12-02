'''
Python MySQL Create Database

Creating a Database
To create a database in MySQL, use the "CREATE DATABASE" statement.


Check if Database Exists
You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement,
or you can try to access the database when making the connection.

'''
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="userdemo",
    password="123"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase1")

# If the above code was executed with no errors, you have successfully created a database.