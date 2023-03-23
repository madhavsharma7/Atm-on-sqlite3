from tkinter import*
from tkinter import messagebox
import sqlite3
import os
from PIL import ImageTk, Image

win=Tk()
win.geometry("500x520")
win.resizable(False,False)
win.title("Admin Login")
load=Image.open('Design.png')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)

def new():
    os.system("newACC.py")

def id():
        a=us.get()
        b=pas.get()
        conn = sqlite3.connect(database=r'bank.db')
        mydb=conn.cursor()
        try:
            mydb.execute("select * from login where username=? and password =?",(us.get(),pas.get(),))
           
            result=mydb.fetchall()
            count=mydb.rowcount 
            print(result)
            print(count) 
            if result:
                os.system("atmfirst.py")     
            else:
                messagebox.showerror("Message","ENTER CORRECT USERNAME AND PASSWORD")
                    
        except:
            messagebox.showerror("Message","DATABASE NOT CONNECTED")

def fr():
     os.system("forgetpassword.py")

def nw():
     os.system("signup.py")
     
frame=Frame(win,bd=10,relief="raised",width=500,height=50).grid(row=0)
lb=Label(frame,text="HMB NATIONAL BANK",font=40).grid(row=0)
frame2=Frame(win,bd=10,relief="raised",width=400,height=400,bg="black").place(x=50,y=100)

frame3=Frame(win,bd=9,relief="raised",width=400,height=40).place(x=50,y=100)
lb2=Label(frame3,text="ADMIN LOGIN",font=20).place(x=190,y=102)

lb=Label(frame2,text="Username",bg="#97FFFF",font=20,width=10).place(x=100,y=150)
lb2=Label(frame2,text="Password",bg="#97FFFF",font=20,width=10).place(x=100,y=200)

lb3=Label(frame2,text="Forget Password?",bg="#97FFFF",font=20,width=15).place(x=100,y=320)
btn2=Button(frame2,text="CLICK HERE",command=fr,font=10,bd=5,relief="raised").place(x=290,y=310)

lb4=Button(frame2,text="Create Bank Account",command=new,font=10).place(x=145,y=370)

btn4=Button(frame2,text="Sign Up",command=nw,font=10,bd=5,relief="raised").place(x=200,y=420)

us=StringVar()
tx=Entry(frame2,width=25,textvariable=us).place(x=250,y=150)
pas=StringVar()
tx2=Entry(frame2,width=25,textvariable=pas).place(x=250,y=200)

btn=Button(frame2,text="Submit",font=20,bd=5,command=id,relief="raised").place(x=220,y=250)
win.mainloop()
