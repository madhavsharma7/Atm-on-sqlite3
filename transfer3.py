from tkinter import*
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image

win=Tk()
win.geometry("550x500")
win.resizable(False,False)
win.title("Welcome to the transfer")
load=Image.open('tra.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)

def transfer():
   #a=str(num1.get())
   #b=str(num2.get())
   #c=str(num3.get())
   #d=str(num4.get())
   #e=str(num5.get())
    atmtype="Transfer"
    conn = sqlite3.connect(database=r'bank.db')
    mydb=conn.cursor()
    try:
        mydb.execute("insert into type(card_number,amount,type) values ('"+num1.get()+"','"+num3.get()+"','"+atmtype+"')")
        mydb.execute("update deposit set amount = amount - '"+num3.get()+"' where pin='"+num2.get()+"'")
        mydb.execute("insert into bank(card_number_to,pin,amount) values ('"+num4.get()+"','"+num2.get()+"','"+num3.get()+"')")
        conn.commit()
        messagebox.showinfo("Message","Transfed")
    except:
        messagebox.showerror("Error","Check your Details")
    conn.close()

lb=Label(win,text="Enter Card Number From",font=20,width=25).grid(row=0,column=0,padx=20,pady=20)

lb2=Label(win,text="Enter Pin",font=20,width=10).grid(row=1,column=0,padx=20,pady=20)

lb3=Label(win,text="Enter Amount",font=20,width=15).grid(row=2,column=0,padx=20,pady=20)

lb4=Label(win,text="Enter Card Number To",font=20,width=20).grid(row=3,column=0,padx=20,pady=20)

lb5=Label(win,text="Enter IFSC",font=20,width=10).grid(row=4,column=0,padx=20,pady=20)

num1=StringVar()
tx=Entry(win,font=10,width=20,textvariable=num1).grid(row=0,column=1)
num2=StringVar()
tx2=Entry(win,font=10,width=20,textvariable=num2).grid(row=1,column=1)
num3=StringVar()
tx3=Entry(win,font=10,width=20,textvariable=num3).grid(row=2,column=1)
num4=StringVar()
tx4=Entry(win,font=10,width=20,textvariable=num4).grid(row=3,column=1)
num5=StringVar()
tx5=Entry(win,font=10,width=20,textvariable=num5).grid(row=4,column=1)

btn=Button(win,text="Transfer",command=transfer,relief="raised",bd=10,font=20,highlightbackground="blue",highlightthickness=10).place(x=220,y=370)

win.mainloop()
