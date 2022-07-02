import mysql.connector

conn = mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="myDemo"
)

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM tbl_user")

myresult = mycursor.fetchall()

for x in myresult:
     print(x)