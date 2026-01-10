#Check table exist or not, if table not exists then create a new table with primary key.

#Check table exist or not, if table not exists then create a new table with primary key.

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

#Check table exist or not query
show_tables = "Show Tables LIKE '"+table_name+"'"
mycursor.execute(show_tables)

#Create table query
create_table = "Create table "+table_name+" (st_id Int Auto_Increment Primary Key, Name Varchar(30), Address Varchar(50))"

result = mycursor.fetchone()
if result:
    print("Table Already Exist...")    
else:
    mycursor.execute(create_table)
    print("Table Created Successfully...")    