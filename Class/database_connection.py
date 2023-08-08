import mysql.connector as sql

db = sql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "Attendance"
)

cursor = db.cursor()

cursor.execute("DELETE from student where ID = 5")
db.commit() # use this whenever you're altering the database
cursor.execute("SELECT * FROM student")
data = cursor.fetchall()
print(data)
