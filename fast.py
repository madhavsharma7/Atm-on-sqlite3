from tkinter import*
from tkinter import messagebox
import sqlite3
import os
from PIL import ImageTk, Image

win=Tk()
win.geometry("500x380")
win.title("Welcome to the fast cash")
win.resizable(False, False)
load=Image.open('fa.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)



def cash1():
    a=num1.get()
    b=num2.get()
    amount='2000'
    atmtype="Fast Cash"
    try:
        conn = sqlite3.connect(database=r'bank.db')
        mydb=conn.cursor()
        mydb.execute("select * from depos where Enter_Card_Number='"+a+"'")
        mydb.execute("insert into type(Enter_Card_Number,Enter_Amount,type) values ('"+a+"','"+amount+"','"+atmtype+"')")
        mydb.execute("update depos set Enter_Amount=Enter_Amount - 100 where Enter_Pin='"+b+"'")
        conn.commit()
        result=mydb.fetchall()
        count=mydb.rowcount
        print(result)
        print(count)
        if count>0:
            messagebox.showinfo("Message","Rs 2000 Withdrawed")
        else:
            messagebox.showerror("Message","Failed")
    except:
        conn.rollback()
        messagebox.showinfo("Message","Not Withdrawed")
    conn.close()

def cash2():
    a=num1.get()
    b=num2.get()
    amount='5000'
    atmtype="Fast Cash"
    try:
        conn = sqlite3.connect(database=r'bank.db')
        mydb.execute("select * from depos where Enter_Card_Number='"+a+"'")
        mydb.execute("insert into type(Enter_Card_Number,Enter_Amount,type) values ('"+a+"','"+amount+"','"+atmtype+"')")
        mydb.execute("update depos set Enter_Amount = Enter_Amount - 200 where Enter_Pin='"+b+"'")
        conn.commit()
        result=mydb.fetchall()
        count=mydb.rowcount
        print(result)
        print(count)
        if count>0:
            messagebox.showinfo("Message","Rs 5000 Withdrawed")
        else:
            messagebox.showerror("Message","Failed")
    except:
        conn.rollback()
        messagebox.showinfo("Message","Not Withdrawed")
    conn.close()
    
def cash3():
    a=num1.get()
    b=num2.get()
    amount='7000'
    atmtype="Fast Cash"
    try:
        conn = sqlite3.connect(database=r'bank.db')
        mydb.execute("select * from depos where Enter_Card_Number='"+a+"'")
        mydb.execute("insert into type(Enter_Card_Number,Enter_Amount,type) values ('"+a+"','"+amount+"','"+atmtype+"')")
        mydb.execute("update depos set Enter_Amount = Enter_Amount - 500 where Enter_Pin='"+b+"'")
        conn.commit()
        result=mydb.fetchall()
        count=mydb.rowcount
        print(result)
        print(count)
        if count>0:
            messagebox.showinfo("Message","Rs 7000 Withdrawed")
        else:
            messagebox.showerror("Message","Failed")
    except:
        conn.rollback()
        messagebox.showinfo("Message","Not Withdrawed")
    conn.close()

def cash4():
    a=num1.get()
    b=num2.get()
    amount='10000'
    atmtype="Fast Cash"
    try:
        conn = sqlite3.connect(database=r'bank.db')
        mydb.execute("select * from depos where Enter_Card_Number='"+a+"'")
        mydb.execute("insert into type(Enter_Card_Number,Enter_Amount,type) values ('"+a+"','"+amount+"','"+atmtype+"')")
        mydb.execute("update depos set Enter_Amount = Enter_Amount - 2000 where Enter_Pin='"+b+"'")
        conn.commit()
        result=mydb.fetchall()
        count=mydb.rowcount
        print(result)
        print(count)
        if count>0:
            messagebox.showinfo("Message","Rs 10000 Withdrawed")
        else:
            messagebox.showerror("Message","Faileds")
    except:
        conn.rollback()
        messagebox.showinfo("Message","Not Withdrawed")
    conn.close()


lb=Label(win,text="Enter card number ",font=20,width=20).grid(row=0,column=0,padx=20,pady=20)
lb2=Label(win,text="Enter pin",font=20,width=10).grid(row=1,column=0,padx=20,pady=20)

num1=StringVar()
tx=Entry(win,font=10,width=20,textvariable=num1).grid(row=0,column=1)
num2=StringVar()
tx2=Entry(win,font=10,width=20,textvariable=num2).grid(row=1,column=1)

btn=Button(win,text="100",command=cash1,relief="raised",width=10,bd=10,font=20).place(x=100,y=160)
btn2=Button(win,text="200",command=cash2,relief="raised",width=10,bd=10,font=20).place(x=300,y=160)
btn3=Button(win,text="500",command=cash3,relief="raised",width=10,bd=10,font=20).place(x=100,y=250)
btn4=Button(win,text="2000",command=cash4,relief="raised",width=10,bd=10,font=20).place(x=300,y=250)

win.mainloop()
