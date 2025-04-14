import tkinter as tk
from tkinter import messagebox,ttk
from PIL import Image, ImageTk
import admin,adminpg  # Import login page file
import sqlite3

conn = sqlite3.connect("tempdb.db")  # Creates or connects to the database
cursor = conn.cursor()  # Create a cursor object to interact with the database

class ShEmp:
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
        
        tk.Button(self.admin_frame, text="Back", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_prev).place(x=20, y=20)
        
        # Employee Page Button
        tk.Button(self.admin_frame, text="Logout", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_login).place(x=600, y=20)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", font=("Times New Roman", 16, "bold"), background="black", foreground="white")
        style.configure("Treeview", font=("Times New Roman", 14))
                # Treeview for displaying employee data
        self.tree = ttk.Treeview(self.admin_frame, columns=("Username", "Name", "Password"), show="headings")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Password", text="Password")

        self.tree.column("Username", width=150)
        self.tree.column("Name", width=150)
        self.tree.column("Password", width=150)

        self.tree.place(x=50, y=100, width=600, height=300)

        # Optional: Add vertical scrollbar
        # scrollbar = ttk.Scrollbar(self.admin_frame, orient="vertical", command=self.tree.yview)
        # scrollbar.place(x=600, y=100, height=300)
        # self.tree.configure(yscrollcommand=scrollbar.set)

        self.show_employees()


    def show_employees(self):
        cursor.execute("SELECT * FROM emp")
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def go_to_prev(self):
        self.admin_frame.place_forget()  # Hide admin frame
        adminpg.AdminPage1(self.root)

    def go_to_login(self):
        self.admin_frame.place_forget()  # Hide admin frame
        admin.AdminPage(self.root)  # Show Login Page

if __name__ == "__main__":
    root = tk.Tk()
    app = ShEmp(root)
    root.mainloop()
