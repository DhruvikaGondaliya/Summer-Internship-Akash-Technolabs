import mysql.connector

conn = mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="mydb"
)

mycursor = conn.cursor()

sql = "INSERT INTO tbl_student (st_name, st_email, st_mobile) VALUES ('Zenil', 'z@gmail.com', 7852641078)"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "row inserted.")