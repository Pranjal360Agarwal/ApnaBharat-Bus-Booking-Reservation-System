from tkinter import *
from tkinter.messagebox import showerror,showinfo
import sqlite3
import scrypt

con=sqlite3.Connection("My_database")
cur=con.cursor()

root = Tk()
root.title("Python Bus Service Admin")

my_img = PhotoImage(file="Bus_for_project.png")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

frame = Frame()
frame.place(x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
my_label = Label(frame,image=my_img,anchor=CENTER,width=width).grid(
    row = 0,column=0,columnspan=5
)
Label(
    frame,
    text="ADMIN REGISTER",
    font=("Arial", 25),
    bg="deep sky blue",
    fg="red",
    anchor=CENTER,
).grid(row=1, column=0, columnspan=5)
frame2 = Frame(frame, pady=20)
frame2.grid(row=2, column=0, columnspan=5)
name_var=StringVar()
uname_var=StringVar()
passw_var=StringVar()
cpassw_var=StringVar()
email_var=StringVar()

Label(frame2,text='Name').grid(row=3)
uname = Entry(frame2,textvariable=name_var).grid(row=3,column=1)
Label(frame2,text='E-Mail').grid(row=4)
uname = Entry(frame2,textvariable=email_var).grid(row=4,column=1)
Label(frame2,text='Username').grid(row=5)
uname = Entry(frame2,textvariable=uname_var).grid(row=5,column=1)
Label(frame2,text='Password').grid(row=6)
pswd = Entry(frame2,show='*',textvariable=passw_var).grid(row=6,column=1)
Label(frame2,text='Confirm Password').grid(row=7)
pswd = Entry(frame2,show='*',textvariable=cpassw_var).grid(row=7,column=1)
def handlesubmit():
    if(cpassw_var.get() != passw_var.get()):
        showinfo(title="Password Not Match",message="Please enter same password in both the field")
    else:
        hashed_password = scrypt.hash(passw_var.get(),"ApnaBharat")
        cur.execute("insert into admin(username,pass,name,email) values(?,?,?,?)",
            (uname_var.get(),str(hashed_password),name_var.get(),email_var.get()),
        )
        con.commit()
        showinfo(title="Successful",message="Admin Registered successfully");
    
Button(frame2,text="SUBMIT",anchor=CENTER, command=handlesubmit).grid(
    row=8, column=0, columnspan=5
)

root.mainloop()