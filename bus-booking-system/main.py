import tkinter
from datetime import date
from tkinter import *
from tkinter import Button
import sqlite3
from tkinter.messagebox import *

import requests
from opencage.geocoder import RateLimitExceededError
from tkcalendar import *
import Modules.SignIn_Module.SignIn_page as SignIn
import Modules.DeleteAccount.AccountDelete as Acc_delete

con = sqlite3.Connection("My_database")
cur = con.cursor()

Check = SignIn.Login().mainloop()


def Transition_LoginToMain():
    with open("Modules\\SignIn_Module\\SignIn_Check.txt", "r") as file:
        content = file.read()
    value = bool(content)
    # For debugging
    # print(value)
    if not value:
        exit()

    with open("Modules\\SignIn_Module\\SignIn_Check.txt", "w") as file2:
        file2.truncate(0)


Transition_LoginToMain()


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
            "select * from runs where bus_id="
            + e23.get()
            + " and journey_date="
            + e24.get()
        )
        already = cur.fetchall()
        if len(already):
            showerror("Error", "Route details already exist")
        else:
            cur.execute(
                "insert into runs(bus_id,journey_date,seat_available) values(?,?,?)",
                (int(e23.get()), e24.get(), e25.get()),
            )
            con.commit()
            cur.execute(
                "select * from runs where bus_id="
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
            "DELETE FROM runs WHERE bus_id="
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

    def change_theme():
        current_bg = f17.cget("bg")  # Get the current background color

        if current_bg == "white":
            f17.configure(bg="gray70")
            f18.configure(bg="gray70")
        else:
            f17.configure(bg="white")
            f18.configure(bg="white")

    buttonTheme = Button(f17, text="Theme", command=change_theme, width=35).grid(
        row=6, column=0, columnspan=5
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
            "select * from route where route_id="
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
                "insert into route (route_id ,station ,s_id) values (?,?,?)",
                (int(e20.get()), e21.get(), int(e22.get())),
            )
            cur.execute(
                "select * from route where route_id="
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
            "DELETE FROM route WHERE route_id=? and station=? and s_id=?",
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

    def change_theme():
        current_bg = f15.cget("bg")  # Get the current background color

        if current_bg == "white":
            f15.configure(bg="gray70")
            f16.configure(bg="gray70")
        else:
            f15.configure(bg="white")
            f16.configure(bg="white")

    buttonTheme = Button(f15, text="Theme", command=change_theme, width=35).grid(
        row=6, column=0, columnspan=5
    )


def new_bus():
    f13 = Frame()
    f13.place(
        x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight()
    )
    my_label = Label(f13, image=my_img, anchor=CENTER, width=width).grid(
        row=0, column=0, columnspan=5, sticky="nsew"
    )
    Label(
        f13, text="Python Bus Service", font=("Arial", 25), bg="deep sky blue", fg="red"
    ).grid(row=1, column=0, columnspan=5, sticky="nsew")
    Label(f13, text="Add Bus Details", font=("Arial", 25), fg="light green").grid(
        row=2, column=0, columnspan=1, pady=20, sticky="nsew"
    )

    f14 = Frame(f13)
    f14.grid(row=3, column=0, columnspan=15, pady=2, sticky="nsew")
    Label(f14, text="Bus Id ", font=("Arial", 15), fg="light green").grid(
        row=0, column=0, sticky="nsew"
    )
    e14 = Entry(f14)
    e14.grid(row=0, column=1, sticky="nsew")
    Label(f14, text="Bus Type ", font=("Arial", 15), fg="light green").grid(
        row=0, column=2, sticky="nsew"
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
    )
    drop2.grid(row=0, column=3, sticky="nsew")
    Label(f14, text="Capacity ", font=("Arial", 15), fg="light green").grid(
        row=0, column=4, sticky="nsew"
    )
    e16 = Entry(f14)
    e16.grid(row=0, column=5, sticky="nsew")
    Label(f14, text="Fare Rs ", font=("Arial", 15), fg="light green").grid(
        row=1, column=0, sticky="nsew"
    )
    e17 = Entry(f14)
    e17.grid(row=1, column=1, sticky="nsew")
    Label(f14, text="Operator ID", font=("Arial", 15), fg="light green").grid(
        row=1, column=2, sticky="nsew"
    )
    e18 = Entry(f14)
    e18.grid(row=1, column=3, sticky="nsew")
    Label(f14, text="Route ID", font=("Arial", 15), fg="light green").grid(
        row=1, column=4, sticky="nsew"
    )
    e19 = Entry(f14)
    e19.grid(row=1, column=5, sticky="nsew")

    def add_bus():
        cur.execute(
            "select * from bus where bus_id=" + e14.get() + " and route_id=" + e19.get()
        )
        already = cur.fetchall()
        if len(already):
            showerror("Error", "Bus Id already exist")
        else:
            cur.execute(
                "insert into bus (bus_id,type,capacity,fare,route_id,op_id) values (?,?,?,?,?,?)",
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
                "select * from bus where bus_id="
                + e14.get()
                + " and route_id="
                + e19.get()
            )
            row = cur.fetchall()
            row = row[0]
            con.commit()
            showinfo("Successful", "Data added successfully\n" + str(row))

    def delete_bus():
        cur.execute("DELETE FROM bus WHERE bus_id=" + e14.get())
        con.commit()

        showinfo("Deleted", "Bus Details Deleted Successfully")

    button17 = Button(
        f14,
        text="Add Bus",
        font=("Arial", 15),
        bg="light green",
        anchor=CENTER,
        command=add_bus,
    )
    button17.grid(row=2, column=3, padx=20, pady=20, sticky="nsew")
    button18 = Button(
        f14,
        text="Delete",
        font=("Arial", 15),
        bg="light green",
        anchor=CENTER,
        command=delete_bus,
    )
    button18.grid(row=2, column=5, padx=20, pady=20, sticky="nsew")

    button19 = Button(f13, image=home_img, anchor=CENTER, command=tab2).grid(
        row=4, column=0, columnspan=5
    )

    def change_theme():
        current_bg = f13.cget("bg")  # Get the current background color

        if current_bg == "white":
            f13.configure(bg="gray70")
            f14.configure(bg="gray70")
        else:
            f13.configure(bg="white")
            f14.configure(bg="white")

    buttonTheme = Button(f13, text="Theme", command=change_theme, width=35).grid(
        row=6, column=0, columnspan=5
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
        cur.execute("select * from operator where op_id=" + e9.get())
        already = cur.fetchall()
        if len(already):
            showerror("Error", "Operator Id already exist")
        else:
            cur.execute(
                "insert into operator (op_id ,name ,address ,phone , email) values (?,?,?,?,?)",
                (int(e9.get()), e10.get(), e11.get(), int(e12.get()), e13.get()),
            )
            cur.execute("select * from operator where op_id=" + e9.get())
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

    def change_theme():
        current_bg = f11.cget("bg")  # Get the current background color

        if current_bg == "white":
            f11.configure(bg="gray70")
            f12.configure(bg="gray70")
        else:
            f11.configure(bg="white")
            f12.configure(bg="white")

    buttonTheme = Button(f11, text="Theme", command=change_theme, width=35).grid(
        row=6, column=0, columnspan=5
    )


# This get_weather function is called by button5 inside e1 and Frame no4 is passed
# note this api offers free calls upto 250 monthly
def get_weather(location, Outer_frame):
    valid_cities = [
        "Mumbai",
        "Delhi",
        "Bangalore",
        "Kolkata",
        "Chennai",
        "Hyderabad",
        "Ahmedabad",
        "Pune",
        "Surat",
        "Jaipur",
        "Lucknow",
        "Kanpur",
        "Nagpur",
        "Indore",
        "Thane",
        "Bhopal",
        "Patna",
        "Vadodara",
        "Amritsar",
        "Kota",
        "Ghaziabad",
        "Guna",
        "Ludhiana",
    ]
    weather_icons = {
        "395": "🌨️",  # Moderate or heavy snow in an area with thunder
        "392": "🌨️",  # Patchy light snow in an area with thunder
        "389": "⛈️",  # Moderate or heavy rain in an area with thunder
        "386": "⛈️",  # Patchy light rain in an area with thunder
        "377": "🌨️",  # Moderate or heavy showers of ice pellets
        "374": "🌨️",  # Light showers of ice pellets
        "371": "🌨️",  # Moderate or heavy snow showers
        "368": "🌨️",  # Light snow showers
        "365": "🌨️",  # Moderate or heavy sleet showers
        "362": "🌨️",  # Light sleet showers
        "359": "🌧️",  # Torrential rain shower
        "356": "🌧️",  # Moderate or heavy rain shower
        "353": "🌧️",  # Light rain shower
        "350": "🌨️",  # Ice pellets
        "338": "🌨️",  # Heavy snow
        "335": "🌨️",  # Patchy heavy snow
        "332": "🌨️",  # Moderate snow
        "329": "🌨️",  # Patchy moderate snow
        "326": "🌨️",  # Light snow
        "323": "🌨️",  # Patchy light snow
        "320": "🌨️",  # Moderate or heavy sleet
        "317": "🌨️",  # Light sleet
        "314": "🌨️",  # Moderate or heavy freezing rain
        "311": "🌨️",  # Light freezing rain
        "308": "🌧️",  # Heavy rain
        "305": "🌧️",  # Heavy rain at times
        "302": "🌧️",  # Moderate rain
        "299": "🌧️",  # Moderate rain at times
        "296": "🌧️",  # Light rain
        "293": "🌧️",  # Patchy light rain
        "284": "🌨️",  # Heavy freezing drizzle
        "281": "🌨️",  # Freezing drizzle
        "266": "🌧️",  # Light drizzle
        "263": "🌧️",  # Patchy light drizzle
        "260": "🌫️",  # Freezing fog
        "248": "🌫️",  # Fog
        "230": "🌨️",  # Blizzard
        "227": "🌨️",  # Blowing snow
        "200": "⛈️",  # Thundery outbreaks in nearby
        "185": "🌨️",  # Patchy freezing drizzle nearby
        "182": "🌨️",  # Patchy sleet nearby
        "179": "🌨️",  # Patchy snow nearby
        "176": "🌧️",  # Patchy rain nearby
        "143": "🌫️",  # Mist
        "122": "☁️",  # Overcast
        "119": "☁️",  # Cloudy
        "116": "🌤️",  # Partly Cloudy
        "113": "☀️",  # Clear/Sunny
    }
    if location != "":
        if location in valid_cities:
            try:
                api_access_key = "1c612a821aa42c79d13eb57c831c4c2f"  # Access key for Weatherstack api it is on free plan "Monthly 250 calls"
                url = f"http://api.weatherstack.com/current?access_key={api_access_key}&query={location + ',India'}"
                response = requests.get(url)
                data = response.json()

                # weather information
                temperature = data["current"]["temperature"]
                weather_description = data["current"]["weather_descriptions"][0]
                weather_code = data["current"]["weather_code"]
                weather_code = str(weather_code)
                icon = weather_icons[weather_code]
                # Inner frame
                inner_frame = tkinter.Frame(
                    Outer_frame, bg="white", bd=2, width=450, height=250
                )
                inner_frame.place(relx=0.3, rely=0.1, anchor="n")

                # displaying the icons
                icon_weather = tkinter.Label(inner_frame, text=icon, font=("Arial", 20))
                icon_weather.pack()

                # Display weather information in a label
                weather_label = tkinter.Label(
                    inner_frame,
                    text=f"Temperature of {location} : {temperature}°C\nDescription: {weather_description}",
                    bg="white",
                )
                weather_label.pack()

            except RateLimitExceededError as rlee:
                showinfo("Error Occurred  : ", rlee)
            except requests.exceptions.RequestException as rqstexcptn:
                showinfo("Error Occurred  ", rqstexcptn)
            except ValueError:
                showinfo("Error Occurred", " Incomplete or incorrect data received.")
            except KeyError as kE:
                showinfo(
                    "Error Occurred KeyError Or",
                    "You Might have Entered Wrong Spelling of  Destination",
                )
        else:
            showinfo("Error Occured:", "Invalid City")
    else:
        showinfo("Error Occurred", "Destination Not Entered ")


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

    def change_theme():
        current_bg = f4.cget("bg")  # Get the current background color

        if current_bg == "white":
            f4.configure(bg="gray70")
            final.configure(bg="gray70")
        else:
            f4.configure(bg="white")
            final.configure(bg="white")

    buttonTheme = Button(f4, text="Theme", command=change_theme, width=35).grid(
        row=6, column=0, columnspan=5
    )


def seat_book():
    f4 = Frame()
    f4.place(x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    my_label = Label(f4, image=my_img, anchor=CENTER, width=width).grid(
        row=0, column=0, columnspan=5
    )
    label1 = Label(
        f4, text="Python Bus Service", font=("Arial", 25), bg="deep sky blue", fg="red"
    ).grid(row=1, column=0, columnspan=5)
    label2 = Label(
        f4,
        text="Enter Journey Details",
        font=("Arial", 20),
        bg="light green",
        fg="green4",
        bd=5,
    ).grid(row=3, column=0, columnspan=5, pady=20)

    f5 = Frame(f4, pady=20)
    f5.grid(row=4, column=0, columnspan=5)
    label3 = Label(f5, text="TO ", font=("Arial", 10, "bold")).grid(
        row=0, column=0, sticky=E
    )
    e1 = Entry(f5)
    e1.grid(row=0, column=1)
    label4 = Label(f5, text="FROM ", font=("Arial", 10, "bold")).grid(row=1, column=0)
    e2 = Entry(f5)
    e2.grid(row=1, column=1)
    label5 = Label(
        f5, text="JOURNEY DATE (MM-DD-YYYY) ", font=("Arial", 10, "bold")
    ).grid(row=0, column=10, padx=10)
    cal = DateEntry(f5, selectmode="day", date_pattern="MM-DD-YYYY")
    cal.grid(row=0, column=11, padx=5)

    """e3 = Entry(f5)
    e3.grid(row=0,column=5)"""

    f6 = Frame(f5)

    def proceed_to(f5, busch, fare):
        if type(busch) != int:
            showinfo("Invalid Choice", "Please choose a bus!")
        else:
            f6.grid(row=6, column=0, columnspan=11, pady=20)
            Label(
                f6,
                text="Fill Passenger Details To Book The Bus Ticket",
                font=("Arial", 16),
                bg="deep sky blue",
                fg="red",
            ).grid(row=0, column=0, columnspan=15)

            Label(f6, text="Name", font=("Arial", 10)).grid(
                row=1, column=0, padx=20, pady=20
            )
            e4 = Entry(f6)
            e4.grid(row=1, column=1)
            Label(f6, text="Gender", font=("Arial", 10)).grid(
                row=1, column=2, padx=20, pady=20
            )
            menu = StringVar()
            menu.set("CHOOSE")
            drop1 = OptionMenu(f6, menu, "MALE", "FEMALE", "TRANS").grid(
                row=1, column=3
            )
            Label(f6, text="No. of seats.", font=("Arial", 10)).grid(
                row=1, column=4, padx=20, pady=20
            )

            e5 = Entry(f6)
            e5.grid(row=1, column=5)
            Label(f6, text="Mobile No", font=("Arial", 10)).grid(
                row=1, column=6, padx=20, pady=20
            )

            e6 = StringVar()
            Entry(f6, textvariable=e6).grid(row=1, column=7)
            Label(f6, text="Age", font=("Arial", 10)).grid(
                row=1, column=8, padx=20, pady=20
            )
            e7 = Entry(f6)
            e7.grid(row=1, column=9)

            def booked(fare):
                if (
                    e6.get() == ""
                    or e4.get() == ""
                    or e7.get() == ""
                    or cal.get() == ""
                    or e5.get() == ""
                    or e2.get() == ""
                    or e1.get() == ""
                ):
                    showerror("Invalid Data", "Please fill all the data!")
                else:
                    insertRow = (
                        int(e6.get()),
                        e4.get(),
                        menu.get(),
                        int(e7.get()),
                        busch,
                        cal.get(),
                        int(e5.get()),
                        fare,
                        e2.get(),
                        e1.get(),
                    )
                    fare *= insertRow[6]
                    cur.execute(
                        "select seat_available from runs where bus_id="
                        + str(busch)
                        + ' and journey_date="'
                        + cal.get()
                        + '"'
                    )
                    seats_avail = cur.fetchall()
                    seats_avl = int(seats_avail[0][0])
                    if int(e5.get()) < seats_avl:
                        resp = askyesno(
                            "Book", "Total fare = " + str(fare) + "\nProceed to book?"
                        )
                        if resp:
                            cur.execute(
                                "insert into Booking (Mobile ,Name ,sex ,age ,Bus_id , journey_date ,Ticket, Fare ,FromSt ,Tost ) values (?,?,?,?,?,?,?,?,?,?)",
                                insertRow,
                            )
                            cur.execute(
                                "update runs set seat_available="
                                + str(seats_avl - int(e5.get()))
                                + " where bus_id="
                                + str(busch)
                                + ' and journey_date="'
                                + cal.get()
                                + '"'
                            )
                            con.commit()
                            ticketShow(insertRow)
                    else:
                        showerror(
                            "Limited Seats", "Insufficient seats avilable in the bus!"
                        )

            def seat_matrix():
                import tkinter as tk
                from tkinter import messagebox

                def submit(root):
                    selected_seats = []
                    for seat_var in seat_vars:
                        if seat_var.get() != "":
                            selected_seats.append(seat_var.get())
                    # print("Selected seats:", selected_seats)
                    root.destroy()  # Close the window after submitting
                    messagebox.showinfo("Tickets Selected", "Tickets Selected")

                root = tk.Tk()
                root.title("Seat Matrix")
                bus_frame = tk.Frame(root)
                root.geometry("400x500")
                bus_frame.pack()
                bus_frame.config(bg="gray70")

                seat_vars = []
                seat_checkboxes = []

                for row in range(1, 11):
                    seat_row = tk.Frame(bus_frame)
                    seat_row.grid(row=row, column=1)
                    row_label = tk.Label(
                        seat_row, text=f"Row {row}", font=("Arial", 10, "bold")
                    )
                    row_label.pack(side=tk.TOP)

                    for col in range(1, 5):
                        seat_var = tk.StringVar()
                        seat_checkbox = tk.Checkbutton(
                            seat_row,
                            text=f"Seat {col}",
                            variable=seat_var,
                            onvalue=f"Seat {col}",
                            offvalue="",
                        )
                        seat_checkbox.pack(side=tk.LEFT)
                        seat_vars.append(seat_var)
                        seat_checkboxes.append(seat_checkbox)

                        if col == 2:
                            empty_label = tk.Label(seat_row, text=" ", width=5)
                            empty_label.pack(side=tk.LEFT)

                    seat_row.grid(row=row, column=1)

                submit_button = tk.Button(
                    root, text="Submit", command=lambda: submit(root)
                )
                submit_button.pack(pady=10)

                root.mainloop()

            # Button For seat matrix
            button8 = Button(
                f6,
                text="Seat Matrix",
                font=("Arial", 10),
                activebackground="light green",
                bg="SpringGreen3",
                command=seat_matrix,
            ).grid(row=1, column=10, padx=20, pady=20)

            button9 = Button(
                f6,
                text="Book Seat",
                font=("Arial", 10),
                activebackground="light green",
                bg="SpringGreen3",
                command=lambda: booked(fare),
            ).grid(row=1, column=11, padx=20, pady=20)

    def show_bus(f5):
        if e1.get() == "":
            showinfo("Invalid Inputs", "Please enter the Source location!")
        elif e2.get() == "":
            showinfo("Invalid Inputs", "Please enter the Destination location!")
        elif e1.get() == e2.get():
            showinfo("Invalid Inputs", "Source and Destination cannot be same!")
        elif e1.get() == "" or e2.get() == "" or cal.get() == "":
            showinfo("Invalid Inputs", "Please enter all the details!")
        else:
            data = cur.execute(
                'select b.bus_id,o.name,b.type,t.seat_available,b.fare from route r,route s,runs t,bus b,operator o where o.op_id=b.op_id and r.route_id=s.route_id and t.bus_id=b.bus_id and b.route_id=r.route_id and t.journey_date= "'
                + str(cal.get())
                + '" and r.station="'
                + str(e1.get())
                + '" and s.station="'
                + str(e2.get())
                + '" and r.s_id>s.s_id'
            )
            
            f6 = Frame(f5)
            f6.grid(row=5, column=0, columnspan=10, pady=20)
            Label(f6, text="Select BUS ", font=("Arial", 15), fg="light green").grid(
                row=0, column=0, padx=20
            )
            Label(f6, text="Operator ", font=("Arial", 15), fg="light green").grid(
                row=0, column=1, padx=20
            )
            Label(f6, text="Bus Type ", font=("Arial", 15), fg="light green").grid(
                row=0, column=2, padx=20
            )
            Label(f6, text="Availability ", font=("Arial", 15), fg="light green").grid(
                row=0, column=3, padx=10 + 10
            )
            Label(f6, text="Fare ", font=("Arial", 15), fg="light green").grid(
                row=0, column=4, padx=19 + 1
            )
            i, busch = 1, IntVar()
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

    frame_seat_booking = Frame(f5)
    frame_seat_booking.grid(row=12, column=3, columnspan=10, pady=20)
    button5 = Button(
        frame_seat_booking,
        text="Show Bus",
        font=("Arial", 15),
        activebackground="light green",
        bg="SpringGreen3",
        command=lambda: (show_bus(f5), get_weather(e1.get(), f4)),
    ).grid(row=7, column=3, padx=20)

    button6 = Button(frame_seat_booking, image=home_img, command=tab2).grid(
        row=7, column=4, padx=20
    )

    def change_theme():
        current_bg = f5.cget("bg")  # Get the current background color

        if current_bg == "white":
            f5.configure(bg="gray70")
            f4.configure(bg="gray70")
            f6.configure(bg="gray70")
        else:
            f5.configure(bg="white")
            f4.configure(bg="white")
            f6.configure(bg="white")

    buttonTheme = Button(f4, text="Theme", command=change_theme, width=35).grid(
        row=6, column=0, columnspan=5
    )


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
                # Adding Ticket data into pdf
                label_text = box.cget("text")
                global text
                text = label_text
                i += 1
                # Download Ticket
                button10 = Button(
                    f7, text="Download Ticket", anchor=CENTER, command=download_ticket
                ).grid(row=4, column=0, columnspan=5)
                temp_label = Label(f7, text="", anchor=CENTER).grid(
                    row=5, column=0, columnspan=5
                )
            if i == 5:
                showerror("Test", "No tickets found!!")

    button8 = Button(
        f8, text="Check Booking", font=("Arial", 15), command=checkHistory
    ).grid(row=0, column=2, padx=20)
    button9 = Button(f7, image=home_img, anchor=CENTER, command=tab2).grid(
        row=6, column=0, columnspan=5
    )
    button9 = Button(f7, image=home_img, anchor=CENTER, command=tab2).grid(
        row=6, column=0, columnspan=5
    )

    def change_theme():
        current_bg = f7.cget("bg")  # Get the current background color

        if current_bg == "white":
            f7.configure(bg="gray70")
            f8.configure(bg="gray70")
        else:
            f7.configure(bg="white")
            f8.configure(bg="white")

    buttonTheme = Button(f7, text="Theme", command=change_theme, width=35).grid(
        row=7, column=0, columnspan=5
    )


def add_bus():
    def all_bus():
        root = Toplevel()
        root.geometry("600x800")
        root.title("AlL BUS")
        Label(root, text="All Bus Availabe : ").place(x=20, y=20)

        Label(root, text="Bus ID", font=("Arial", 15)).place(x=20, y=80)
        Label(root, text="Bus Type", font=("Arial", 15)).place(x=100, y=80)
        Label(root, text="Capacity", font=("Arial", 15)).place(x=230, y=80)
        Label(root, text="Fare", font=("Arial", 15)).place(x=320, y=80)
        Label(root, text="Operator ID", font=("Arial", 15)).place(x=420, y=80)
        Label(root, text="Route ID", font=("Arial", 15)).place(x=480, y=80)

        sql = "Select * from Bus ;"
        cur.execute(sql)
        data = cur.fetchall()

        a = 0
        for i in data:
            a += 30
            Label(root, text=i[0]).place(x=20, y=80 + a)
            Label(root, text=i[1]).place(x=100, y=80 + a)
            Label(root, text=i[2]).place(x=230, y=80 + a)
            Label(root, text=i[3]).place(x=300, y=80 + a)
            Label(root, text=i[4]).place(x=420, y=80 + a)
            Label(root, text=i[5]).place(x=480, y=80 + a)

        root.mainloop()

    def all_routes():
        root = Toplevel()
        root.geometry("600x800")
        root.title("AlL Rutes")
        Label(root, text="All Routes Availabe : ").place(x=20, y=20)

        Label(root, text="Route Id", font=("Arial", 15)).place(x=20, y=80)
        Label(root, text="Station Name", font=("Arial", 15)).place(x=100, y=80)
        Label(root, text="Station ID", font=("Arial", 15)).place(x=230, y=80)

        sql = "Select * from route ;"
        cur.execute(sql)
        data = cur.fetchall()

        a = 0
        for i in data:
            a += 30
            Label(root, text=i[0]).place(x=20, y=80 + a)
            Label(root, text=i[1]).place(x=100, y=80 + a)
            Label(root, text=i[2]).place(x=230, y=80 + a)

        root.mainloop()

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

    button14 = Button(
        f10,
        text="All Bus",
        font=("Arial", 15),
        bg="green",
        anchor=CENTER,
        command=all_bus,
    ).grid(column=1, row=3)

    button15 = Button(
        f10,
        text="All Routes",
        font=("Arial", 15),
        bg="blue",
        anchor=CENTER,
        command=all_routes,
    ).grid(column=2, row=3)

    button23 = Button(f9, image=home_img, anchor=CENTER, command=tab2).grid(
        row=4, column=0, columnspan=5
    )

    # bg varibale 0 = white and  bg variable 1 = dark mode
    def change_theme():
        current_bg = f9.cget("bg")  # Get the current background color

        if current_bg == "white":
            f9.configure(bg="gray70")
            f10.configure(bg="gray70")
        else:
            f9.configure(bg="white")
            f10.configure(bg="white")

    buttonTheme = Button(f9, text="Theme", command=change_theme, width=35).grid(
        row=5, column=0, columnspan=5
    )


# Second tkinter GUI page
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
    f3 = Frame(f2, pady=25)
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
    # Label(f3, text="    ").grid(row=0, column=1)
    button2 = Button(
        f3,
        text="CHECK BOOKED SEAT",
        font=("Arial", 15),
        bg="light green",
        padx=10,
        pady=10,
        command=lambda: check_booked_seat(f2),
    ).grid(row=1, column=2)
    # Label(f3, text="    ").grid(row=0, column=3)
    button3 = Button(
        f3,
        text="ADD BUS DETAILS",
        font=("Arial", 15),
        bg="light green",
        padx=10,
        pady=10,
        command=add_bus,
    ).grid(row=1, column=4)

    adminlabel = Label(f3, text="For Admins Only", fg="red")
    adminlabel.grid(row=2, column=4)

    button4 = Button(f2, image=home_img, anchor=CENTER, command=tab2).grid(
        row=3, column=0, columnspan=5
    )

    # bg varibale 0 = white and  bg variable 1 = dark mode
    def change_theme():
        current_bg = f2.cget("bg")  # Get the current background color

        if current_bg == "white":
            f2.configure(bg="gray70")
            f3.configure(bg="gray70")
            adminlabel.config(bg="gray70")
        else:
            f2.configure(bg="white")
            f3.configure(bg="white")
            adminlabel.config(bg="white")

    button5 = Button(f2, text="Theme", command=change_theme, width=35).grid(
        row=4, column=0, columnspan=5
    )


# first or landing page
def tab1():
    f1 = Frame()
    f1.place(x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    my_label = Label(f1, image=my_img, anchor=CENTER).pack()
    PythonBusService = Label(
        f1,
        text="Python Bus Service",
        font=("Arial", 25),
        bg="yellow",
        fg="red",
    ).pack(padx=0, pady=50)

    Label(
        f1,
        text="Name :  Pranjal Agarwal",
        font=("Arial", 15),
        fg="white",
        anchor=S,
        pady=0,
        bg="gray70",
    ).pack(padx=0, pady=0)
    # Label(f1,text = "Enrollment No. : 211B218", font=("Arial",14),fg='blue',anchor = S).pack()
    Label(
        f1,
        text="Mobile : +919451492673",
        font=("Arial", 14),
        fg="white",
        anchor=S,
        pady=0,
        bg="gray70",
    ).pack(padx=0, pady=50)
    # Label(f1,text = "Submitted to : Dr. Mahesh Kumar", font=("Arial",20), bg = 'yellow', fg = 'red' , pady = 10).pack()
    # Label(f1,text = "Project Based learning",font="Arial 16 bold",fg='red').pack()

    button1 = Button(f1, text="Start", command=tab2, width=35).pack(pady=(0, 50))

    # bg varibale 0 = white and  bg variable 1 = dark mode
    def change_theme():
        current_bg = f1.cget("bg")  # Get the current background color

        if current_bg == "white":
            f1.configure(bg="gray70")
        else:
            f1.configure(bg="white")

    buttonTheme = Button(f1, text="Theme", command=change_theme, width=35).pack(
        anchor=S
    )

    def delete_account():
        Acc_delete.AccountDelete().mainloop()

    buttonDeleteAccount = Button(
        f1, text="Delete Your Account", command=delete_account, width=35
    )
    buttonDeleteAccount.pack(anchor=W, padx=(20, 0), pady=(150, 0))


def download_ticket():
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()

    # Set font as heading font
    pdf.set_font("Arial", style="B", size=22)
    pdf.multi_cell(0, 10, txt="Python Bus Service", align="C")
    pdf.multi_cell(0, 10, txt="", align="C")
    pdf.multi_cell(0, 10, txt="", align="C")
    pdf.multi_cell(0, 10, txt="Booked Ticket Details : ", align="L")
    pdf.multi_cell(0, 10, txt="", align="C")

    # Set font for the remaining lines
    pdf.set_font("Arial", size=15)

    # Split the text into individual lines
    lines = text.splitlines()

    # Add the remaining lines to the PDF
    for line in lines:
        pdf.multi_cell(0, 10, txt=line, align="L")

    pdf.output("Ticket_Details.pdf")

    from tkinter import messagebox

    messagebox.showinfo("PDF Downloaded", "Your Ticket has been downloaded.")


# -------------------------------------------------------------------------------------------------------------

my_img = PhotoImage(file="Image/Bus_for_project.png")
home_img = PhotoImage(file="Image/home.png")
tab1()
root.mainloop()
