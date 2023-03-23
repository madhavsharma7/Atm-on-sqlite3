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
    a=num1.get()
    b=num2.get()
    conn = sqlite3.connect(database=r'bank.db')
    mydb.execute("select Enter_Amount from depos where Enter_Card_Number='"+a+"'")
    result=mydb.fetchall()
    count=mydb.rowcount
    print(result)
    print(count)
    if count>0:
          messagebox.showinfo("Balance",result)
    else:
        messagebox.showerror("Balance","INVALID Card Number and PIN")


lb=Label(win,text="Enter_Card_Number",width=20,font=10).grid(row=0,column=0,padx=20,pady=20)
lb2=Label(win,text="Enter_Pin", width=20,font=10).grid(row=3,column=0,padx=20,pady=20)

num1=StringVar()
tx=Entry(win,font=10,textvariable=num1).grid(row=0,column=1)
num2=StringVar()
tx2=Entry(win,font=10,textvariable=num2).grid(row=3,column=1)

btn=Button(win,text="Show",command=depo,font=10,width=10,bd=10,relief="raised").place(x=200,y=200)
             

win.mainloop()
