#Create a new table.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="rai_deepak_07",
    password="#MySQL@2003"
)

mycursor = mydb.cursor()
sql = "Use student_management"
mycursor.execute(sql)

create_table = "Create table Login(username Varchar(40), password Varchar(30))"
mycursor.execute(create_table)