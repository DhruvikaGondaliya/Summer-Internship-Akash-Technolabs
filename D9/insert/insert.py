import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "myDemo"
)

mycursor = conn.cursor()

sql = "INSERT INTO tbl_user(user_firstname, user_lastname, user_city, user_email, user_password) VALUES ('Dhruvika', 'Gondaliya', 'Ahemdabad', 'd@gmail.com', '1234cde')"

mycursor.execute(sql)
mycursor.execute("INSERT INTO tbl_user(user_firstname, user_lastname, user_city, user_email, user_password) VALUES ('Rajvi', 'Desai', 'Vadodra' , 'r@gmail.com', 'nhy7894')")
mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "row inserted.")
