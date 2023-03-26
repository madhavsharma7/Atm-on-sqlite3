from tkinter import*
import os
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image

win=Tk()
win.geometry("1150x600")
win.resizable(False,False)
win.title("Welcome to the Statement")
load=Image.open('mini.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)

def mini():
   #a=st.get()
    win2=Frame(win).place(x=80,y=200)
    conn = sqlite3.connect(database=r'bank.db')
    mydb=conn.cursor()
    mydb.execute("select * from type where card_number='"+st.get()+"'")
    result=mydb.fetchall()
    count=mydb.rowcount
    num=10

    tx=Text(win2,font="arial",width=60,height=count+15)
    tx.insert(END,"\t\t\tHMB Bank Statement")
    tx.insert(END,"\n\tCard_Number\t\tAmount\t\tType")
    tx.place(x=num,y=200)
    for i in result:
        tx.insert(END,"\t\t\n\t{0}\t\t{1}\t\t{2}".format(i[0],i[1],i[2]))
        num+=1
    
lb=Label(win,text="Enter Card Number",font=35,width=28).place(x=10,y=10)

st=StringVar()
tx=Entry(win,width=20,font=30,textvariable=st).place(x=330,y=10)
btn=Button(win,command=mini,text="Show",width=20,font=30,bd=10,relief="raised").place(x=300,y=90)

win.mainloop()
