#Delete Record in Table

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

#Create query to delete record using parameterized query to prevent SQL injection
qry  = "Delete from "+table_name+" Where email = %s"
email = ('rai@gmail.com',)

mycursor.execute(qry, email)
mydb.commit()

print(mycursor.rowcount," record(s) deleted...")