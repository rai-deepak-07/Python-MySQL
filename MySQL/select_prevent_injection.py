#Select with SQL prevent Injection.

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

qry = "Select *From "+table_name+" Where Address = %s"
address = ('Delhi',)
mycursor.execute(qry,address)

myresult = mycursor.fetchall()
for i in myresult:
    print(i)