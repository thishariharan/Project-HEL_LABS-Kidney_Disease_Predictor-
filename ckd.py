import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import login,select, result  # Import admin page file
import sqlite3, pandas as pd, joblib

model = joblib.load('CKD_RF_Model.pkl')

conn = sqlite3.connect("tempdb.db")  # Creates or connects to the database
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

class ChronicKidneyDisease:
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
        self.ckdf = tk.Frame(self.root)
        self.ckdf.place(relwidth=1, relheight=1)

        if self.bg_image:
            background_label = tk.Label(self.ckdf, image=self.bg_image)
            background_label.image = self.bg_image
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Patiets details
        tk.Label(self.ckdf, text=" Datas for Chronic Kidney Disease ", font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=170, y=20)
       
    #    ####

        tk.Label(self.ckdf, text="Age", font=("Times New Roman", 12), fg="white", bg="Black").place(x=80, y=70)
        self.age = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.age.place(x=120, y=70)

        tk.Label(self.ckdf, text="B P", font=("Times New Roman", 12), fg="white", bg="Black").place(x=80, y=100)
        self.bp = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.bp.place(x=120, y=100)

        tk.Label(self.ckdf, text="Specific Gravity", font=("Times New Roman", 12), fg="white", bg="Black").place(x=5, y=130)
        self.sg = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.sg.place(x=120, y=130)

        tk.Label(self.ckdf, text="Albumin", font=("Times New Roman", 12), fg="white", bg="Black").place(x=50, y=160)
        self.alb = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.alb.place(x=120, y=160)

        tk.Label(self.ckdf, text="Sugar", font=("Times New Roman", 12), fg="white", bg="Black").place(x=60, y=190)
        self.sug = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.sug.place(x=120, y=190)
        
        tk.Label(self.ckdf, text="RBCs", font=("Times New Roman", 12), fg="white", bg="Black").place(x=60, y=220)
        self.rbc = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.rbc.place(x=120, y=220)
        
        tk.Label(self.ckdf, text="Pus Cells", font=("Times New Roman", 12), fg="white", bg="Black").place(x=40, y=250)
        self.pus = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.pus.place(x=120, y=250)

        tk.Label(self.ckdf, text="Pus Cell Cast", font=("Times New Roman", 12), fg="white", bg="Black").place(x=20, y=280)
        self.pcc = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.pcc.place(x=120, y=280)

        tk.Label(self.ckdf, text="Bacteria", font=("Times New Roman", 12), fg="white", bg="Black").place(x=50, y=310)
        self.bac = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.bac.place(x=120, y=310)

        tk.Label(self.ckdf, text="Blood Glucose", font=("Times New Roman", 12), fg="white", bg="Black").place(x=10, y=340)
        self.bg = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.bg.place(x=120, y=340)

        tk.Label(self.ckdf, text="Blood Urea", font=("Times New Roman", 12), fg="white", bg="Black").place(x=30, y=370)
        self.bu = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.bu.place(x=120, y=370)

        tk.Label(self.ckdf, text="Serum Creatinine", font=("Times New Roman", 12), fg="white", bg="Black").place(x=5, y=400)
        self.sc = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.sc.place(x=120, y=400)

#   ######

        tk.Label(self.ckdf, text="Sodium", font=("Times New Roman", 12), fg="white", bg="Black").place(x=390, y=70)
        self.sod = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.sod.place(x=450, y=70)

        tk.Label(self.ckdf, text="Potassium", font=("Times New Roman", 12), fg="white", bg="Black").place(x=370, y=100)
        self.pot = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.pot.place(x=450, y=100)

        tk.Label(self.ckdf, text="Hemoglobin", font=("Times New Roman", 12), fg="white", bg="Black").place(x=360, y=130)
        self.hb = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.hb.place(x=450, y=130)

        tk.Label(self.ckdf, text="Packed Cells", font=("Times New Roman", 12), fg="white", bg="Black").place(x=350, y=160)
        self.pcv = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.pcv.place(x=450, y=160)

        tk.Label(self.ckdf, text="WBCs", font=("Times New Roman", 12), fg="white", bg="Black").place(x=390, y=190)
        self.wbc = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.wbc.place(x=450, y=190)

        tk.Label(self.ckdf, text="RC", font=("Times New Roman", 12), fg="white", bg="Black").place(x=410, y=220)
        self.rc = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.rc.place(x=450, y=220)

        tk.Label(self.ckdf, text="Hypertension", font=("Times New Roman", 12), fg="white", bg="Black").place(x=350, y=250)
        self.htn = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.htn.place(x=450, y=250)

        tk.Label(self.ckdf, text="Diabetic Mellitus", font=("Times New Roman", 12), fg="white", bg="Black").place(x=330, y=280)
        self.dm = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.dm.place(x=450, y=280)

        tk.Label(self.ckdf, text="Coronary Artery Disease", font=("Times New Roman", 12), fg="white", bg="Black").place(x=290, y=310)
        self.cad = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.cad.place(x=460, y=310)

        tk.Label(self.ckdf, text="Appetite", font=("Times New Roman", 12), fg="white", bg="Black").place(x=370, y=340)
        self.apt = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.apt.place(x=450, y=340)

        tk.Label(self.ckdf, text="Physics", font=("Times New Roman", 12), fg="white", bg="Black").place(x=390, y=370)
        self.pe = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.pe.place(x=450, y=370)

        tk.Label(self.ckdf, text="Anemia", font=("Times New Roman", 12), fg="white", bg="Black").place(x=390, y=400)
        self.ane = tk.Entry(self.ckdf, font=("Times New Roman", 12), width=20)
        self.ane.place(x=450, y=400)



        tk.Button(self.ckdf, text="Logout", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_login).place(x=600, y=20)

        tk.Button(self.ckdf, text="Continue", font=("Times New Roman", 16, "bold"), fg="white", bg="Black", command=self.go_to_nxt).place(x=287, y=455)

        tk.Button(self.ckdf, text="Back", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_prev).place(x=20, y=20)
        
    def go_to_login(self):        
        cursor.execute("delete from tpt")
        conn.commit()
        self.ckdf.place_forget()  # Hide admin frame
        login.LoginPage(self.root)  # Show Login Page
        
    def go_to_prev(self):
        self.ckdf.place_forget()  # Hide admin frame
        select.SelectDisease(self.root)  # Show Login Page

        
    def go_to_nxt(self):
        # age = self.age.get()
        # bp = self.bp.get()
        # sg = self.sg.get()
        # alb = self.alb.get()
        # sug = self.sug.get()
        # rbc = self.rbc.get()
        # pus = self.pus.get()
        # pcc = self.pcc.get()
        # bac = self.bac.get()
        # bgr = self.bg.get()
        # bu = self.bu.get()
        # sc = self.sc.get()
        # sod = self.sod.get()
        # pot = self.pot.get()
        # hb = self.hb.get()
        # pcv = self.pcv.get()
        # wbc = self.wbc.get()
        # rc = self.rc.get()
        # htn = self.htn.get()
        # dm = self.dm.get()
        # cad = self.cad.get()
        # apt = self.apt.get()
        # pe = self.pe.get()
        # ane = self.ane.get()

        input_values = [
        self.age.get(), self.bp.get(), self.sg.get(), self.alb.get(), self.sug.get(), self.rbc.get(),
        self.pus.get(), self.pcc.get(), self.bac.get(), self.bg.get(), self.bu.get(), self.sc.get(),
        self.sod.get(), self.pot.get(), self.hb.get(), self.pcv.get(), self.wbc.get(), self.rc.get(),
        self.htn.get(), self.dm.get(), self.cad.get(), self.apt.get(), self.pe.get(), self.ane.get()
    ]
        
        processed_input = [float(val) for val in input_values]

        column_names = [
            'age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu',
            'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc', 'rc', 'htn', 'dm', 'cad',
            'appet', 'pe', 'ane'
        ]

        input_df = pd.DataFrame([processed_input], columns=column_names)

        res = model.predict(input_df)[0]

        cursor.execute("select * from tpt")
        r = cursor.fetchone()
        if r:
            page = self.agnus = r["a"]
            pname = self.nemes = r["nm"]
            pgender = self.genpac = r["g"]

        if res == 1:
            cursor.execute("Insert into tresult values (?,?,?,?,?)", (pname,page,pgender,'Chronic Kidney Disease','Positive'))
            conn.commit()
            # messagebox.showinfo("Prediction Result", "⚠️ Diabetic Nephropathy Detected!")
        else:
            cursor.execute("Insert into tresult values (?,?,?,?,?)", (pname,page,pgender,'Chronic Kidney Disease','Negative'))
            conn.commit()
            # messagebox.showinfo("Prediction Result", "✅ No Diabetic Nephropathy Detected.")

        # cursor.execute("Insert into tckd values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (age,bp,sg,alb,sug,rbc,pus,pcc,bac,bgr,bu,sc,sod,pot,hb,pcv,wbc,rc,htn,dm,cad,apt,pe,ane))
        # conn.commit()
        self.ckdf.place_forget()  # Hide admin frame
        result.ResultPage(self.root)  # Show Login Page


if __name__ == "__main__":
    root = tk.Tk()
    app = ChronicKidneyDisease(root)
    root.mainloop()