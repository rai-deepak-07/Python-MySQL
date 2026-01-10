# Update table record using prevent SQL injection.

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

#Create query to update record using parameterized query to prevent SQL injection
qry = "Update " + table_name + " Set name = %s Where st_id = %s"
val = ('Mohit Verma','4')

mycursor.execute(qry, val)
mydb.commit()

print(mycursor.rowcount," record(s) affected successfully...")