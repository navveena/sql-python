from tkinter.ttk import*
from tkinter import*
import mysql.connector
from tkinter import messagebox
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    databse="naveenaaa"
)
mycursor=mydb.cursor()
root=Tk()
root.title("Student Data")
root.geometry("1200*700")

label12=Label(root).grid(row=8,column=5)
label1=Label(root,text="RollNo",width=20,height=2,bg="pink").grid(row=0,column=0)
label2=Label(root,text="First_Name",width=20,height=2,bg="pink").grid(row=1,column=0)
label3=Label(root,text="Last_Name",width=20,height=2,bg="pink").grid(row=2,column=0)
label4=Label(root,text="Phone_Number",width=20,height=2,bg="pink").grid(row=3,column=0)
label5=Label(root,text="City",width=20,height=2,bg="pink").grid(row=4,column=0)
label6=Label(root,text="State",width=20,height=2,bg="pink").grid(row=5,column=0)
label7=Label(root,text="Age",width=20,height=2,bg="pink").grid(row=6,column=0)
label8=Label(root,width=10,height=2).grid(row=7,column=2)
label9=Label(root,width=10,height=2).grid(row=7,column=4)
label10=Label(root,width=10,height=2).grid(row=7,column=6)
label11=Label(root,width=10,height=2).grid(row=7,column=8)
e1=Entry(root,width=30,borderwidth=8)
e1.grid(row=0,column=1)
e2=Entry(root,width=30,borderwidth=8)
e2.grid(row=1,column=1)
e3=Entry(root,width=30,borderwidth=8)
e3.grid(row=2,column=1)
e4=Entry(root,width=30,borderwidth=8)
e4.grid(row=3,column=1)
e5=Entry(root,width=30,borderwidth=8)
e5.grid(row=4,column=1)
e6=Entry(root,width=30,borderwidth=8)
e6.grid(row=5,column=1)
e7=Entry(root,width=30,borderwidth=8)
e7.grid(row=6,column=1)
def Register():
    RollNo=e1.get()
    dbRollNo=""
    Select="select RollNo from student where RollNo='%s'"%(RollNO)
    mycursor.execute(Select)
    result=mycursor.fetchall()
    for i in result:
        dbRollNo=i[0]
    if(RollNo==dbRollNo):
        messagebox.askokcancel("Information","Record Already exists")
    else :
        Insert="Insert into student(RollNo,First_Name,Last_Name,Phone_Number,City,State,Age)" values("")
        First_Name=e2.get()
        Last_Name=e3.get()
        Phone_Number=e4.get()
        City=e5.get()
        State=e6.get()
        Age=e7.get()
        if(First_Name !="" and Last_Name !="" and Phone_Number !="" and City !="" and State != "" and Age !=""):
           value=(RollNo,First_Name,Last_Name,Phone_Number,City,State,Age)
           mycursor.execute(Insert,Value)
           mydb.commit()
           messagebox.askokcancel("Information","Record inserted")
           
           e1.delete(0,END)
           e2.delete(0,END)
           e3.delete(0,END)
           e4.delete(0,END)
           e5.delete(0,END)
           e6.delete(0,END)
           e7.delete(0,END)
        else:
            if (First_Name=="" and Last_Name =="" and Phone_Number =="" and City =="" and State =="" and Age ==""):
                messagebox.askokcancel("Information","New Entery Fill  All Details")
            else:
                messagebox.askokcancel("Information","Some fields left blank")
    def ShowRecord():
        RollNo=e1.get()
        dbRollNo=""
        Select="select RollNo from student where RollNo='%s'"%(RollNo)
        mycursor.execute(Select)
        result1=mycursor.fetchall()
        for i in result1:
            dbRollNo=i[0]
        Select1="select First_Name,Last_Name,Phone_Number,City,State,Age from student where RollNo='%s'"

    def Delete():
        RollNo=e1.get()
        Delete="delete from student where RollNo ='s'"%(RollNo)
        mycursor.execute(Delete)
        mydb.commit()
        messagebox.showinfo("Information","Record Deleted")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
    def Update():
        RollNo=e1.get()
        First_Name=e2.get()
        Last_Name=e3.get()
        Phone_Number=e4.get()
        
        
    

