import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import login, adminpg  # Import login page file
import sqlite3

conn = sqlite3.connect("tempdb.db")  # Creates or connects to the database
cursor = conn.cursor()  # Create a cursor object to interact with the database

class AdminPage:
    def __init__(self, root):
        self.root = root
        self.root.title("HEL Labs - Admin")
        self.root.geometry("700x500")

        # Load background image
        try:
            background_image = Image.open(r"Images\page 1.png")
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

        # Username
        tk.Label(self.admin_frame, text="Administrator Name:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black").place(x=170, y=298)
        self.username_entry = tk.Entry(self.admin_frame, font=("Times New Roman", 12), width=20)
        self.username_entry.place(x=375, y=300)

        # Password
        tk.Label(self.admin_frame, text="Password:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black").place(x=200, y=348)
        self.password_entry = tk.Entry(self.admin_frame, font=("Times New Roman", 12), width=20, show="*")
        self.password_entry.place(x=350, y=350)

        # Login Button
        tk.Button(self.admin_frame, text="Login", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.admin_login).place(x=320, y=400)

        # Employee Page Button
        tk.Button(self.admin_frame, text="Employee", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_login).place(x=300, y=450)

    def admin_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        cursor.execute("Select * from admin where un=? and pw=?", (username,password))
        r=cursor.fetchall()
        if(r):
            self.admin_frame.place_forget()  # Hide admin frame
            adminpg.AdminPage1(self.root)  # Show Login Page
        else:
            messagebox.showwarning("Admin Login", "Incorrect username or password")

        # if username == "AdminUser" and password == "adminpass":
        #     messagebox.showinfo("Admin Login", "Login successful!")

    def go_to_login(self):
        self.admin_frame.place_forget()  # Hide admin frame
        login.LoginPage(self.root)  # Show Login Page

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminPage(root)
    root.mainloop()
