#Select with a wildcard character. 

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
address = "%De%"

qry = "Select *From "+table_name+" Where Address LIKE '"+address+"'"
mycursor.execute(qry)

myresult = mycursor.fetchall()
for i in myresult:
    print(i)