import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydb"
)

mycourser = conn.cursor()

sql = "DELETE FROM tbl_student WHERE st_id = 4"

mycourser.execute(sql)

conn.commit()

print(mycourser.rowcount, "row deleted.")