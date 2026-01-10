#Insert single data into the table

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="rai_deepak_07",
    password="#MySQL@2003"
)

mycursor = mydb.cursor()
sql = "use student_management"
mycursor.execute(sql)

#Insert single data into login table
insert_data = "Insert Into login Values(%s, %s)"
data_val = ("rai_deepak_07","Rai@123")

mycursor.execute(insert_data, data_val)
mydb.commit()
print(mycursor.rowcount, "record inserted...")