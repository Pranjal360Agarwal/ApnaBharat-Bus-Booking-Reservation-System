import tkinter as tk
import tkinter.messagebox
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter.font import Font
import customtkinter
import re
from PIL import Image, ImageTk
import sqlite3

# import tkinter as tk


customtkinter.set_appearance_mode("dark")


def check_credentials(username, password):
    # Connect to the database
    conn = sqlite3.connect("user_credentials.db")
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve the stored usernames and passwords
    cursor.execute("SELECT username, password FROM users")
    stored_credentials = cursor.fetchall()

    # Check if the entered credentials match any of the stored values
    for stored_username, stored_password in stored_credentials:
        if username == stored_username and password == stored_password:
            conn.close()
            return True

    conn.close()
    return False


class Login(customtkinter.CTk):
    width = 1240  # helps in image width
    height = 1080  # helps in image height

    def __init__(self):
        super().__init__()

        # OPENING win SIZE
        self.title("Login")
        self.geometry(f"{1240}x{720}")
        self.bg_image = customtkinter.CTkImage(
            Image.open("Image/Background_gradient.jpg"),
            size=(self.width, self.height),
        )
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # LOGIN FRAME INSIDE win
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

        self.show_password_var = tk.BooleanVar()
        self.show_password_checkbutton = tk.Checkbutton(
            self.login_frame,
            text="Show Password",
            variable=self.show_password_var,
            command=self.toggle_password_visibility,
        )
        self.show_password_checkbutton.grid(
            row=4, column=0, padx=30, sticky="w", pady=(0, 15)
        )

        # TEXT : LOGIN BUTTON TEXT
        self.login_button = customtkinter.CTkButton(
            self.login_frame, text="Login", command=self.login_event, width=200
        )
        self.login_button.grid(row=5, column=0, padx=30, pady=(15, 15))

        # TEXT to register
        self.login_label_3 = customtkinter.CTkLabel(
            self.login_frame,
            text="Register now if you don't have an account.",
            font=customtkinter.CTkFont(size=12, weight="normal"),
        )
        self.login_label_3.grid(row=7, column=0, padx=30, pady=(20, 5))

        # TEXT : Register BUTTON TEXT
        self.login_button = customtkinter.CTkButton(
            self.login_frame, text="Register", command=self.register_event, width=200
        )
        self.login_button.grid(row=8, column=0, padx=30, pady=(0, 15))

        # Forgot Password label
        self.forgot_password_label = customtkinter.CTkLabel(
            self.login_frame,
            text="Forgot password ?",
            font=customtkinter.CTkFont(underline=True),
            cursor="hand2",
        )
        self.forgot_password_label.grid(
            row=4, column=0, padx=(0, 30), pady=(0, 15), sticky="e"
        )

        # Bind the callback function to the label's click event
        self.forgot_password_label.bind(
            "<Button-1>", lambda event: self.forgot_password_event()
        )

        # Theme button
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.login_frame, text="Appearance Mode", anchor="s"
        )
        self.appearance_mode_label.grid(row=12, column=0, padx=10, pady=(5, 0))

        # Theme mode button
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(
            self.login_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionmenu.grid(row=13, column=0, padx=20, pady=(10, 10))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    def login_event(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        if check_credentials(entered_username, entered_password):
            self.destroy()
            # writing data in buffer
            with open("BufferData/CurrentUser/username.txt", "w") as username:
                username.write(str(entered_username))
            with open("BufferData/CurrentUser/password.txt", "w") as password:
                password.write(str(entered_password))
            # correct transition check
            value = True
            with open("Modules/SignIn_Module/SignIn_Check.txt", "w") as file:
                file.write(str(value))

        else:
            print("error")
            return messagebox.showerror("Error", "Incorrect Username or Password")

        # for debugging if any error encountered
        # print("Login pressed - username:", entered_username, "password:",entered_password)

    def register_event(self):
        import tkinter as tk

        def register():
            username = entry_username.get()
            password = entry_password.get()

            def validate_password(password):
                # Check if the password has at least 1 uppercase, 1 lowercase, 1 special character, and 1 number
                if (
                    re.search(r"[A-Z]", password)
                    and re.search(r"[a-z]", password)
                    and re.search(r"\d", password)
                    and re.search(r"\W", password)
                ):
                    return True
                else:
                    return False

            if not validate_password(password):
                win.geometry("600x200")
                error_label.config(
                    text="Password is invalid!\n "
                    "Please make sure it has at least 1 uppercase, 1 lowercase, 1 special character, and 1 number."
                )
                return

            # Save username and password in the database
            import sqlite3

            conn = sqlite3.connect("user_credentials.db")
            c = conn.cursor()

            # Create table if it doesn't exist
            c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

            # Check if the username already exists
            c.execute("SELECT * FROM users WHERE username=?", (username,))
            existing_user = c.fetchone()

            if existing_user:
                messagebox.showerror(
                    "Registration Error",
                    "Username already exists. Please choose a different username.",
                )
            else:
                # Insert new user into the database
                c.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, password),
                )
                conn.commit()

                messagebox.showinfo("Registration", "Registration successful!")

            c.close()
            conn.close()

            win.destroy()

        win = tk.Tk()
        win.title("Registration")
        win.geometry("300x200")

        label_username = tk.Label(win, text="Username:")
        label_username.pack()

        entry_username = tk.Entry(win)
        entry_username.pack()

        label_password = tk.Label(win, text="Password:")
        label_password.pack()

        entry_password = tk.Entry(win, show="*")
        entry_password.pack()

        error_label = tk.Label(win, fg="red")
        error_label.pack(pady=(5, 0))

        btn_register = tk.Button(win, text="Register", command=register)
        btn_register.pack()

        win.mainloop()

    def forgot_password_event(self):
        import tkinter as tk

        def send_password():
            username = entry_username.get()

            conn = sqlite3.connect("user_credentials.db")
            c = conn.cursor()

            c.execute("SELECT * FROM users WHERE username=?", (username,))
            user = c.fetchone()

            if user:
                # Close the current win
                win.destroy()

                # Open a new win to prompt for a new password
                def update_password():
                    new_password = entry_new_password.get()

                    def validate_password(password):
                        # Check if the password has at least 1 uppercase, 1 lowercase, 1 special character, and 1 number
                        if (
                            re.search(r"[A-Z]", password)
                            and re.search(r"[a-z]", password)
                            and re.search(r"\d", password)
                            and re.search(r"\W", password)
                        ):
                            return True
                        else:
                            return False

                    if not validate_password(new_password):
                        messagebox.showerror(
                            "Invalid Password",
                            "Password is invalid!\nPlease make sure it has at least 1 uppercase, 1 lowercase, 1 special character, and 1 number.",
                        )
                        return

                    conn = sqlite3.connect("user_credentials.db")
                    c = conn.cursor()

                    # Update the password in the database
                    c.execute(
                        "UPDATE users SET password=? WHERE username=?",
                        (new_password, username),
                    )
                    conn.commit()

                    messagebox.showinfo(
                        "Password Updated", "Password updated successfully!"
                    )

                    # Close the new win
                    new_win.destroy()

                    c.close()
                    conn.close()

                new_win = tk.Toplevel()
                new_win.title("Reset Password")
                new_win.geometry("300x150")

                label_new_password = tk.Label(new_win, text="New Password:")
                label_new_password.pack()

                entry_new_password = tk.Entry(new_win, show="*")
                entry_new_password.pack()

                btn_update = tk.Button(
                    new_win, text="Update Password", command=update_password
                )
                btn_update.pack()

            else:
                messagebox.showerror(
                    "Forgot Password", "Invalid username. Please try again."
                )

            c.close()
            conn.close()

            # win.destroy()

        win = tk.Tk()
        win.title("Forgot Password")
        win.geometry("300x150")

        label_username = tk.Label(win, text="Username:")
        label_username.pack()

        entry_username = tk.Entry(win)
        entry_username.pack()

        btn_send = tk.Button(win, text="Send Password", command=send_password)
        btn_send.pack()

        win.mainloop()


if __name__ == "__main__":
    app9 = Login()
    app9.mainloop()
