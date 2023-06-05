# importing the required modules
from tkinter import *
import os
from tkinter import messagebox

# Configuration of screen size
windows = Tk()
windows.title("Login")
windows.geometry("925x500+300+200")
windows.config(bg="#52057B")
windows.resizable(False, False)


# Function for SignIn functionality
def signIn():
    username = user.get()
    password = inside.get()

    if username == "admin" and password == "1234":  # constant username & password
        # Output will be displayed on terminal
        # print('Hey There ;)')
        screen = Toplevel(windows)
        screen.title("Prototype")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")

        Label(
            screen, text="Hey There ;)", bg="#fff", font=("Calibri(Body)", 50, "bold")
        ).pack(expand=True)
        screen.mainloop()

    elif username != "admin" and password != "1234":
        messagebox.showerror("Invalid", "Both credentials are incorrect")

    elif username != "admin" or password != "1234":
        messagebox.showerror("Invalid", "Incorrect Username/Password")


# Adding the background image
img = PhotoImage(file="Login.png")
Label(windows, image=img, bg="black").place(x=50, y=50)

# Adding the 'sign in' section
frame = Frame(windows, width=350, height=350, bg="white")
frame.place(x=480, y=70)
heading = Label(
    frame,
    text="Sign In",
    fg="#711A75",
    bg="white",
    font=("Microsoft YaHei UI Light", 23, "bold"),
)
heading.place(x=100, y=5)

# Adding Username Section


# Adding functions for writing the password
def on_enter(e):
    user.delete(0, "end")


def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "Username")


user = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft YaHei UI Light", 11, "bold"),
)
user.place(x=30, y=80)
user.insert(0, "Username")

user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(
    x=25, y=107
)  # For adding a bold line below the text

# Adding Password Section


# Adding functions for writing the password
def on_enter(e):
    inside.delete(0, "end")


def on_leave(e):
    name = inside.get()
    if name == "":
        inside.insert(0, "Password")


inside = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft YaHei UI Light", 11, "bold"),
)
inside.place(x=30, y=150)
inside.insert(0, "Password")

inside.bind("<FocusIn>", on_enter)
inside.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(
    x=25, y=177
)  # For adding a bold line below the text

# Adding Buttons for submitting
Button(
    frame,
    width=39,
    pady=7,
    text="Sign In",
    bg="#BC6FF1",
    fg="white",
    border=0,
    command=signIn,
).place(
    x=35, y=204
)  # Adding the signIn functionality
label = Label(
    frame,
    text="Don't have an account?",
    fg="black",
    bg="white",
    font=("Microsoft YaHei UI Light", 9),
)
label.place(x=25, y=270)

# Sign Up option
sign_up = Button(
    frame, width=6, text="Sign Up", border=0, bg="white", cursor="hand2", fg="#57a1f8"
)
sign_up.place(x=162, y=270)


# To run Tkinter event
windows.mainloop()
