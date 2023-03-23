from tkinter import*
import os
from PIL import ImageTk, Image

def bank():
    os.system("transfer3.py")

win=Tk()
win.geometry("400x450")
win.title("Select the Bank")
win.resizable(False,False)
load=Image.open('tr.png')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)


lb=Label(win,text="Select the Option",width=30,height=2,font=7).place(x=50,y=40)

bt1=Button(win,text="HDFC",command=bank,font=20,width=10,bd=10,relief="raised").place(x=50,y=150)
bt2=Button(win,text="ICICI",command=bank,font=20,width=10,bd=10,relief="raised").place(x=50,y=250)
bt3=Button(win,text="SBI",command=bank,font=20,width=10,bd=10,relief="raised").place(x=240,y=150)
bt4=Button(win,text="PNB",command=bank,font=20,width=10,bd=10,relief="raised").place(x=240,y=250)
bt4=Button(win,text="Other Bank",command=bank,font=20,width=10,bd=10,relief="raised").place(x=148,y=350)

win.mainloop()
