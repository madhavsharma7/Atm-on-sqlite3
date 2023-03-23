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
    a=str(num1.get())
    b=str(num2.get())
    c=str(num3.get())
    d=str(num4.get())
    e=str(num5.get())
    atmtype="Transfer"
    
    try:
        conn = sqlite3.connect(database=r'bank.db')
        mydb.execute("insert into type(Enter_Card_Number,Enter_Amount,type) values ('"+a+"','"+c+"','"+atmtype+"')")
        mydb.execute("update depos set Enter_Amount = Enter_Amount - '"+c+"' where Enter_Pin='"+b+"'")
        mydb.execute("insert into bank(Card_Number_To,Enter_Pin,Enter_Amount) values ('"+d+"','"+b+"','"+c+"')")
        #mydb.execute("update bank set Enter_Amount = Enter_Amount + '"+c+"' where Card_Number_To ='"+d+"'")
        conn.commit()
        messagebox.showinfo("Message","Transfed")
    except:
        conn.rollback()
        messagebox.showinfo("Message","Not Transfered")
    conn.close()

lb=Label(win,text="Enter_Card_Number_From",font=20,width=25).grid(row=0,column=0,padx=20,pady=20)

lb2=Label(win,text="Enter_Pin",font=20,width=10).grid(row=1,column=0,padx=20,pady=20)

lb3=Label(win,text="Enter_Amount",font=20,width=15).grid(row=2,column=0,padx=20,pady=20)

lb4=Label(win,text="Enter_Card_Number_To",font=20,width=20).grid(row=3,column=0,padx=20,pady=20)

lb5=Label(win,text="Enter_IFSC",font=20,width=10).grid(row=4,column=0,padx=20,pady=20)

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
