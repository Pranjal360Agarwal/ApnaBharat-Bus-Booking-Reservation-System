# ___ RDBMS MODULE ____

# __Data Storage and retrieval module below__

import mysql.connector as sql_conn

import tkinter as tk
from tkinter import ttk

def infobox(val):
    infobox = tk.Tk()
    infobox.geometry("800x600+100+100")
    infobox.configure(bg = "#B7C3EC")
    infobox.resizable(False, False)
    infobox.title('--Info--')
    tk.Label(text = val, bg = "#B7C3EC", font = ("Calibri", 20)).place(relx = 0.5, rely = 0.35, anchor = 'center')
    tk.Button(text='Ok ✔', command = infobox.destroy, bg = "#113870", fg = "#B1D6C6", font = ("Calibri", 12)).place(anchor='center', relx = 0.5, rely = 0.58, height = 40, width = 100)
    infobox.mainloop()

def mysql_pass():
    infobox = tk.Tk()
    infobox.geometry("800x600+100+100")
    infobox.configure(bg="#B7C3EC")
    infobox.resizable(False, False)
    infobox.title('--Info--')
    tk.Label(text = 'Enter MySQL Password (Leave blank if no password set)', bg = "#B7C3EC", font = ("Calibri", 20)).place(relx = 0.5, rely = 0.35, anchor = 'center')
    global sql_pass
    sql_pass = tk.StringVar()
    inpt = ttk.Entry(show = "*", textvariable = sql_pass).place(relx = 0.5, rely = 0.40, anchor = 'center', width = 250)
    tk.Button(text='Login ✔', command = infobox.destroy, bg = "#113870", fg = "#B1D6C6", font = ("Calibri", 12)).place(anchor='center', relx = 0.5, rely = 0.58, height = 40, width = 100)
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
    cmd = f"INSERT INTO passwords_data (site_name, site_url, username, password, password_nature) VALUES ('{site_name}', '{site_URL}', '{username}', '{password}', '{password_nature}')"
    data_entry = cmd
    infobox("Storing your credentials...")
    try:
        sql_cursor.execute(data_entry)
        conn_obj.commit()
        infobox("Your data was entered.")
    except (sql_conn.ProgrammingError, sql_conn.IntegrityError):
        err = "Only one password per URL is allowed for data integrity\n Please try again with a unique URL"
        infobox(err)
