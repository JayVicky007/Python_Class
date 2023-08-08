import mysql.connector as sql

db = sql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "Attendancemanager"
)

cursor = db.cursor()

# cursor.execute("CREATE DATABASE Attendancemanager")
cursor.execute("USE Attendancemanager")
# cursor.execute("CREATE TABLE user (id INT PRIMARY KEY AUTO_INCREMENT, first_name varchar(25) NOT NULL, last_name VARCHAR (25), number INT)")
# cursor.execute("INSERT INTO user (first_name, last_name, number) VALUES ('Jules', 'Hangar', '1')")
# db.commit()
# cursor.execute("UPDATE user SET first_name = 'Rose', last_name = 'Parker', number = '4' WHERE id = '1' ")
cursor.execute("SELECT * FROM user")

data = cursor.fetchall()

print(data)

