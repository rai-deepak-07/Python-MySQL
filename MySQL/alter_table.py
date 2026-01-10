#Alter the exists table and add new column.

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

alter_table = "ALTER TABLE "+table_name+" ADD COLUMN email Varchar(30)"

mycursor.execute(alter_table)