from tkinter import*
from tkinter import messagebox
import sqlite3
import os
from PIL import ImageTk, Image

win=Tk()
win.geometry("520x300")
win.title("Welcome to the Balance")
win.resizable(False,False)
load=Image.open('cash.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)

def depo():
   #a=num1.get()
   #b=num2.get()
    conn = sqlite3.connect(database=r'bank.db')
    mydb=conn.cursor()
    mydb.execute("select amount from deposit where card_number='"+num1.get()+"'")
    result=mydb.fetchall()
    count=mydb.rowcount
    print(result)
    print(count)
    if result:
        messagebox.showinfo("Balance",result)
    else:
        messagebox.showerror("Error","INVALID Card Number and Pin")

lb=Label(win,text="Enter Card Number",width=20,font=10).grid(row=0,column=0,padx=20,pady=20)
lb2=Label(win,text="Enter Pin", width=20,font=10).grid(row=3,column=0,padx=20,pady=20)

num1=StringVar()
tx=Entry(win,font=10,textvariable=num1).grid(row=0,column=1)
num2=StringVar()
tx2=Entry(win,font=10,textvariable=num2).grid(row=3,column=1)

btn=Button(win,text="Show",command=depo,font=10,width=10,bd=10,relief="raised").place(x=200,y=200)
            
win.mainloop()
