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


def show_info_box(message):
    infobox = tk.Toplevel(window)
    infobox.title("--Info--")
    infobox.geometry("400x200")
    infobox.resizable(False, False)
    infobox.configure(bg="#B7C3EC")
    tk.Label(infobox, text=message, bg="#B7C3EC", font=("Calibri", 16)).pack(pady=20)
    tk.Button(
        infobox,
        text="Ok",
        command=infobox.destroy,
        bg="#113870",
        fg="#B1D6C6",
        font=("Calibri", 12),
    ).pack(pady=10)


def main():
    # Create the main window
    window = tk.Tk()
    window.title("ApnaBharat Bus Booking Reservation")
    window.geometry("1600x800")
    window.resizable(False, False)
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
    usernm = ttk.Entry(textvariable=username)
    usernm.place(relx=0.5, rely=0.50, anchor="center", width=250)

    tk.Button(
        text="Next ➤",
        command=new_user,
        bg="#113870",
        fg="#B1D6C6",
        font=("Calibri", 12),
    ).place(anchor="center", relx=0.5, rely=0.55, height=40, width=100)

    window.mainloop()


def connect_to_mysql():
    password = mysql_pass_entry.get()
    conn_obj = sql_conn.connect(host="localhost", user="root", passwd=password)

    if conn_obj.is_connected():
        show_info_box("Connection established...")
        sql_cursor = conn_obj.cursor()
        sql_cursor.execute("CREATE DATABASE IF NOT EXISTS Py_PassCred")
        sql_cursor.execute("USE Py_PassCred")
        show_info_box("Py_Pass database created")
        table = "CREATE TABLE IF NOT EXISTS passwords_data (SNo INTEGER AUTO_INCREMENT PRIMARY KEY,username VARCHAR(20),password VARCHAR(50))"
        sql_cursor.execute(table)
    else:
        show_info_box("MySQL connection failed.")
        show_info_box(
            "Please restart the app after logging in to your MySQL interface."
        )


def data_entry(username, password):
    cmd = f"INSERT INTO passwords_data (username, password) VALUES ('{username}', '{password}')"
    try:
        sql_cursor.execute(cmd)
        conn_obj.commit()
        show_info_box("Your data was entered.")
    except (sql_conn.ProgrammingError, sql_conn.IntegrityError):
        err = "Only one password per URL is allowed for data integrity. Please try again with a unique URL."
        show_info_box(err)


def mysql_pass():
    infobox = tk.Toplevel(window)
    infobox.geometry("400x200")
    infobox.configure(bg="#B7C3EC")
    infobox.title("--MySQL Password--")

    tk.Label(
        infobox,
        text="Enter MySQL Password (Leave blank if no password set)",
        bg="#B7C3EC",
        font=("Calibri", 14),
    ).pack(pady=10)

    mysql_pass_entry = tk.StringVar()
    entry = ttk.Entry(
        infobox,
        show="*",
        textvariable=mysql_pass_entry,
        font=("Calibri", 12),
        width=25,
    )
    entry.pack(pady=10)

    login_button = tk.Button(
        infobox,
        text="Login",
        command=connect_to_mysql,
        bg="#113870",
        fg="#B1D6C6",
        font=("Calibri", 12),
    )
    login_button.pack(pady=10)

    infobox.mainloop()
    return mysql_pass_entry.get()


window.mainloop()
