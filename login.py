import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import admin,patient  # Import admin page file
import sqlite3

conn = sqlite3.connect("tempdb.db")  # Creates or connects to the database
cursor = conn.cursor()

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("HEL Labs")
        self.root.geometry("700x500")

        # Load background image
        try:
            background_image = Image.open(r"Images\page 1.png")
            background_image = background_image.resize((700, 500), Image.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(background_image)
        except Exception as e:
            print(f"Error loading background image: {e}")
            self.bg_image = None

        # Create login frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.place(relwidth=1, relheight=1)

        # Set background image
        if self.bg_image:
            background_label = tk.Label(self.login_frame, image=self.bg_image)
            background_label.image = self.bg_image
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

        cursor.execute("delete from tpt")
        cursor.execute("delete from tresult")
        conn.commit()
        # Username
        tk.Label(self.login_frame, text="Username:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black").place(x=200, y=298)
        self.username_entry = tk.Entry(self.login_frame, font=("Times New Roman", 12), width=20)
        self.username_entry.place(x=300, y=300)

        # Password
        tk.Label(self.login_frame, text="Password:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black").place(x=200, y=348)
        self.password_entry = tk.Entry(self.login_frame, font=("Times New Roman", 12), width=20, show="*")
        self.password_entry.place(x=300, y=350)

        # Login Button
        tk.Button(self.login_frame, text="Login", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.login).place(x=320, y=400)

        # Admin Page Button
        tk.Button(self.login_frame, text="Administrator", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_admin).place(x=285, y=450)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        cursor.execute("Select * from emp where un=? and pw=?", (username,password))
        r=cursor.fetchall()
        if(r):
            self.login_frame.place_forget()  # Hide admin frame
            patient.PatientPage(self.root)  # Show Login Page
        else:
            messagebox.showwarning("Employee Login", "Incorrect username or password")

    def go_to_admin(self):
        self.login_frame.place_forget()  # Hide login frame
        admin.AdminPage(self.root)  # Show Admin Page

# Run application
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()
