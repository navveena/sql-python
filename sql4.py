import mysql.connector
con1=mysql.connector.connect(host="localhost",user="root",password="root",database="pythondatanew")
if con1.is_connected()==False:
    print("database not connected")

cursor=con1.cursor()
cursor.execute("select * from login")
data=cursor.fetchall()

for row in data:
    print(row)