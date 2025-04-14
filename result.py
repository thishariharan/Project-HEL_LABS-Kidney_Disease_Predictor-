import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import login,ckd,dn,patient  # Import admin page file
import sqlite3, pandas as pd, joblib

# model = joblib.load('CKD_RF_Model.pkl')

conn = sqlite3.connect("tempdb.db")  # Creates or connects to the database
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# dis = 0
class ResultPage:
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
        self.result = tk.Frame(self.root)
        self.result.place(relwidth=1, relheight=1)

        if self.bg_image:
            background_label = tk.Label(self.result, image=self.bg_image)
            background_label.image = self.bg_image
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Patiets details
        tk.Label(self.result, text=" Result of Analysis ", font=("Times New Roman", 18, "bold"), fg="white", bg="Black").place(x=250, y=20)
       
        cursor.execute("select * from tresult")
        r = cursor.fetchone()

        if r:
            a = self.age = r["age"]
            n = self.name = r["name"]
            g = self.gen = r["gender"]
            d = self.disease = r["disease"]

            if d == "Chronic Kidney Disease":
                self.dis = 1
            else:
                self.dis = 0

            o = self.op = r["result"]

            tk.Label(self.result, text=" Name : ", font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=170, y=100)
            tk.Label(self.result, text=n, font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=300, y=100)
            tk.Label(self.result, text=" Age : ", font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=170, y=150)
            tk.Label(self.result, text=a, font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=300, y=150)
            tk.Label(self.result, text=" Gender : ", font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=170, y=200)
            tk.Label(self.result, text=g, font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=300, y=200)
            tk.Label(self.result, text=" Disease : ", font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=170, y=250)
            tk.Label(self.result, text=d, font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=300, y=250)
            tk.Label(self.result, text=" Result : ", font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=170, y=300)
            tk.Label(self.result, text=o, font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=300, y=300)
       
        else:            
            tk.Label(self.result, text="No Records found", font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=250, y=230)
            
    #    ####

        # tk.Label(self.ckdf, text="Age", font=("Times New Roman", 12), fg="white", bg="Black").place(x=80, y=70)
        # self.age = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        # self.age.place(x=120, y=70)



        tk.Button(self.result, text="Logout", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_login).place(x=600, y=20)

        tk.Button(self.result, text="Home", font=("Times New Roman", 16, "bold"), fg="white", bg="Black", command=self.go_to_nxt).place(x=287, y=455)

        tk.Button(self.result, text="Back", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_prev).place(x=20, y=20)
        
    def go_to_login(self):        
        cursor.execute("delete from tpt")
        cursor.execute("delete from tresult")
        conn.commit()
        self.result.place_forget()  # Hide admin frame
        login.LoginPage(self.root)  # Show Login Page
        
    def go_to_prev(self):        
        cursor.execute("delete from tresult")
        conn.commit()
        if self.dis == 1:
            self.result.place_forget()  # Hide admin frame
            ckd.ChronicKidneyDisease(self.root)  # Show Login Page
        else:
            self.result.place_forget()  # Hide admin frame
            dn.DiabeticNephropathy(self.root)  # Show Login Page

        
    def go_to_nxt(self):                
        cursor.execute("delete from tpt")
        cursor.execute("delete from tresult")
        conn.commit()
        self.result.place_forget()  # Hide admin frame
        patient.PatientPage(self.root)  # Show Login Page


if __name__ == "__main__":
    root = tk.Tk()
    app = ResultPage(root)
    root.mainloop()