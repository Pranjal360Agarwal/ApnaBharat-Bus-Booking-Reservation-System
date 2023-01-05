import tkinter as tk
from tkinter import ttk

def new_usr():
    def show():
        #global username
        #global password
        print(f"Username = {username.get()}    Password = {password.get()}")

    #Create the main window
    window = tk.Tk()
    window.title('ApnaBharat Bus Booking Reservation')
    window.geometry("1600x800")
    window.resizable(False,False)

    #Set the background color to blue
    window.configure(bg="#B7C3EC")

    #Create a thin ribbon across the top of the window
    ribbon = tk.Frame(window, bg="#B1D6C6", height=30)
    ribbon.pack(side=tk.TOP, fill=tk.X)

    #Add the Welcome text in the middle of the ribbon
    welcome_text = tk.Label(ribbon, text="ApnaBharat Bus Booking Reservation - Signin/Register to continue", bg="#B1D6C6", font=("Calibri Light", 14))
    welcome_text.place(relx = 0.5, rely = 0.5, anchor = 'center')

    #Add text on the left edge of the window
    edge_text = tk.Label(window, text="Welcome to ApnaBharat Bus", bg="#B7C3EC", font=("Georgia", 35))
    edge_text.place(relx = 0.5, rely = 0.15, anchor = 'center')

    tk.Label(text = 'Hi ___! Register yourself to continue', bg = "#B7C3EC", font = ("Calibri", 23)).place(relx = 0.5, rely = 0.25, anchor = 'center')

    tk.Label(text = 'Username', bg = "#B7C3EC", font = ("Calibri", 20)).place(relx = 0.5, rely = 0.35, anchor = 'center')
    username = tk.StringVar()
    #global username
    usrnm = ttk.Entry(textvariable = username).place(relx = 0.5, rely = 0.40, anchor = 'center', width = 250)

    tk.Label(text = 'Password', bg = "#B7C3EC", font = ("Calibri", 20)).place(relx = 0.5, rely = 0.50, anchor = 'center')
    password = tk.StringVar()
    #global password
    pswd = ttk.Entry(show = '*', textvariable = password).place(relx = 0.5, rely = 0.55, anchor = 'center', width = 250)

    tk.Label(text = 'Confirm Password', bg = "#B7C3EC", font = ("Calibri", 20)).place(relx = 0.5, rely = 0.65, anchor = 'center')
    cnfpassword = ttk.Entry(show = '*').place(relx = 0.5, rely = 0.70, anchor = 'center', width = 250)
    tk.Button(text='Register and Login ✔', command = show, bg = "#113870", fg = "#B1D6C6", font = ("Calibri", 12)).place(anchor='center', relx = 0.5, rely = 0.75, height = 40, width = 200)

    #Run the main loop
    window.mainloop()
new_usr()
