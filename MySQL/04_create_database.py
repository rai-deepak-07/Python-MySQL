import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="rai_deepak_07",
    password="#MySQL@2003"
)

mycursor = mydb.cursor()
db_name = "student_management"
sql = "Create Database " + db_name
mycursor.execute(sql)