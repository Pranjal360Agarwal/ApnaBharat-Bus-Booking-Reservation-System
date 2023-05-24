from datetime import date
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import *
from tkcalendar import *
import Modules.SignIn_Module.SignIn_page as SignIn
con=sqlite3.Connection("My_database")
cur=con.cursor()

SignIn.Login().mainloop()

root = Tk()
root.title("Python Bus Service")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))


def new_run():
    f17 = Frame()
    f17.place(
        x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight()
    )
    my_label = Label(f17, image=my_img, anchor=CENTER, width=width).grid(
        row=0, column=0, columnspan=5
    )
    Label(
        f17, text="Python Bus Service", font=("Arial", 25), bg="deep sky blue", fg="red"
    ).grid(row=1, column=0, columnspan=5)
    Label(
        f17, text="Add New Running Details", font=("Arial", 25), fg="light green"
    ).grid(row=2, column=0, columnspan=5, pady=20)

    f18 = Frame(f17)
    f18.grid(row=3, column=0, columnspan=15, pady=20)
    Label(f18, text="Bus Id ", font=("Arial", 15), fg="light green").grid(
        row=0, column=0, padx=20
    )
    e23 = Entry(f18)
    e23.grid(row=0, column=1)
    Label(
        f18, text="Running Date (DD-MM-YY)", font=("Arial", 15), fg="light green"
    ).grid(row=0, column=2, padx=20)
    e24 = Entry(f18)
    e24.grid(row=0, column=3)
    Label(f18, text="Seat Available", font=("Arial", 15), fg="light green").grid(
        row=0, column=4, padx=10 + 10
    )
    e25 = Entry(f18)
    e25.grid(row=0, column=5)

    def add_run():
        cur.execute(
            'select * from runs where bus_id='
            + e23.get()
            + " and journey_date="
            + e24.get()
        )
        already = cur.fetchall()
        if len(already):
            showerror("Error", "Route details already exist")
        else:
            cur.execute(
                'insert into runs(bus_id,journey_date,seat_available) values(?,?,?)',
                (int(e23.get()), e24.get(), e25.get()),
            )
            con.commit()
            cur.execute(
                'select * from runs where bus_id='
                + e23.get()
                + ' and journey_date="'
                + e24.get()
                + '"'
            )
            row = cur.fetchall()
            row = row[0]
            con.commit()
            showinfo("Successful", "Data added successfully\n" + str(row))

    def delete_run():
        cur.execute(
            'DELETE FROM runs WHERE bus_id='
            + e23.get()
            + ' AND journey_date="'
            + e24.get()
            + '"'
        )
        con.commit()

        showinfo("Deleted", "Bus running details deleted successfully!!")

    button20 = Button(
        f18, text="Add Run", font=("Arial", 15), bg="light green", command=add_run
    ).grid(row=0, column=6, padx=20, pady=20)
    button21 = Button(
        f18,
        text="Delete",
        font=("Arial", 15),
        fg="red",
        bg="light green",
        command=delete_run,
    ).grid(row=0, column=7, padx=20, pady=20)

    button22 = Button(f17, image=home_img, anchor=CENTER, command=tab2).grid(
        row=4, column=0, columnspan=5
    )


def new_route():
    f15 = Frame()
    f15.place(
        x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight()
    )
    my_label = Label(f15, image=my_img, anchor=CENTER, width=width).grid(
        row=0, column=0, columnspan=5
    )
    Label(
        f15, text="Python Bus Service", font=("Arial", 25), bg="deep sky blue", fg="red"
    ).grid(row=1, column=0, columnspan=5)
    Label(f15, text="Add Bus Route Details", font=("Arial", 25), fg="light green").grid(
        row=2, column=0, columnspan=5, pady=20
    )

    f16 = Frame(f15)
    f16.grid(row=3, column=0, columnspan=15, pady=20)
    Label(f16, text="Route Id ", font=("Arial", 15), fg="light green").grid(
        row=0, column=0, padx=20
    )
    e20 = Entry(f16)
    e20.grid(row=0, column=1)
    Label(f16, text="Station Name ", font=("Arial", 15), fg="light green").grid(
        row=0, column=2, padx=20
    )
    e21 = Entry(f16)
    e21.grid(row=0, column=3)
    Label(f16, text="Station ID ", font=("Arial", 15), fg="light green").grid(
        row=0, column=4, padx=10 + 10
    )
    e22 = Entry(f16)
    e22.grid(row=0, column=5)

    def add_route():
        cur.execute(
            'select * from route where route_id='
            + e20.get()
            + ' and station="'
            + e21.get()
            + '" and s_id='
            + e22.get()
        )
        already = cur.fetchall()
        if len(already):
            showerror("Error", "Route details already exist")
        else:
            cur.execute(
                'insert into route (route_id ,station ,s_id) values (?,?,?)',
                (int(e20.get()), e21.get(), int(e22.get())),
            )
            cur.execute(
                'select * from route where route_id='
                + e20.get()
                + " and s_id="
                + e22.get()
            )
            row = cur.fetchall()
            row = row[0]
            con.commit()
            showinfo("Successful", "Data added successfully\n" + str(row))

    def delete_route():
        cur.execute(
            'DELETE FROM route WHERE route_id=? and station=? and s_id=?',
            (int(e20.get()), e21.get(), int(e22.get())),
        )
        con.commit()
        showinfo("Deleted", "Route Deleted Successfully")

    button20 = Button(
        f16, text="Add Route", font=("Arial", 15), bg="light green", command=add_route
    ).grid(row=0, column=6, padx=20, pady=20)
    button21 = Button(
        f16,
        text="Delete",
        font=("Arial", 15),
        fg="red",
        bg="light green",
        command=delete_route,
    ).grid(row=0, column=7, padx=20, pady=20)

    button22 = Button(f15, image=home_img, anchor=CENTER, command=tab2).grid(
        row=4, column=0, columnspan=5
    )


def new_bus():
    f13 = Frame()
    f13.place(
        x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight()
    )
    my_label = Label(f13, image=my_img, anchor=CENTER, width=width).grid(
        row=0, column=0, columnspan=5
    )
    Label(
        f13, text="Python Bus Service", font=("Arial", 25), bg="deep sky blue", fg="red"
    ).grid(row=1, column=0, columnspan=5)
    Label(f13, text="Add Bus Details", font=("Arial", 25), fg="light green").grid(
        row=2, column=0, columnspan=5, pady=20
    )

    f14 = Frame(f13)
    f14.grid(row=3, column=0, columnspan=15, pady=20)
    Label(f14, text="Bus Id ", font=("Arial", 15), fg="light green").grid(
        row=0, column=0, padx=20
    )
    e14 = Entry(f14)
    e14.grid(row=0, column=1)
    Label(f14, text="Bus Type ", font=("Arial", 15), fg="light green").grid(
        row=0, column=2, padx=20
    )
    menu1 = StringVar()
    menu1.set("CHOOSE")
    drop2 = OptionMenu(
        f14,
        menu1,
        "AC 2x2",
        "AC 3x2",
        "Non-AC 2x2",
        "Non-AC 3x2",
        "AC Sleeper 2x2",
        "Non-AC Sleeper 2x2",
    ).grid(row=0, column=3)
    Label(f14, text="Capacity ", font=("Arial", 15), fg="light green").grid(
        row=0, column=4, padx=20
    )
    e16 = Entry(f14)
    e16.grid(row=0, column=5)
    Label(f14, text="Fare Rs ", font=("Arial", 15), fg="light green").grid(
        row=0, column=6, padx=15
    )
    e17 = Entry(f14)
    e17.grid(row=0, column=7)
    Label(f14, text="Operator ID", font=("Arial", 15), fg="light green").grid(
        row=0, column=8, padx=19
    )
    e18 = Entry(f14)
    e18.grid(row=0, column=9)
    Label(f14, text="Route ID", font=("Arial", 15), fg="light green").grid(
        row=0, column=10, padx=19
    )
    e19 = Entry(f14)
    e19.grid(row=0, column=11)

    def add_bus():
        cur.execute(
            'select * from bus where bus_id=' + e14.get() + ' and route_id=' + e19.get()
        )
        already = cur.fetchall()
        if len(already):
            showerror("Error", "Bus Id already exist")
        else:
            cur.execute(
                'insert into bus (bus_id,type,capacity,fare,route_id,op_id) values (?,?,?,?,?,?)',
                (
                    int(e14.get()),
                    menu1.get(),
                    int(e16.get()),
                    int(e17.get()),
                    int(e19.get()),
                    int(e18.get()),
                ),
            )
            cur.execute(
                'select * from bus where bus_id='
                + e14.get()
                + ' and route_id='
                + e19.get()
            )
            row = cur.fetchall()
            row = row[0]
            con.commit()
            showinfo("Successful", "Data added successfully\n" + str(row))

    def delete_bus():
        cur.execute('DELETE FROM bus WHERE bus_id=' + e14.get())
        con.commit()

        showinfo("Deleted", "Bus Details Deleted Successfully")

    button17 = Button(
        f14,
        text="Add Bus",
        font=("Arial", 15),
        bg="light green",
        anchor=CENTER,
        command=add_bus,
    ).grid(row=1, column=4, padx=20, pady=20)
    button18 = Button(
        f14,
        text="Delete",
        font=("Arial", 15),
        bg="light green",
        anchor=CENTER,
        command=delete_bus,
    ).grid(row=1, column=6, padx=20, pady=20)

    button19 = Button(f13, image=home_img, anchor=CENTER, command=tab2).grid(
        row=4, column=0, columnspan=5
    )


def new_operator():
    f11 = Frame()
    f11.place(
        x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight()
    )
    my_label = Label(f11, image=my_img, anchor=CENTER, width=width).grid(
        row=0, column=0, columnspan=5
    )
    Label(
        f11, text="Python Bus Service", font=("Arial", 25), bg="deep sky blue", fg="red"
    ).grid(row=1, column=0, columnspan=5)
    Label(f11, text="Add Bus Operator Details", font=("Arial", 25), fg="green").grid(
        row=2, column=0, columnspan=5
    )

    f12 = Frame(f11)
    f12.grid(row=3, column=0, columnspan=15, pady=20)
    Label(f12, text="Operator Id ", font=("Arial", 12), fg="green").grid(
        row=0, column=0, padx=20
    )
    e9 = Entry(f12)
    e9.grid(row=0, column=1)
    Label(f12, text="Name ", font=("Arial", 12), fg="green").grid(
        row=0, column=2, padx=20
    )
    e10 = Entry(f12)
    e10.grid(row=0, column=3)
    Label(f12, text="Address ", font=("Arial", 12), fg="green").grid(
        row=0, column=4, padx=20
    )
    e11 = Entry(f12)
    e11.grid(row=0, column=5)
    Label(f12, text="Phone ", font=("Arial", 12), fg="green").grid(
        row=0, column=6, padx=10 + 10
    )
    e12 = Entry(f12)
    e12.grid(row=0, column=7)
    Label(f12, text="E-mail", font=("Arial", 12), fg="green").grid(
        row=0, column=8, padx=19 + 1
    )
    e13 = Entry(f12)
    e13.grid(row=0, column=9)

    def add_op():
        cur.execute('select * from operator where op_id=' + e9.get())
        already = cur.fetchall()
        if len(already):
            showerror("Error", "Operator Id already exist")
        else:
            cur.execute(
                "insert into operator (op_id ,name ,address ,phone , email) values (?,?,?,?,?)",
                (int(e9.get()), e10.get(), e11.get(), int(e12.get()), e13.get()),
            )
            cur.execute('select * from operator where op_id=' + e9.get())
            row = cur.fetchall()
            row = row[0]
            con.commit()
            showinfo("Successful", "Data added successfully\n" + str(row))

    def delete_op():
        cur.execute(
            "DELETE FROM operator WHERE op_id="
            + e9.get()
            + ' and name="'
            + e10.get()
            + '" and address="'
            + e11.get()
            + '" and phone='
            + e12.get()
            + ' and email="'
            + e13.get()
            + '"'
        )
        con.commit()

        showinfo("Deleted", "Operator Details Deleted Successfully")

    button15 = Button(
        f12, text="Add", font=("Arial", 15), bg="light green", command=add_op
    ).grid(row=1, column=4, padx=20)
    button16 = Button(
        f12, text="Delete", font=("Arial", 15), bg="light green", command=delete_op
    ).grid(row=1, column=6, padx=20)

    button14 = Button(f11, image=home_img, anchor=CENTER, command=tab2).grid(
        row=4, column=0, columnspan=5
    )


def ticketShow(row):
    f4 = Frame()
    f4.place(x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    my_label = Label(f4, image=my_img, anchor=CENTER, width=width).grid(
        row=0, column=0, columnspan=5
    )
    Label(
        f4, text="Python Bus Service", font=("Arial", 25), bg="deep sky blue", fg="red"
    ).grid(row=1, column=0, columnspan=5)
    Label(
        f4, text="BUS TICKET", font=("Arial", 20), bg="light green", fg="green4", bd=5
    ).grid(row=3, column=0, columnspan=5, pady=20)
    final = LabelFrame(f4)
    final.grid(row=5, column=0, columnspan=5)
    Label(final, text="Passenger: " + row[1]).grid(row=6, column=0)
    Label(final, text="No of seats: " + str(row[6])).grid(row=7, column=0)
    Label(final, text="Age: " + str(row[3])).grid(row=8, column=0)
    Label(final, text="Travel on: " + row[5]).grid(row=9, column=0)
    Label(final, text="Gender: " + row[2] + "                      ").grid(
        row=6, column=7, columnspan=3
    )
    Label(final, text="Phone: " + str(row[0]) + "              ").grid(
        row=7, column=7, columnspan=3
    )
    Label(final, text="Fare Rs: " + str(row[7]) + "                  ").grid(
        row=8, column=7, columnspan=3
    )
    Label(final, text="Bus Id: " + str(row[4]) + "                       ").grid(
        row=9, column=7, columnspan=3
    )
    Label(final, text="Boarding Point: " + row[8] + "           ").grid(
        row=10, column=7, columnspan=3
    )
    Label(
        final,
        text="Total Rs. "
        + str(row[7] * row[6])
        + " you have to pay at the time of boarding: ",
    ).grid(row=11, column=0, columnspan=3)
    showinfo("Successful", "Ticket Book Sucessfully")
    button2 = Button(f4, image=home_img, anchor=CENTER, command=tab2).grid(
        row=16, column=2, pady=50
    )



def seat_book():
    f4 = Frame()
    f4.place(x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    my_label = Label(f4, image=my_img, anchor=CENTER, width=width).grid(
        row=0, column=0, columnspan=5
    )
    Label(
        f4, text="Python Bus Service", font=("Arial", 25), bg="deep sky blue", fg="red"
    ).grid(row=1, column=0, columnspan=5)
    Label(
        f4,
        text="Enter Journey Details",
        font=("Arial", 20),
        bg="light green",
        fg="green4",
        bd=5,
    ).grid(row=3, column=0, columnspan=5, pady=20)

    f5 = Frame(f4, pady=20)
    f5.grid(row=4, column=0, columnspan=5)
    label=Label(f5, text="TO ", font=("Arial", 10)).grid(row=0, column=0, sticky=E)
    cities= [
    "Guna",
    "Delhi",
    "Bhopal",
    "Kota",
    "Amritsar",
    "Jaipur"]
    dropdown_to = ttk.Combobox(f5,values=cities)
    dropdown_to.grid(row=0, column=1, padx=10)
    e1 = dropdown_to
    label=Label(f5, text="FROM ", font=("Arial", 10)).grid(row=0, column=2)
    dropdown_from = ttk.Combobox(f5,values=cities)
    dropdown_from.grid(row=0, column=3, padx=10)
    e2 = dropdown_from
    Label(f5,text = "JOURNEY DATE (MM-DD-YYYY) ", font=("Arial",10)).grid(row=0,column=4)
    cal=DateEntry(f5,selectmode='day', date_pattern = "MM-DD-YYYY")
    cal.grid(row=0,column=5,padx=15)
    '''e3 = Entry(f5)
    e3.grid(row=0,column=5)'''
    
    def proceed_to(f5, busch, fare):
        if type(busch) != int:
            showinfo("Invalid Choice", "Please choose a bus!")
        else:
            f6 = Frame(f5)
            f6.grid(row=6, column=0, columnspan=10, pady=20)
            Label(
                f6,
                text="Fill Passenger Details To Book The Bus Ticket",
                font=("Arial", 25),
                bg="deep sky blue",
                fg="red",
            ).grid(row=0, column=0, columnspan=15)
            Label(f6, text="Name", font=("Arial", 15)).grid(
                row=1, column=0, padx=20, pady=20
            )
            e4 = Entry(f6)
            e4.grid(row=1, column=1)
            Label(f6, text="Gender", font=("Arial", 15)).grid(
                row=1, column=2, padx=20, pady=20
            )
            menu = StringVar()
            menu.set("CHOOSE")
            drop1 = OptionMenu(f6, menu, "MALE", "FEMALE", "TRANS").grid(
                row=1, column=3
            )
            Label(f6, text="No. of seats.", font=("Arial", 15)).grid(
                row=1, column=4, padx=20, pady=20
            )

            e5 = Entry(f6)
            e5.grid(row=1, column=5)
            Label(f6, text="Mobile No", font=("Arial", 15)).grid(
                row=1, column=6, padx=20, pady=20
            )

            e6 = StringVar()
            Entry(f6, textvariable=e6).grid(row=1, column=7)
            Label(f6, text="Age", font=("Arial", 15)).grid(
                row=1, column=8, padx=20, pady=20
            )
            e7 = Entry(f6)
            e7.grid(row=1, column=9)

            def booked(fare):
                if e6.get()=="" or e4.get()=="" or e7.get()=="" or cal.get()=="" or e5.get()=="" or e2.get()=="" or e1.get()=="":
                    showerror("Invalid Data","Please fill all the data!")
                else:                    
                    insertRow = (int(e6.get()),e4.get(),menu.get(),int(e7.get()),busch,cal.get(),int(e5.get()),fare,e2.get(),e1.get())
                    fare*=insertRow[6]
                    cur.execute('select seat_available from runs where bus_id='+str(busch)+' and journey_date="'+cal.get()+'"')
                    seats_avail=cur.fetchall()
                    seats_avl=int(seats_avail[0][0])
                    if int(e5.get())<seats_avl:
                        resp = askyesno("Book","Total fare = "+str(fare)+"\nProceed to book?")
                        if resp:
                            cur.execute('insert into Booking (Mobile ,Name ,sex ,age ,Bus_id , journey_date ,Ticket, Fare ,FromSt ,Tost ) values (?,?,?,?,?,?,?,?,?,?)',insertRow)
                            cur.execute('update runs set seat_available='+str(seats_avl-int(e5.get()))+' where bus_id='+str(busch)+' and journey_date="'+cal.get()+'"')
                            con.commit()
                            ticketShow(insertRow)
                    else:
                        showerror(
                            "Limited Seats", "Insufficient seats avilable in the bus!"
                        )

            button8 = Button(
                f6,
                text="Book Seat",
                font=("Arial", 15),
                activebackground="light green",
                bg="SpringGreen3",
                command=lambda: booked(fare),
            ).grid(row=1, column=10, padx=20, pady=20)

    def show_bus(f5):
        if e1.get()=="" or e2.get()=="" or cal.get()=="":
            showinfo("Invalid Inputs","Please enter all the details!")
        else:
            data=cur.execute('select b.bus_id,o.name,b.type,t.seat_available,b.fare from route r,route s,runs t,bus b,operator o where o.op_id=b.op_id and r.route_id=s.route_id and t.bus_id=b.bus_id and b.route_id=r.route_id and t.journey_date= "'+str(cal.get())+'" and r.station="'+str(e1.get())+'" and s.station="'+str(e2.get())+'" and r.s_id>s.s_id')
            f6=Frame(f5)
            f6.grid(row = 5, column = 0, columnspan = 10,pady = 20)
            Label(f6,text = "Select BUS ", font=("Arial",15),fg='light green').grid(row=0,column=0,padx = 20)
            Label(f6,text = "Operator ", font=("Arial",15),fg='light green').grid(row=0,column=1,padx=20)
            Label(f6,text = "Bus Type ", font=("Arial",15),fg='light green').grid(row=0,column=2,padx= 20)
            Label(f6,text = "Availability ", font=("Arial",15),fg='light green').grid(row=0,column=3,padx = 10+10)
            Label(f6,text = "Fare ", font=("Arial",15),fg='light green').grid(row=0,column=4, padx = 19+1)
            i,busch=1,IntVar()
            for row in data:
                rb = Radiobutton(f6, text="Bus" + str(i), variable=busch, value=row[0])
                rb.grid(row=i, column=0)
                Label(f6, text=str(row[1]), fg="green").grid(row=i, column=1)
                Label(f6, text=str(row[2]), fg="green").grid(row=i, column=2)
                Label(f6, text=str(row[3]), fg="green").grid(row=i, column=3)
                Label(f6, text=str(row[4]), fg="green").grid(row=i, column=4)
                i += 1
            if i == 1:
                showinfo("Not Found", "No bus found for given details!")
            button7 = Button(
                f6,
                text="Proceed to Book",
                font=("Arial", 15),
                activebackground="light green",
                bg="SpringGreen3",
                command=lambda: proceed_to(f5, busch.get(), row[4]),
            ).grid(row=1, column=5, padx=20, pady=20)

    button5 = Button(
        f5,
        text="Show Bus",
        font=("Arial", 15),
        activebackground="light green",
        bg="SpringGreen3",
        command=lambda: show_bus(f5),
    ).grid(row=0, column=6, padx=20)
    button6 = Button(f5, image=home_img, command=tab2).grid(row=0, column=7, padx=20)


text = ""
def check_booked_seat(f2):
    f7 = Frame(f2)
    f7.place(x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    my_label = Label(f7, image=my_img, anchor=CENTER, width=width).grid(
        row=0, column=0, columnspan=5
    )
    Label(
        f7,
        text="Python Bus Service",
        font=("Arial", 25),
        bg="deep sky blue",
        fg="red",
        anchor=CENTER,
    ).grid(row=1, column=0, columnspan=5)
    Label(
        f7,
        text="Check Your Booking",
        font=("Arial", 25),
        bg="light green",
        fg="forest green",
    ).grid(row=2, column=0, columnspan=10, pady=20)

    f8 = Frame(f7)
    f8.grid(row=3, column=0, pady=20, columnspan=5)
    Label(f8, text="Enter Your Mobile No.", font=("Arial", 15)).grid(row=0, column=0)
    e8 = Entry(f8)
    e8.grid(row=0, column=1, padx=20)

    def checkHistory():
        MobNo = e8.get()
        if len(e8.get()) != 10:
            showerror("Value Missing", "Enter correct Mobile Number!!")
        elif e8.get() == "":
            showerror("Error", "Value missing!!!")
        else:
            cur.execute(
                "select name,sex,ticket,mobile,age,fare,ref_id,bus_id,fromst,tost,journey_date from booking where Mobile="
                + str(e8.get())
                + " order by ref_id desc limit 1"
            )
            con.commit()
            details = cur.fetchall()
            i = 5
            
            for row in details:
                box = Label(
                    f8,
                    text="Name: "
                    + row[0]
                    + "\nGender: "
                    + row[1]
                    + "\nNo. of seats: "
                    + str(row[2])
                    + "\nPhone: "
                    + str(row[3])
                    + "\nAge: "
                    + str(row[4])
                    + "\nFare Rs: "
                    + str(row[5])
                    + "\nBooking ref: "
                    + str(row[6])
                    + "\nBus Id: "
                    + str(row[7])
                    + "\nBoarding point: "
                    + row[8]
                    + "\nDestination: "
                    + row[9]
                    + "\nTravel On: "
                    + row[10]
                    + "\n\n *Total amount Rs "
                    + str(row[5] * row[2])
                    + " to be paid at time of boarding the bus",
                    font="bold",
                    relief="groove",
                )
                box.grid(row=i, column=0, columnspan=3)
                #Adding Ticket data into pdf
                label_text = box.cget("text") 
                global text 
                text = label_text
                i += 1
                 #Download Ticket 
                button10 = Button(f7, text="Download Ticket", anchor=CENTER, command=download_ticket).grid(
                    row=4, column=0, columnspan=5)
                temp_label = Label(f7, text="", anchor=CENTER).grid(
                    row=5, column=0, columnspan=5)
            if i == 5:
                showerror("Test", "No tickets found!!")

    button8 = Button(
        f8, text="Check Booking", font=("Arial", 15), command=checkHistory
    ).grid(row=0, column=2, padx=20)
    button9 = Button(f7, image=home_img, anchor=CENTER, command=tab2).grid(
        row=6, column=0, columnspan=5
    )

   


def add_bus():
    f9 = Frame()
    f9.place(x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    my_label = Label(f9, image=my_img, anchor=CENTER, width=width).grid(
        row=0, column=0, columnspan=5
    )
    Label(
        f9,
        text="Python Bus Service",
        font=("Arial", 25),
        bg="deep sky blue",
        fg="red",
        anchor=CENTER,
    ).grid(row=1, column=0, columnspan=5)
    Label(
        f9,
        text="Add New Details to Database",
        font=("Arial", 25),
        bd=5,
        fg="light green",
        bg="green",
    ).grid(row=2, column=0, columnspan=10, pady=20)

    f10 = Frame(f9)
    f10.grid(row=3, column=0, pady=20, columnspan=10)
    button10 = Button(
        f10,
        text="New Operator",
        font=("Arial", 15),
        bg="light green",
        command=new_operator,
    ).grid(row=0, column=0, padx=20)
    button11 = Button(
        f10,
        text="New Bus",
        font=("Arial", 15),
        bg="orange",
        anchor=CENTER,
        command=new_bus,
    ).grid(row=0, column=1, padx=20)
    button12 = Button(
        f10,
        text="New Route",
        font=("Arial", 15),
        bg="SlateBlue1",
        anchor=CENTER,
        command=new_route,
    ).grid(row=0, column=2, padx=20)
    button13 = Button(
        f10,
        text="New Run",
        font=("Arial", 15),
        bg="sienna3",
        anchor=CENTER,
        command=new_run,
    ).grid(row=0, column=3, padx=20)
    button23 = Button(f9, image=home_img, anchor=CENTER, command=tab2).grid(
        row=4, column=0, columnspan=5
    )


def tab2():
    f2 = Frame()
    f2.place(x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    my_label = Label(f2, image=my_img, anchor=CENTER, width=width).grid(
        row=0, column=0, columnspan=5
    )
    Label(
        f2,
        text="Python Bus Service",
        font=("Arial", 25),
        bg="deep sky blue",
        fg="red",
        anchor=CENTER,
    ).grid(row=1, column=0, columnspan=5)
    f3 = Frame(f2, pady=20)
    f3.grid(row=2, column=0, columnspan=5)

    button2 = Button(
        f3,
        text="SEAT BOOKING",
        font=("Arial", 15),
        bg="light green",
        padx=10,
        pady=10,
        command=seat_book,
    ).grid(row=1, column=0)
    Label(f3, text="    ").grid(row=0, column=1)
    button2 = Button(
        f3,
        text="CHECK BOOKED SEAT",
        font=("Arial", 15),
        bg="light green",
        padx=10,
        pady=10,
        command=lambda: check_booked_seat(f2),
    ).grid(row=1, column=2)
    Label(f3, text="    ").grid(row=0, column=3)
    button3 = Button(
        f3,
        text="ADD BUS DETAILS",
        font=("Arial", 15),
        bg="light green",
        padx=10,
        pady=10,
        command=add_bus,
    ).grid(row=1, column=4)
    Label(f3, text="For Admins Only", fg="red").grid(row=2, column=4)
    button4 = Button(f2, image=home_img, anchor=CENTER, command=tab2).grid(
        row=3, column=0, columnspan=5
    )


def tab1():
    f1 = Frame()
    f1.place(x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    my_label = Label(f1, image=my_img, anchor=CENTER).pack()
    Label(
        f1, text="Python Bus Service", font=("Arial", 25), bg="yellow", fg="red"
    ).pack()
    Label(
        f1,
        text="Name : Pranjal Agarwal",
        font=("Arial", 15),
        fg="blue",
        anchor=S,
        pady=50,
    ).pack()
    # Label(f1,text = "Enrollment No. : 211B218", font=("Arial",14),fg='blue',anchor = S).pack()
    Label(
        f1,
        text="Mobile : +919451492673",
        font=("Arial", 14),
        fg="blue",
        anchor=S,
        pady=50,
    ).pack()
    # Label(f1,text = "Submitted to : Dr. Mahesh Kumar", font=("Arial",20), bg = 'yellow', fg = 'red' , pady = 10).pack()
    # Label(f1,text = "Project Based learning",font="Arial 16 bold",fg='red').pack()

    button1 = Button(f1, text="Start", command=tab2).pack()

def download_ticket():
  from fpdf import FPDF
  pdf = FPDF()
  pdf.add_page()

  # Set font as heading font
  pdf.set_font("Arial", style="B", size=22)
  pdf.multi_cell(0, 10, txt="Python Bus Service", align='C')
  pdf.multi_cell(0, 10, txt="", align='C')
  pdf.multi_cell(0, 10, txt="", align='C')
  pdf.multi_cell(0, 10, txt="Booked Ticket Details : ", align='L')
  pdf.multi_cell(0, 10, txt="", align='C')
 
  # Set font for the remaining lines
  pdf.set_font("Arial", size=15)

  # Split the text into individual lines
  lines = text.splitlines()

  # Add the remaining lines to the PDF
  for line in lines:
     pdf.multi_cell(0, 10, txt=line, align='L')

  pdf.output("Ticket_Details.pdf")

  from tkinter import messagebox
  messagebox.showinfo("PDF Downloaded", "Your Ticket has been downloaded.")







# -------------------------------------------------------------------------------------------------------------

my_img = PhotoImage(file="Bus_for_project.png")
home_img = PhotoImage(file="home.png")
tab1()
root.mainloop()
