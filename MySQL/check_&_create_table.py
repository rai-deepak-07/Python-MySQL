#Check table exist or not, if table not exists then create a new table.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="rai_deepak_07",
    password="#MySQL@2003"
)

mycursor = mydb.cursor()
sql = "use student_management"
mycursor.execute(sql)

table_name = "login"

show_tables = "Show Tables LIKE '"+table_name+"'"
mycursor.execute(show_tables)

create_table = "Create table Login(username Varchar(30), password Varchar(30))"

result = mycursor.fetchone()
if result:
    print("Table Already Exist...")    
else:
    mycursor.execute(create_table)
    print("Table Created Successfully...")    