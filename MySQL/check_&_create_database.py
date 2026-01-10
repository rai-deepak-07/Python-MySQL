#Check database exists or not, if database not exists then create database. 

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="rai_deepak_07",
    password="#MySQL@2003"
)

mycursor = mydb.cursor()
db_name = "student_management"
check_database = False

show_db = "Show Databases"
mycursor.execute(show_db)
create_db = "Create Database " + db_name

for i in mycursor:
    if(i[0]==db_name):
        check_database = True

if (check_database==True):
    print("Database Already Exist...")
else:
    mycursor.execute(create_db)
    print("Database Created Successfully...")