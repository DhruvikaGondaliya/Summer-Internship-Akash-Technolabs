import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "myDemo"
)

mycursor = conn.cursor()

sql = "DELETE FROM tbl_user WHERE user_id = 2"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "row deleted.")