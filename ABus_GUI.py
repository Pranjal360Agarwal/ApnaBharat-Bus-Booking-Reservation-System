# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk


def Landing_page():
    def show():
        # global username
        print(f"Username = {username.get()}")

    # Create the main window
    window = tk.Tk()
    window.title("ApnaBharat Bus Booking Reservation")
    window.geometry("1600x800")
    window.resizable(False, False)

    # Set the background color to blue
    window.configure(bg="#B7C3EC")

    # Create a thin ribbon across the top of the window
    ribbon = tk.Frame(window, bg="#B1D6C6", height=30)
    ribbon.pack(side=tk.TOP, fill=tk.X)

    # Add the Welcome text in the middle of the ribbon
    welcome_text = tk.Label(
        ribbon,
        text="ApnaBharat Bus Booking Reservation - Signin/Register to continue",
        bg="#B1D6C6",
        font=("Calibri Light", 14),
    )
    welcome_text.place(relx=0.5, rely=0.5, anchor="center")

    # Add text on the left edge of the window
    edge_text = tk.Label(
        window, text="Welcome to ApnaBharat Bus", bg="#B7C3EC", font=("Georgia", 35)
    )
    edge_text.place(relx=0.5, rely=0.15, anchor="center")

    tk.Label(text="Username", bg="#B7C3EC", font=("Calibri", 20)).place(
        relx=0.5, rely=0.45, anchor="center"
    )
    username = tk.StringVar()
    # global username
    usernm = ttk.Entry(textvariable=username).place(
        relx=0.5, rely=0.50, anchor="center", width=250
    )
    tk.Button(text="Next ➤", command=show, bg="#113870", fg="#B1D6C6").place(
        anchor="center", relx=0.5, rely=0.55, height=40, width=100
    )

    # Run the main loop
    window.mainloop()


# ___ Username Login/Register Screen ___


def Login_pswd():
    def show():
        # global password
        print(f"Password = {password.get()}")

    # Create the main window
    window = tk.Tk()
    window.title("ApnaBharat Bus Booking Reservation")
    window.geometry("1600x800")
    window.resizable(False, False)

    # Set the background color to blue
    window.configure(bg="#B7C3EC")

    # Create a thin ribbon across the top of the window
    ribbon = tk.Frame(window, bg="#B1D6C6", height=30)
    ribbon.pack(side=tk.TOP, fill=tk.X)

    # Add the Welcome text in the middle of the ribbon
    welcome_text = tk.Label(
        ribbon,
        text="ApnaBharat Bus Booking Reservation - Signin/Register to continue",
        bg="#B1D6C6",
        font=("Calibri Light", 14),
    )
    welcome_text.place(relx=0.5, rely=0.5, anchor="center")

    # Add text on the left edge of the window
    edge_text = tk.Label(
        window, text="Welcome to ApnaBharat Bus", bg="#B7C3EC", font=("Georgia", 35)
    )
    edge_text.place(relx=0.5, rely=0.15, anchor="center")

    tk.Label(text="Password", bg="#B7C3EC", font=("Calibri", 20)).place(
        relx=0.5, rely=0.45, anchor="center"
    )
    password = tk.StringVar()
    # global password
    pswd = ttk.Entry(show="*", textvariable=password).place(
        relx=0.5, rely=0.51, anchor="center", width=250
    )
    tk.Button(
        text="Login ✔", command=show, bg="#113870", fg="#B1D6C6", font=("Calibri", 12)
    ).place(anchor="center", relx=0.5, rely=0.58, height=40, width=100)

    # Run the main loop
    window.mainloop()


# ___Login Password Screen___


def new_usr():
    def show():
        # global username
        # global password
        print(f"Username = {username.get()}    Password = {password.get()}")

    # Create the main window
    window = tk.Tk()
    window.title("ApnaBharat Bus Booking Reservation")
    window.geometry("1600x800")
    window.resizable(False, False)

    # Set the background color to blue
    window.configure(bg="#B7C3EC")

    # Create a thin ribbon across the top of the window
    ribbon = tk.Frame(window, bg="#B1D6C6", height=30)
    ribbon.pack(side=tk.TOP, fill=tk.X)

    # Add the Welcome text in the middle of the ribbon
    welcome_text = tk.Label(
        ribbon,
        text="ApnaBharat Bus Booking Reservation - Signin/Register to continue",
        bg="#B1D6C6",
        font=("Calibri Light", 14),
    )
    welcome_text.place(relx=0.5, rely=0.5, anchor="center")

    # Add text on the left edge of the window
    edge_text = tk.Label(
        window, text="Welcome to ApnaBharat Bus", bg="#B7C3EC", font=("Georgia", 35)
    )
    edge_text.place(relx=0.5, rely=0.15, anchor="center")

    tk.Label(
        text="Hi ___! Register yourself to continue", bg="#B7C3EC", font=("Calibri", 23)
    ).place(relx=0.5, rely=0.25, anchor="center")

    tk.Label(text="Username", bg="#B7C3EC", font=("Calibri", 20)).place(
        relx=0.5, rely=0.35, anchor="center"
    )
    username = tk.StringVar()
    # global username
    usrnm = ttk.Entry(textvariable=username).place(
        relx=0.5, rely=0.40, anchor="center", width=250
    )

    tk.Label(text="Password", bg="#B7C3EC", font=("Calibri", 20)).place(
        relx=0.5, rely=0.50, anchor="center"
    )
    password = tk.StringVar()
    # global password
    pswd = ttk.Entry(show="*", textvariable=password).place(
        relx=0.5, rely=0.55, anchor="center", width=250
    )

    tk.Label(text="Confirm Password", bg="#B7C3EC", font=("Calibri", 20)).place(
        relx=0.5, rely=0.65, anchor="center"
    )
    cnfpassword = ttk.Entry(show="*").place(
        relx=0.5, rely=0.70, anchor="center", width=250
    )
    tk.Button(
        text="Register and Login ✔",
        command=show,
        bg="#113870",
        fg="#B1D6C6",
        font=("Calibri", 12),
    ).place(anchor="center", relx=0.5, rely=0.75, height=40, width=200)

    # Run the main loop
    window.mainloop()


# ___ RDBMS MODULE ____

# __Data Storage and retrieval module below__

import mysql.connector as sql_conn

import tkinter as tk
from tkinter import ttk


def infobox(val):
    infobox = tk.Tk()
    infobox.geometry("800x600+100+100")
    infobox.configure(bg="#B7C3EC")
    infobox.resizable(False, False)
    infobox.title("--Info--")
    tk.Label(text=val, bg="#B7C3EC", font=("Calibri", 20)).place(
        relx=0.5, rely=0.35, anchor="center"
    )
    tk.Button(
        text="Ok ✔",
        command=infobox.destroy,
        bg="#113870",
        fg="#B1D6C6",
        font=("Calibri", 12),
    ).place(anchor="center", relx=0.5, rely=0.58, height=40, width=100)
    infobox.mainloop()


def mysql_pass():
    infobox = tk.Tk()
    infobox.geometry("800x600+100+100")
    infobox.configure(bg="#B7C3EC")
    infobox.resizable(False, False)
    infobox.title("--Info--")
    tk.Label(
        text="Enter MySQL Password (Leave blank if no password set)",
        bg="#B7C3EC",
        font=("Calibri", 20),
    ).place(relx=0.5, rely=0.35, anchor="center")
    global sql_pass
    sql_pass = tk.StringVar()
    inpt = ttk.Entry(show="*", textvariable=sql_pass).place(
        relx=0.5, rely=0.40, anchor="center", width=250
    )
    tk.Button(
        text="Login ✔",
        command=infobox.destroy,
        bg="#113870",
        fg="#B1D6C6",
        font=("Calibri", 12),
    ).place(anchor="center", relx=0.5, rely=0.58, height=40, width=100)
    infobox.mainloop()
    return sql_pass.get()


conn_obj = sql_conn.connect(host="localhost", user="root", passwd=mysql_pass())

if conn_obj.is_connected():
    infobox("Connection established...")
    sql_cursor = conn_obj.cursor()
    sql_cursor.execute("CREATE DATABASE IF NOT EXISTS Py_PassCred")
    sql_cursor.execute("USE Py_PassCred")
    infobox("Py_Pass database created")
    table = "CREATE TABLE IF NOT EXISTS passwords_data (SNo INTEGER AUTO_INCREMENT PRIMARY KEY,username VARCHAR(20),password VARCHAR(50))"
    sql_cursor.execute(table)
else:
    infobox("MySQL connection failed.")
    infobox("Please restart app after logging in to your MySQL interface.")


def data_entry(username, password):
    """
    Actual insertion of data into RDBMS.
    Parameters
    ----------
    username : STRING
        .
    password : STRING
    Returns
    -------
    None.
    """
    cmd = f"INSERT INTO passwords_data (username, password) VALUES ('{username}', '{password}')"
    data_entry = cmd
    infobox("Storing your credentials...")
    try:
        sql_cursor.execute(data_entry)
        conn_obj.commit()
        infobox("Your data was entered.")
    except (sql_conn.ProgrammingError, sql_conn.IntegrityError):
        err = "Only one password per URL is allowed for data integrity\n Please try again with a unique URL"
        infobox(err)
