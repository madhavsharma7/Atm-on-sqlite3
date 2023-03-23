from tkinter import*
import sqlite3
import os
from tkinter import messagebox
from PIL import ImageTk, Image

win=Tk()
win.geometry("400x400")
win.resizable(False,False)
win.title("Welcome to Sign Up")
load=Image.open('up.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)

def insert():
    a=str(num1.get())
    b=str(num2.get())
    c=str(num3.get())
    d=str(num4.get())
    try:    
        conn = sqlite3.connect(database=r'bank.db')
        mydb=conn.cursor()
        mydb.execute("insert into login(first_name,last_name,username,password) values('"+a+"','"+b+"','"+c+"','"+d+"')")
        conn.commit()
        messagebox.showinfo("Message","Account Created!!")
    except:
        conn.rollback()
        messagebox.showerror("Messge","Check Details")
    conn.close()
    
frame=Frame(win,bd=10,relief="raised",width=400,height=50).grid(row=0)
lb=Label(frame,font=('arial',15,'bold'),text="SIGN UP").grid(row=0)

lb=Label(win,font=('arial',10,'bold'),text="First_name",width=15).place(x=20,y=100)
lb2=Label(win,font=('arial',10,'bold'),text="Last_name",width=15).place(x=20,y=150)
lb3=Label(win,font=('arial',10,'bold'),text="username",width=15).place(x=20,y=200)
lb4=Label(win,font=('arial',10,'bold'),text="password",width=15).place(x=20,y=250)

num1=StringVar()
tx=Entry(win,width=30,textvariable=num1).place(x=180,y=100)
num2=StringVar()
tx2=Entry(win,width=30,textvariable=num2).place(x=180,y=150)
num3=StringVar()
tx3=Entry(win,width=30,textvariable=num3).place(x=180,y=200)
num4=StringVar()
tx4=Entry(win,width=30,textvariable=num4).place(x=180,y=250)

btn=Button(win,text="Submit",font=('arial',10,'bold'),command=insert,width=15,bd=8,relief="raised").place(x=120,y=320)
win.mainloop()
