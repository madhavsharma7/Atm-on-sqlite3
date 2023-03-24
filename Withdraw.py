from tkinter import*
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image

win=Tk()
#win.config(bg="grey")
win.geometry("470x420")
win.title("Welcome to the Withdraw")
win.resizable(False,False)
load=Image.open('wi.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)


def wit():
   #a=num1.get()
   #b=num2.get()
   #c=num3.get()
    atmtype="Withdraw"
    conn = sqlite3.connect(database=r'bank.db')
    mydb=conn.cursor()
    try:
        mydb.execute("insert into type(card_number,amount,type) values ('"+num1.get()+"','"+num3.get()+"','"+atmtype+"')")
        mydb.execute("update deposit set amount = amount - '"+num3.get()+"' where card_number='"+num1.get()+"'")
        conn.commit()
        messagebox.showinfo("Message","Withdraw")
    except:
        messagebox.showerror("Error","There was some error")
    conn.close()    


lb=Label(win,text="Enter Card Number",width=17,font=20).grid(row=0,column=0,padx=10,pady=10)
lb2=Label(win,text="Enter Pin",width=15,font=20).grid(row=1,column=0,padx=10,pady=10)
lb3=Label(win,text="Enter Amount",width=15,font=20).grid(row=3,column=0,padx=10,pady=10)

num1=StringVar()
tx=Entry(win,font=20,textvariable=num1).grid(row=0,column=2,padx=20,pady=10)
num2=StringVar()
tx2=Entry(win,font=20,textvariable=num2).grid(row=1,column=2,padx=20,pady=10)
num3=StringVar()
tx3=Entry(win,font=20,textvariable=num3).grid(row=3,column=2,padx=20,pady=10)

btn=Button(win,text="Withdraw",command=wit,font=20,bd=10,relief="raised").place(x=180,y=280)

win.mainloop()
