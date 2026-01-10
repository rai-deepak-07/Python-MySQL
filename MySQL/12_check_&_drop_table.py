#Drop Only if Exist 

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="rai_deepak_07",
    password="#MySQL@2003"
)

mycursor = mydb.cursor()
sql = "use student_management"
mycursor.execute(sql)
table_name = "login"

qry  = "Drop Table If Exists "+table_name

mycursor.execute(qry)