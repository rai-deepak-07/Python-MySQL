#This code will be use to show all the existing database name.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="rai_deepak_07",
    password="#MySQL@2003"
)

mycursor = mydb.cursor()
sql = "show databases"
mycursor.execute(sql)

for i in mycursor:
    print(i)