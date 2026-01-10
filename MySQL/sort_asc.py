#Use of ORDER BY keyword to sort the data in Ascending Order.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="rai_deepak_07",
    password="#MySQL@2003"
)

mycursor = mydb.cursor()
sql = "use student_management"
mycursor.execute(sql)
table_name = "registration"
field = "Name"

qry = "Select *From "+table_name+" ORDER BY "+field
mycursor.execute(qry)

myresult = mycursor.fetchall()
for i in myresult:
    print(i)