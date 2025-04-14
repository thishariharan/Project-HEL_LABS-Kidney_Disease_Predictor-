import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import login,patient,ckd,dn  # Import admin page file
import sqlite3

conn = sqlite3.connect("tempdb.db")  # Creates or connects to the database
cursor = conn.cursor()

class SelectDisease:
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
        self.select_frame = tk.Frame(self.root)
        self.select_frame.place(relwidth=1, relheight=1)

        if self.bg_image:
            background_label = tk.Label(self.select_frame, image=self.bg_image)
            background_label.image = self.bg_image
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Patiets details
        tk.Label(self.select_frame, text=" Selection of Disease ", font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=250, y=60)
       
        tk.Button(self.select_frame, text="Back", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_prev).place(x=20, y=20)
        
        # Employee Page Button
        tk.Button(self.select_frame, text="Logout", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_login).place(x=600, y=20)

        
        #Diabetic Nephropathy Button
        dn_button = tk.Button(self.select_frame, text=" Diabetic Nephropathy \n by \n Random Forest ", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.to_dn)
        dn_button.place(x=80, y=150)

        #Chronic Kidney Disease Button
        ckd_button = tk.Button(self.select_frame, text=" Chronic Kidney Disease \n by \n Random Forest ", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.to_ckd)
        ckd_button.place(x=370, y=150)

    def go_to_login(self):        
        cursor.execute("delete from tpt")
        conn.commit()
        self.select_frame.place_forget()  # Hide admin frame
        login.LoginPage(self.root)  # Show Login Page
        
    def go_to_prev(self):        
        cursor.execute("delete from tpt")
        conn.commit()
        self.select_frame.place_forget()  # Hide admin frame
        patient.PatientPage(self.root)  # Show Login Page
        
    def to_dn(self):
        self.select_frame.place_forget()  # Hide admin frame
        dn.DiabeticNephropathy(self.root)  # Show Login Page

    def to_ckd(self):
        self.select_frame.place_forget()  # Hide admin frame
        ckd.ChronicKidneyDisease(self.root)  # Show Login Page



if __name__ == "__main__":
    root = tk.Tk()
    app = SelectDisease(root)
    root.mainloop()