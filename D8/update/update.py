import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydb"
)

mycursor = conn.cursor()

sql = "UPDATE tbl_student SET st_name = 'Dhruvi' WHERE st_id = 2"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "row updated.")