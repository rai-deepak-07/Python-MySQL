#Select the limited record using LIMIT from another position.

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
limit = '3'
offset = '2'
qry = "Select *from "+table_name+" LIMIT "+limit+" OFFSET "+offset

mycursor.execute(qry)
result = mycursor.fetchall()

for i in result:
    print(i)