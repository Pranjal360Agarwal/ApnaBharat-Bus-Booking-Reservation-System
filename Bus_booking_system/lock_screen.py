# import modules

from tkinter import *
import os

# Designing window for registration


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show="*")
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(
        register_screen,
        text="Register",
        width=10,
        height=1,
        bg="blue",
        command=register_user,
    ).pack()


# Designing window for login


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show="*")
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(
        register_screen, text="Registration Success", fg="green", font=("calibri", 11)
    ).pack()

    import re


def check_password_strength(password_info):
    if len(password_info) < 9:
        return False
    elif not re.search("[a-z]", password_info):
        return False
    elif not re.search("[A-Z]", password_info):
        return False
    elif not re.search("[0-9]", password_info):
        return False
    elif not re.search("[!@#$%^&*()_+-=]", password_info):
        return False
    else:
        return True


password_info = input("Enter a password: ")
if not check_password_strength(password_info):
    print(
        "The password is not strong enough. Please ensure it has at least 8 characters, including uppercase and lowercase letters, numbers, and symbols."
    )
else:
    print("Password is strong enough.")


# Enforcing password strength requirements with django.contrib.auth.views.password_change
from django import forms
from django.contrib import auth


class ValidatingPasswordChangeForm(auth.forms.PasswordChangeForm):
    MIN_LENGTH = 8

    def clean_new_password1(self):
        password1 = self.cleaned_data.get("new_password1")

        # At least MIN_LENGTH long
        if len(password1) < self.MIN_LENGTH:
            raise forms.ValidationError(
                "The new password must be at least %d characters long."
                % self.MIN_LENGTH
            )

        # At least one letter and one non-letter
        first_isalpha = password1[0].isalpha()
        if all(c.isalpha() == first_isalpha for c in password1):
            raise forms.ValidationError(
                "The new password must contain at least one letter and at least one digit or"
                " punctuation character."
            )

        # ... any other validation you want ...

        return password1


# Implementing event on login button


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("300x250")
    Label(login_success_screen, text="Login Success", fg="green").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("300x250")
    Label(password_not_recog_screen, text="Invalid Password ", fg="red").pack()
    Button(
        password_not_recog_screen, text="OK", command=delete_password_not_recognised
    ).pack()


# Designing popup for user not found


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("300x250")
    Label(user_not_found_screen, text="User Not Found", fg="red").pack()
    Button(
        user_not_found_screen, text="OK", command=delete_user_not_found_screen
    ).pack()


# Deleting popups


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(
        text="Select Your Choice",
        bg="yellow",
        width="300",
        height="2",
        font=("Calibri", 13),
    ).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


if __name__ == "__main__":
    main_account_screen()
