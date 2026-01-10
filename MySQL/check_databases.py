#Check database exists or not.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="rai_deepak_07",
    password="#MySQL@2003"
)

database="rai"
mycursor = mydb.cursor()
sql = "show databases"
mycursor.execute(sql)
check_database_exist = False

for i in mycursor:
    if(i[0]==database):
       check_database_exist=True

if(check_database_exist==True):
    print("Database Found")
else:
    print("Database Not Found")