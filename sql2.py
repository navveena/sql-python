import mysql.connector
con1=mysql.connector.connect(host="localhost",user="root",password="root",database="pythondatanew")


cur=con1.cursor()

try:
    
    dbs=cur.execute("create table login(id int,name char(20)")
except:
    con1.rollback()
print("table created")
