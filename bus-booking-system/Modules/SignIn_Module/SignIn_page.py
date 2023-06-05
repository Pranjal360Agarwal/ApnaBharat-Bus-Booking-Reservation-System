import tkinter as tk
import tkinter.messagebox
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter.font import Font
import customtkinter
import re
from PIL import Image, ImageTk
import tkinter as tk


customtkinter.set_appearance_mode("dark")


def check_credentials(username, password):
    # Read the stored usernames and passwords from text files
    with open("Modules\\SignIn_Database\\username.txt", "r") as f_username, open(
        "Modules\\SignIn_Database\\password.txt", "r"
    ) as f_password:
        stored_usernames = f_username.read().splitlines()
        stored_passwords = f_password.read().splitlines()

    # Check if the entered credentials match any of the stored values
    for stored_username, stored_password in zip(stored_usernames, stored_passwords):
        if username == stored_username and password == stored_password:
            return True

    return False


def register_event():
    def register():
        username = entry_username.get()
        password = entry_password.get()

        def check_username(user):
            if len(user) <= 4:
                return False
            return True

        def check_password(passw):
            # Check if the password has at least one uppercase letter
            if not re.search(r'[A-Z]', passw):
                return False

            # Check if the password has at least one lowercase letter
            if not re.search(r'[a-z]', passw):
                return False

            # Check if the password has at least one digit
            if not re.search(r'\d', passw):
                return False

            # Check if the password has at least one special character
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', passw):
                return False

            # All criteria are met, return True
            return True

        if not check_username(username):
            error_label.config(
                text="Username must be atleast 5 characters\nPlease input again.")
            entry_username.delete(0, tk.END)  # Clear the username input field
            return
        elif not check_password(password):
            error_label.config(
                text="Password must have at least one uppercase, lowercase, digit, and special character."
                     "\nPlease input again.")
            entry_password.delete(0, tk.END)  # Clear the password input field
            return
        # Save username and password in text files
        with open("Modules\\SignIn_Database\\username.txt", "a") as username_file:
            username_file.write(username + "\n")
        with open("Modules\\SignIn_Database\\password.txt", "a") as password_file:
            password_file.write(password + "\n")

        # print("Username:", username)
        # print("Password:", password)
        window.destroy()

    window = tk.Tk()
    window.title("Registration")
    window.geometry("600x400")

    label_username = tk.Label(window, text="Username:")
    label_username.pack()

    entry_username = tk.Entry(window)
    entry_username.pack()

    label_password = tk.Label(window, text="Password:")
    label_password.pack()

    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    error_label = tk.Label(window, text="", fg="red")
    error_label.pack()

    btn_register = tk.Button(window, text="Register", command=register)
    btn_register.pack()

    window.mainloop()


def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


class Login(customtkinter.CTk):
    width = 1240  # helps in image width
    height = 1080  # helps in image height

    def __init__(self):
        super().__init__()

        # OPENEING WINDOW SIZE
        self.title("Login")
        self.geometry(f"{1240}x{720}")
        self.bg_image = customtkinter.CTkImage(
            Image.open("Image/Background_gradient.jpg"), size=(self.width, self.height)
        )
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # LOGIN FRAME INSIDE WINDOW
        # TEXT : "Welcome!\nUnified Travelling & Transport System"
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=15)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(
            self.login_frame,
            text="Welcome!\n",
            font=customtkinter.CTkFont(
                size=24, weight="bold", slant="roman", family="Helvetica"
            ),
        )
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        # TEXT : LOGIN PAGE
        self.login_label_2 = customtkinter.CTkLabel(
            self.login_frame,
            text="Login Page",
            font=customtkinter.CTkFont(size=40, weight="bold"),
        )
        self.login_label_2.grid(row=1, column=0, padx=30, pady=(50, 15))

        # TEXT : USERNAME
        self.username_entry = customtkinter.CTkEntry(
            self.login_frame, width=300, placeholder_text="Username"
        )
        self.username_entry.grid(row=2, column=0, padx=30, pady=(15, 15))

        # TEXT : PASSWORD
        self.password_entry = customtkinter.CTkEntry(
            self.login_frame, width=300, show="*", placeholder_text="Password"
        )
        self.password_entry.grid(row=3, column=0, padx=30, pady=(0, 15))

        # TEXT : LOGIN BUTTON TEXT
        self.login_button = customtkinter.CTkButton(
            self.login_frame, text="Login", command=self.login_event, width=200
        )
        self.login_button.grid(row=4, column=0, padx=30, pady=(15, 15))

        # TEXT to register
        self.login_label_3 = customtkinter.CTkLabel(
            self.login_frame,
            text="Register now if you don't have an account.",
            font=customtkinter.CTkFont(size=12, weight="normal"),
        )
        self.login_label_3.grid(row=6, column=0, padx=30, pady=(20, 5))
        # TEXT : Register BUTTON TEXT
        self.login_button = customtkinter.CTkButton(
            self.login_frame, text="Register", command=register_event, width=200
        )
        self.login_button.grid(row=7, column=0, padx=30, pady=(0, 15))

        # Theme button
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.login_frame, text="Appearance Mode", anchor="s"
        )
        self.appearance_mode_label.grid(row=11, column=0, padx=10, pady=(5, 0))
        # Theme mode buttom
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.login_frame,
            values=["Light", "Dark", "System"],
            command=change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(row=12, column=0, padx=20, pady=(10, 10))

    def login_event(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        if check_credentials(entered_username, entered_password):
            self.destroy()
            # writing data in buffer
            with open("BufferData\\CurrentUser\\username.txt", "w") as username:
                username.write(str(entered_username))
            with open("BufferData\\CurrentUser\\password.txt", "w") as password:
                password.write(str(entered_password))
            # correct transition check
            value = True
            with open("Modules\\SignIn_Module\\SignIn_Check.txt", "w") as file:
                file.write(str(value))

        else:
            print("error")
            return messagebox.showerror("Error", "Incorrect Username or Password")

        # for debugging if any error encountered
        # print("Login pressed - username:", entered_username, "password:",entered_password)


if __name__ == "__main__":
    app9 = Login()
    app9.mainloop()
