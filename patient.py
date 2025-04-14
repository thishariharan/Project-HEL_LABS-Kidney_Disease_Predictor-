import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import login,select  # Import admin page file
import sqlite3

conn = sqlite3.connect("tempdb.db")  # Creates or connects to the database
cursor = conn.cursor()

class PatientPage:
    def __init__(self, root):
        self.root = root
        self.root.title("HEL Labs - Employee")
        self.root.geometry("700x500")

        try:
            background_image = Image.open(r"Images\others.png")
            background_image = background_image.resize((700, 500), Image.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(background_image)
        except Exception as e:
            print(f"Error loading background image: {e}")
            self.bg_image = None

        # Create patient frame
        self.patient_frame = tk.Frame(self.root)
        self.patient_frame.place(relwidth=1, relheight=1)

        if self.bg_image:
            background_label = tk.Label(self.patient_frame, image=self.bg_image)
            background_label.image = self.bg_image
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Patiets details
        tk.Label(self.patient_frame, text=" Patient Details ", font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=270, y=60)

        # Add patient name label and entry
        tk.Label(self.patient_frame, text="Name:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black").place(x=200, y=128)
        self.pname = tk.Entry(self.patient_frame, font=("Times New Roman", 12), width=20)
        self.pname.place(x=300, y=130)

        # Add age label and entry
        tk.Label(self.patient_frame, text="Age:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black").place(x=200, y=178)
        self.page = tk.Entry(self.patient_frame, font=("Times New Roman", 12), width=20)
        self.page.place(x=300, y=180)

        # Add height label and entry
        tk.Label(self.patient_frame, text="Height:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black").place(x=200, y=228)
        self.ph = tk.Entry(self.patient_frame, font=("Times New Roman", 12), width=20)
        self.ph.place(x=300, y=230)

        # Add weight label and entry
        tk.Label(self.patient_frame, text="Weight:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black").place(x=200, y=278)
        self.pw = tk.Entry(self.patient_frame, font=("Times New Roman", 12), width=20)
        self.pw.place(x=300, y=280)

        # Add gender label and dropdown menu
        # tk.Label(self.patient_frame, text="Gender:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black").place(x=200, y=334)
        # self.ph = tk.Entry(self.patient_frame, font=("Times New Roman", 12), width=20)
        # self.ph.place(x=300, y=330)

        gender_label = tk.Label(self.patient_frame, text="Gender", font=("Times New Roman", 14, "bold"), fg="white", bg="Black")
        gender_label.place(x=200, y=334)
        self.gender_var = tk.StringVar()
        self.gender_var.set("Select one")  # Default value
        gender_dropdown = tk.OptionMenu(self.patient_frame, self.gender_var, "Male", "Female")
        gender_dropdown.config(font=("Times New Roman", 12))
        gender_dropdown.place(x=300, y=330)

        tk.Button(self.patient_frame, text="Logout", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_login).place(x=600, y=20)

        tk.Button(self.patient_frame, text="Continue", font=("Times New Roman", 16, "bold"), fg="white", bg="Black", command=self.go_to_nxt).place(x=300, y=400)

    def go_to_login(self):
        self.patient_frame.place_forget()  # Hide admin frame
        login.LoginPage(self.root)  # Show Login Page

        
    def go_to_nxt(self):
        n = self.pname.get()
        a = self.page.get()
        h = self.ph.get()
        w = self.pw.get()
        g = self.gender_var.get()

        cursor.execute("Insert into tpt values (?,?,?,?,?)", (n,a,h,w,g))
        conn.commit()
        self.patient_frame.place_forget()  # Hide admin frame
        select.SelectDisease(self.root)  # Show Login Page

if __name__ == "__main__":
    root = tk.Tk()
    app = PatientPage(root)
    root.mainloop()