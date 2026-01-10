#Select the limited record using LIMIT keyword.

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
limit = '1'

qry = "Select *from "+table_name+" LIMIT "+limit

mycursor.execute(qry)
result = mycursor.fetchall()

for i in result:
    print(i)