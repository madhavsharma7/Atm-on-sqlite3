from tkinter import*
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image

win=Tk()
#win.config(bg="grey")
win.geometry("470x350")
win.title("Welcome to the Account Creation Page")
load=Image.open('ne.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)


def new():
    a=num1.get()
    b=num2.get()
    c=num3.get()
    d=num4.get()
    atmtype="Account Created"
    try:
        conn = sqlite3.connect(database=r'bank.db')
        mydb=conn.cursor()
        mydb.execute("insert into type(card_number,amount,type) values ('"+a+"','"+c+"','"+atmtype+"')")
        mydb.execute("insert into deposit(card_number,pin,amount,contact) values('"+a+"','"+b+"','"+c+"','"+d+"')")
        conn.commit()
        messagebox.showinfo("Message","Account Created!!")
    except:
        conn.rollback()
        messagebox.showinfo("Messge","Account Not Created")
    conn.close()

lb=Label(win,text="Enter_Card_Number",font=20).grid(row=0,column=0,padx=10,pady=10)
lb2=Label(win,text="Enter_Pin",font=20).grid(row=1,column=0,padx=10,pady=10)
lb3=Label(win,text="Enter_Amount",font=20).grid(row=3,column=0,padx=10,pady=10)
lb4=Label(win,text="contact",font=20).grid(row=4,column=0,padx=10,pady=10)
num1=StringVar()
tx=Entry(win,font=20,textvariable=num1).grid(row=0,column=2,padx=20,pady=10)
num2=StringVar()
tx2=Entry(win,font=20,textvariable=num2).grid(row=1,column=2,padx=20,pady=10)
num3=StringVar()
tx3=Entry(win,font=20,textvariable=num3).grid(row=3,column=2,padx=20,pady=10)
num4=StringVar()
tx4=Entry(win,font=20,textvariable=num4).grid(row=4,column=2,padx=20,pady=10)

btn=Button(win,text="Submit",command=new,font=20,bd=10,relief="raised").place(x=180,y=240)

win.mainloop()
