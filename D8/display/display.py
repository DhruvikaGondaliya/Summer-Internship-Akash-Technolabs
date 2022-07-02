import mysql.connector

conn = mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="mydb"
)

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM tbl_student")
#To get only first row
#myresult = mycursor.fetchone()
#print(myresult)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
