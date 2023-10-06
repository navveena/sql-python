import mysql.connector
con1=mysql.connector.connect(host="localhost",user="root",password="root",database="pythondatanew")


cur=con1.cursor()
sql="insert into login(name,id) values(%s,%s)"

val=("arthy",1)

try:

    cur.execute(sql,val)
    con1.commit()
    

except:
    con1.rollback()
print(cur.rowcount,"record inserted!")
con1.close()
