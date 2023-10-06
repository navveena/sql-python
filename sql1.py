import mysql.connector
con1=mysql.connector.connect(host="localhost",user="root",password="root")
print("python with mysql connected successfully")
print(con1)

cur=con1.cursor()

try:
    dbs=cur.execute("show databases")
except:
    con1.rollback()

    
for x in cur:
    print(x)


cur=con1.cursor()

try:
    cur.execute("create database pythondatanew")
    dbd=cur.execute("show databases")
except:
    con1.rollback()

    
for x in cur:
    print(x)
