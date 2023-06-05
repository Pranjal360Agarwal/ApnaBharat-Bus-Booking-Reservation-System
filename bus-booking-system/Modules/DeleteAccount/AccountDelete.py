import tkinter as tk
import tkinter.messagebox
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter.font import Font
import customtkinter
from PIL import Image, ImageTk


customtkinter.set_appearance_mode("dark")


def write_feedback(username, feedback):
    # Read the current count from the file
    with open("Feedbacks\\feedbackCount.txt", "r") as count_file:
        count = int(count_file.read())

    # Increment the count by 1
    count += 1
    # Write the updated count back to the file
    with open("Feedbacks\\feedbackCount.txt", "w") as count_file:
        count_file.write(str(count))

    # Create the new filename using the updated count and the username
    filename = "Feedbacks\\" + str((count - 1)) + username + ".txt"

    # Write the feedback to the new file
    with open(filename, "w") as feedback_file:
        feedback_file.write(feedback)


def check_credentials(username, password):
    # Read the stored usernames and passwords from text files
    with open("BufferData\\CurrentUser\\username.txt", "r") as f_username, open(
        "BufferData\\CurrentUser\\password.txt", "r"
    ) as f_password:
        stored_usernames = f_username.read().splitlines()
        stored_passwords = f_password.read().splitlines()
    # Check if the entered credentials match any of the stored values
    for stored_username, stored_password in zip(stored_usernames, stored_passwords):
        if username == stored_username and password == stored_password:
            return True

    return False


class AccountDelete(customtkinter.CTk):
    width = 452  # helps in image width
    height = 612  # helps in image height

    def __init__(self):
        super().__init__()

        # OPENEING WINDOW SIZE
        self.title("Delete Account")
        self.geometry(f"{300}x{330}")

        self.frame = customtkinter.CTkFrame(self, corner_radius=15)
        self.frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))

        self.label1 = customtkinter.CTkLabel(
            self.frame,
            text="Enter Your Credential",
            font=customtkinter.CTkFont(size=18, weight="bold"),
        )
        self.label1.grid(row=1, column=0, padx=30, pady=(50, 15))

        self.username_entry = customtkinter.CTkEntry(
            self.frame, width=200, placeholder_text="Username"
        )
        self.username_entry.grid(row=2, column=0, padx=30, pady=(15, 15))

        self.password_entry = customtkinter.CTkEntry(
            self.frame, width=200, show="*", placeholder_text="Password"
        )
        self.password_entry.grid(row=3, column=0, padx=30, pady=(0, 15))

        self.login_button = customtkinter.CTkButton(
            self.frame, text="Erase Data", command=self.Erase_event, width=200
        )
        self.login_button.grid(row=4, column=0, padx=30, pady=(15, 2.5))

        self.login_button = customtkinter.CTkButton(
            self.frame, text="Feedback Button", command=self.Feedback_dialog, width=200
        )
        self.login_button.grid(row=5, column=0, padx=30, pady=(2.5, 15))

    def Feedback_dialog(self):
        dialog = customtkinter.CTkInputDialog(
            text="Please enter your valuable Feedback\n"
            + "We are sorry you have to delete your account\n"
            + "Help us to improve",
            title="Feedback Window",
        )

        with open("BufferData\\CurrentUser\\username.txt", "r") as file:
            username = file.read()
        write_feedback(username, dialog.get_input())

    def Erase_event(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        if check_credentials(entered_username, entered_password):

            def delete_line(file_path, line_to_delete):
                with open(file_path, "r") as file:
                    lines = file.readlines()

                with open(file_path, "w") as file:
                    for line in lines:
                        if line.strip() != line_to_delete:
                            file.write(line)

            username_file_path = "Modules\\SignIn_Database\\username.txt"
            password_file_path = "Modules\\SignIn_Database\\password.txt"

            delete_line(username_file_path, entered_username)
            delete_line(password_file_path, entered_password)
            with open("Modules\\DeleteAccount\\DeleteTransition.txt", "w") as file:
                file.write(str(True))

            self.destroy()

        else:
            print("error")
            with open("Modules\\DeleteAccount\\DeleteTransition.txt", "w") as file:
                file.write(str(False))
            return messagebox.showerror("Error", "Enter Correct Credentials")


if __name__ == "__main__":
    app9 = AccountDelete()
    app9.mainloop()
