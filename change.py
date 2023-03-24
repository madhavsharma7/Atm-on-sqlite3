from tkinter import*
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image

win=Tk()
win.geometry("510x420")
win.title("Welcome to the Change pin")
win.resizable(False,False)

load=Image.open('ch.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)

def insert():
   #a=str(num.get())
   #b=str(num1.get())
   #c=str(num2.get())
   #d=str(num3.get())
    conn = sqlite3.connect(database=r'bank.db')
    mydb=conn.cursor()
    try:
        if(num2.get()==num3.get()):
            mydb.execute("update deposit set pin='"+num2.get()+"' where pin='"+num1.get()+"'")
            conn.commit()
            messagebox.showinfo("Message","Pin Updated")
        else:
            messagebox.showinfo("Message","Pin Not Match")
    except:
        messagebox.showwarning("Message","There was some Error")
    conn.close()


lb=Label(win,text="Enter Card Number ",font=20,width=20).grid(row=0,column=0,padx=20,pady=20)

lb2=Label(win,text="Enter Old Pin",font=20,width=12).grid(row=1,column=0,padx=20,pady=20)

lb3=Label(win,text="Enter New Pin",font=20,width=15).grid(row=2,column=0,padx=20,pady=20)

lb4=Label(win,text="Re_enter New Pin",font=20,width=20).grid(row=3,column=0,padx=20,pady=20)

num=StringVar()
tx=Entry(win,font=10,width=20,textvariable=num).grid(row=0,column=1)
num1=StringVar()
tx2=Entry(win,font=10,width=20,textvariable=num1).grid(row=1,column=1)
num2=StringVar()
tx3=Entry(win,font=10,width=20,textvariable=num2).grid(row=2,column=1)
num3=StringVar()
tx4=Entry(win,font=10,width=20,textvariable=num3).grid(row=3,column=1)

btn=Button(win,text="Change",command=insert,relief="raised",bd=10,font=20,highlightbackground="blue",highlightthickness=10).place(x=200,y=310)

win.mainloop()
