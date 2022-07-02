import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "myDemo"
)

mycursor = conn.cursor()

sql = "UPDATE tbl_user SET user_firstname = 'Charmee' WHERE user_id = 3"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "row updated.")