import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import login,admin,shemp,aremp  # Import login page file
import sqlite3

conn = sqlite3.connect("tempdb.db")  # Creates or connects to the database
cursor = conn.cursor()  # Create a cursor object to interact with the database

class AdminPage1:
    def __init__(self, root):
        self.root = root
        self.root.title("HEL Labs - Admin")
        self.root.geometry("700x500")

        # Load background image
        try:
            background_image = Image.open(r"Images\others.png")
            background_image = background_image.resize((700, 500), Image.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(background_image)
        except Exception as e:
            print(f"Error loading background image: {e}")
            self.bg_image = None

        # Create admin frame
        self.admin_frame = tk.Frame(self.root)
        self.admin_frame.place(relwidth=1, relheight=1)

        # Set background image
        if self.bg_image:
            background_label = tk.Label(self.admin_frame, image=self.bg_image)
            background_label.image = self.bg_image
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

        
        tk.Button(self.admin_frame, text="Show Employees", font=("Times New Roman", 16, "bold"), fg="white", bg="Black", command=self.shemp).place(x=260, y=100)

        tk.Button(self.admin_frame, text="Add / Remove Employees", font=("Times New Roman", 16, "bold"), fg="white", bg="Black", command=self.aremp).place(x=220, y=250)

        
        # Employee Page Button
        tk.Button(self.admin_frame, text="Logout", font=("Times New Roman", 16, "bold"), fg="white", bg="Black", command=self.go_to_login).place(x=300, y=450)

    def shemp(self):
        self.admin_frame.pack_forget()
        shemp.ShEmp(self.root)
        
    def aremp(self):
        self.admin_frame.pack_forget()
        aremp.AREmp(self.root)

    def go_to_login(self):
        self.admin_frame.place_forget()  # Hide admin frame
        admin.AdminPage(self.root)  # Show Login Page

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminPage1(root)
    root.mainloop()
