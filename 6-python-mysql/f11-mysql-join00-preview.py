'''
Python MySQL Join

Data configuration in BD for the demo

'''
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="userdemo",
    password="123",
    database="mydatabase1"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav INT)")

mycursor.execute("CREATE TABLE products (id INT, name VARCHAR(255))")

sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
val = [
 ('John', 154),
 ('Peter', 154),
 ('Amy', 155),
 ('Hannah', None ),
 ('Michael', None )
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record was inserted.")


sql2 = "INSERT INTO products (id, name) VALUES (%s, %s)"
val2 = [
 (154, 'Chocolate Heaven'),
 (155, 'Tasty Lemons'),
 (156, 'Vanilla Dreams'),
]

mycursor.executemany(sql2, val2)

mydb.commit()

print(mycursor.rowcount, "record was inserted.")
