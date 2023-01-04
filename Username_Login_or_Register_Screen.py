import tkinter as tk
from tkinter import ttk

def Landing_page():
    def show():
        #global username
        print(f"Username = {username.get()}")


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

    tk.Label(text = 'Username', bg = "#B7C3EC", font = ("Calibri", 20)).place(relx = 0.5, rely = 0.45, anchor = 'center')
    username = tk.StringVar()
    #global username
    usernm = ttk.Entry(textvariable = username).place(relx = 0.5, rely = 0.50, anchor = 'center', width = 250)
    tk.Button(text='Next ➤', command = show, bg = "#113870", fg = "#B1D6C6").place(anchor='center', relx = 0.5, rely = 0.55, height = 40, width = 100)

    #Run the main loop
    window.mainloop()
