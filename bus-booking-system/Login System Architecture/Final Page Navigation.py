# importing the required modules
from idlelib import window
from tkinter import *
import os
from tkinter import messagebox
import ast

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

    # Linking it up with the database file
    file = open("dataset.txt", "r")
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username in r.keys() and password == r[username]:
        screen = Toplevel(windows)
        screen.title("ApnaBharat")
        screen.geometry("925x500+300+200")
        screen.config(bg="light blue")

        img = PhotoImage(file="busproject.png")
        Label(window, image=img, border=0, bg="blue")

    else:
        messagebox.showerror("Invalid", "Invalid Username or Password")


# -------------------------------------------------------------------------------------------------
# Adding the code of dataset here
def signup_command():
    window = Toplevel(windows)
    window.title("Sign Up")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False, False)

    # Syncing it up with text file which will work after two clicks
    def SignUp():
        username = user.get()
        password = inside.get()
        confirm_password = confirm.get()

        if password == confirm_password:
            try:
                file = open("dataset.txt", "r+")  # Read & write
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open("dataset.txt", "w")
                w = file.write(str(r))

                messagebox.showinfo("Signup", "Successfully Signed Up")
                window.destroy()

            except:  # if the file is not available
                file = open("dataset.txt", "w")
                pp = str({"Username": "password"})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror("Invalid", "Both password should match")

    def sign():
        window.destroy()

    # Adding the background image
    img = PhotoImage(file="Sign Up.png")
    Label(window, image=img, border=0, bg="white").place(x=50, y=90)

    # Adding the 'sign Up' section
    frame = Frame(window, width=350, height=390, bg="#fff")
    frame.place(x=480, y=50)

    heading = Label(
        frame,
        text="Sign Up",
        fg="#57a1f8",
        bg="white",
        font=("Microsoft Yahei UI Light", 23, "bold"),
    )
    heading.place(x=100, y=5)

    # Username
    def on_enter(e):
        user.delete(0, "end")

    def on_leave(e):
        if user.get() == "":
            user.insert(0, "Username")

    user = Entry(
        frame,
        width=25,
        fg="black",
        border=0,
        bg="white",
        font=("Microsoft Yahei UI Light", 11),
    )
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

    # Password
    def on_enter(e):
        inside.delete(0, "end")

    def on_leave(e):
        if inside.get() == "":
            inside.insert(0, "Password")

    inside = Entry(
        frame,
        width=25,
        fg="black",
        border=0,
        bg="white",
        font=("Microsoft Yahei UI Light", 11),
    )
    inside.place(x=30, y=150)
    inside.insert(0, "Password")
    inside.bind("<FocusIn>", on_enter)
    inside.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    # Confirm Password
    def on_enter(e):
        confirm.delete(0, "end")

    def on_leave(e):
        if confirm.get() == "":
            confirm.insert(0, "Confirm Password")

    confirm = Entry(
        frame,
        width=25,
        fg="black",
        border=0,
        bg="white",
        font=("Microsoft Yahei UI Light", 11),
    )
    confirm.place(x=30, y=220)
    confirm.insert(0, "Confirm Password")
    confirm.bind("<FocusIn>", on_enter)
    confirm.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

    # Button Functionality
    Button(
        frame,
        width=39,
        pady=7,
        text="Sign Up",
        bg="#57a1f8",
        fg="white",
        border=0,
        command=SignUp,
    ).place(x=35, y=280)
    label = Label(
        frame,
        text="I have an account",
        fg="black",
        bg="white",
        font=("Microsoft Yahei UI Light", 9),
    )
    label.place(x=90, y=340)

    signIn = Button(
        frame,
        width=6,
        text="Sign In",
        border=0,
        bg="white",
        cursor="hand2",
        fg="#57a1f8",
    )
    signIn.place(x=200, y=340)

    window.mainloop()


# -------------------------------------------------------------------------------------------------


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
    frame,
    width=6,
    text="Sign Up",
    border=0,
    bg="white",
    cursor="hand2",
    fg="#57a1f8",
    command=signup_command,
)
sign_up.place(x=162, y=270)


# To run Tkinter event
windows.mainloop()
