from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import simpledialog

def exit_profile():
    messagebox.showinfo("Exit", "Close the Window")
    root.destroy()

def show_password():
    messagebox.showinfo("Show Password", "Your password is: ********")

def rename():
    new_name = simpledialog.askstring("Rename", "Enter new name:")
    if new_name:
        name_label.config(text=new_name)

def add_bio():
    new_bio = simpledialog.askstring("Add Bio", "Enter your bio:")
    if new_bio:
        bio_label.config(text="Bio: " + new_bio)


# color codes
# #fbf3db : BG
# #f7c92e : Button
# #747464 : user Detail text
# #1f181c : text



class Profile(tk.Toplevel):
    def __init__(root):
        super().__init__()
        root.title("User Profile")
        width = 480
        height = 620
        root.geometry("%dx%d" % (width, height))

        f1 = tk.Frame(root, bg="#fbf3db")
        f1.pack(fill=tk.BOTH, expand=True)
    
        # Load and resize the image
        image = Image.open("Image\\userprofile.jpg")
        image = image.resize((150, 150))  # Resize the image as desired
    
        # Convert the image to Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(image)
    
        # Create a Label widget to display the image
        label = tk.Label(f1, image=tk_image)
        label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
    
        # Create a Label widget for the user's name
        name_label = tk.Label(f1, text="Harsh", font=("Arial", 28), fg="black", bg="#fbf3db")
        name_label.grid(row=0, column=1, padx=10, sticky="sw")
    
        # Create a Label widget for the Date of Birth
        dob_label = tk.Label(f1, text="Date of Birth: 05/06/2003", font=("Arial", 14), fg="black", bg="#fbf3db")
        dob_label.grid(row=1, column=1, padx=10, sticky="w")
    
        # Create a Label widget for the phone number
        phone_label = tk.Label(f1, text="Phone: 1234567890", font=("Arial", 14), fg="black", bg="#fbf3db")
        phone_label.grid(row=2, column=1, padx=10, sticky="w")
    
        # Create a Label widget for the email address
        email_label = tk.Label(f1, text="Email: harsh@example.com", font=("Arial", 14), fg="black", bg="#fbf3db", wraplength=400)
        email_label.grid(row=3, column=1, padx=10, sticky="w")
    
        # Create a yellow line using Canvas widget
        line_canvas = tk.Canvas(f1, width=width, height=2, bg="#f7c92e", highlightthickness=0)
        line_canvas.grid(row=4, column=0, columnspan=2, pady=10)
    
        # Create a Label widget for the bio
        bio_label = tk.Label(f1, text="Bio: you can add your bio here from add bio and after integration your bio from database will come here.", font=("Arial", 16), fg="black", bg="#fbf3db", wraplength=400)
        bio_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    
        # Create buttons
        delete_button = Button(f1, text="Exit",bg="#f7c92e", command=exit_profile)
        show_password_button = Button(f1, text="Show Password",bg="#f7c92e", command=show_password)
        rename_button = Button(f1, text="Rename",bg="#f7c92e", command=rename)
        add_bio_button = Button(f1, text="Add Bio",bg="#f7c92e", command=add_bio)
    
        # Position the buttons using the grid layout
        delete_button.grid(row=6, column=0, padx=10, pady=10,sticky="ew")
        show_password_button.grid(row=6, column=1, padx=10, pady=10,sticky="ew")
        rename_button.grid(row=7, column=0, padx=10, pady=10,sticky="ew")
        add_bio_button.grid(row=7, column=1, padx=10, pady=10,sticky="ew")
        
        
        root.mainloop()


