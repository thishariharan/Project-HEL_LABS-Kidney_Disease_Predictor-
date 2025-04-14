import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import admin,adminpg  # Import login page file
import sqlite3

conn = sqlite3.connect("tempdb.db")  # Creates or connects to the database
cursor = conn.cursor()  # Create a cursor object to interact with the database

class AREmp:
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

        # Username
        tk.Label(self.admin_frame, text="Employee Name:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black").place(x=170, y=100)
        self.name_entry = tk.Entry(self.admin_frame, font=("Times New Roman", 12), width=20)
        self.name_entry.place(x=350, y=100)

        tk.Label(self.admin_frame, text="Username:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black").place(x=170, y=200)
        self.username_entry = tk.Entry(self.admin_frame, font=("Times New Roman", 12), width=20)
        self.username_entry.place(x=350, y=200)

        # Password
        tk.Label(self.admin_frame, text="Password:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black").place(x=170, y=300)
        self.password_entry = tk.Entry(self.admin_frame, font=("Times New Roman", 12), width=20, show="*")
        self.password_entry.place(x=350, y=300)
        
        tk.Button(self.admin_frame, text="Back", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_prev).place(x=20, y=20)

        tk.Button(self.admin_frame, text="Add Employee", font=("Times New Roman", 16, "bold"), fg="white", bg="Black", command=self.add).place(x=100, y=400)

        tk.Button(self.admin_frame, text="Remove Employee", font=("Times New Roman", 16, "bold"), fg="white", bg="Black", command=self.rem).place(x=400, y=400)

        
        # Employee Page Button
        tk.Button(self.admin_frame, text="Logout", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_login).place(x=600, y=20)

    def add(self):
        name = self.name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        cursor.execute("Select * from emp where un=?", (username,))
        r=cursor.fetchall()
        if(r):
            messagebox.showwarning("Employee Addition", "Employee already exist !")
        
        else:
            try:
                cursor.execute("INSERT INTO emp (un, nm, pw) VALUES (?, ?, ?)", (username, name, password))
                conn.commit()
                messagebox.showinfo("Employee Addition", "Employee successfully added!")
            except Exception as e:
                messagebox.showerror("Database Error", f"Error: {e}")                                                                       

        # else:
        #     cursor.execute("Insert into emp values (?,?,?)",(username,name,password))       
        #     conn.commit()     
        #     messagebox.showinfo("Employee Addition", "Employee successfully Added !")
        
    def rem(self):
        username = self.username_entry.get()
        
        cursor.execute("Select * from emp where un=?", (username,))
        r=cursor.fetchall()
        if(r):
            cursor.execute("delete from emp where un=?",(username,))     
            conn.commit()
            messagebox.showinfo("Employee Removal", "Employee successfully Removed !")
        else:
            messagebox.showwarning("Employee Removal", "Employee doesn't exist !")

    def go_to_prev(self):
        self.admin_frame.place_forget()  # Hide admin frame
        adminpg.AdminPage1(self.root)

    def go_to_login(self):
        self.admin_frame.place_forget()  # Hide admin frame
        admin.AdminPage(self.root)  # Show Login Page

if __name__ == "__main__":
    root = tk.Tk()
    app = AREmp(root)
    root.mainloop()
