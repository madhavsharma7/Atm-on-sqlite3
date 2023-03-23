from tkinter import*
import os
from PIL import ImageTk, Image

def ab():
    os.system("deposit.py")
def wd():
    os.system("Withdraw.py")
def bl():
    os.system("Balance.py")
def tf():
    os.system("transfer2.py")
def ch():
    os.system("change.py")
def fc():
    os.system("fast.py")  
def up():
    os.system("update.py")
def new():
    os.system("newACC.py")
def st():
    os.system('ministatement1.py')
    
lin=Tk()
lin.geometry("570x420")
lin.resizable(False,False)
lin.title("Welcome to the main page")
load=Image.open('photo.jpg')
render=ImageTk.PhotoImage(load)
img=Label(lin,image=render)
img.place(x=0,y=0)

tb1=Button(lin,text="Deposit Cash",bg="slategray1",command=ab,width=20,bd=10,relief="raised",font=20).grid(row=0,column=0,padx=10,pady=10,ipadx=5,ipady=5)
tb2=Button(lin,text="Withdraw Cash",bg="slategray1",command=wd,width=20,bd=10,relief="raised",font=20).grid(row=1,column=0,padx=10,pady=10,ipadx=5,ipady=5)           
tb3=Button(lin,text="Balance Enquiry",bg="slategray1",command=bl,width=20,bd=10,relief="raised",font=20).grid(row=2,column=0,padx=10,pady=10,ipadx=5,ipady=5)
tb4=Button(lin,text="Transfer Fund",bg="slategray1",command=tf,width=20,bd=10,relief="raised",font=20).grid(row=3,column=0,padx=10,pady=10,ipadx=5,ipady=5)
tb5=Button(lin,text="Mini Statement",bg="slategray1",command=st,width=20,bd=10,relief="raised",font=20).grid(row=0,column=2,padx=20,pady=10,ipadx=5,ipady=5)
tb6=Button(lin,text="Fast Cash",bg="slategray1",command=fc,bd=10,width=20,relief="raised",font=20).grid(row=1,column=2,padx=20,pady=10,ipadx=5,ipady=5)
tb7=Button(lin,text="Change Pin",bg="slategray1",command=ch,bd=10,width=20,relief="raised",font=20).grid(row=2,column=2,padx=15,pady=10,ipadx=5,ipady=5)
tb8=Button(lin,text="Update Contact",bg="slategray1",command=up,width=20,bd=10,relief="raised",font=20).grid(row=3,column=2,padx=20,pady=10,ipadx=5,ipady=5)
tb10=Button(lin,text="Press To Exit",bg="slategray1",bd=10,relief="raised",font=20,command=lin.destroy).place(x=200,y=350)
lin.mainloop()
