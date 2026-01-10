#Get inserted id

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

#Insert single data into registration table
insert_data = "Insert Into "+table_name+" (Name, Address, email) Values(%s, %s, %s)"
data_val = ("Pankaj","Sonipat","pankaj@gmail.com")

mycursor.execute(insert_data, data_val)
mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)