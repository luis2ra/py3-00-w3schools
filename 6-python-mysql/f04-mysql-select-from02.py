'''
Python MySQL Select From


Select From a Table

To select from a table in MySQL, use the "SELECT" statement.

Note: We use the fetchall() method, which fetches all rows from the last executed statement.


Selecting Columns

To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s).


Using the fetchone() Method

If you are only interested in one row, you can use the fetchone() method.

The fetchone() method will return the first row of the result:

'''
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="userdemo",
    password="123",
    database="mydatabase1"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)