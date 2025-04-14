import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import login,select,result  # Import admin page file
import sqlite3, pandas as pd, joblib

model = joblib.load('DN_RF_Model.pkl')

conn = sqlite3.connect("tempdb.db")  # Creates or connects to the database
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

class DiabeticNephropathy:
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
        self.dnf = tk.Frame(self.root)
        self.dnf.place(relwidth=1, relheight=1)

        if self.bg_image:
            background_label = tk.Label(self.dnf, image=self.bg_image)
            background_label.image = self.bg_image
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Patiets details
        tk.Label(self.dnf, text=" Datas for Diabetic Nephropathy ", font=("Times New Roman", 16, "bold"), fg="white", bg="Black").place(x=200, y=20)
       
    #    ####

        tk.Label(self.dnf, text="Duration", font=("Times New Roman", 12), fg="white", bg="Black").place(x=50, y=70)
        self.dur = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.dur.place(x=120, y=70)

        tk.Label(self.dnf, text="D Retinopathy", font=("Times New Roman", 12), fg="white", bg="Black").place(x=20, y=110)
        self.dr = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.dr.place(x=120, y=110)

        tk.Label(self.dnf, text="Smoke", font=("Times New Roman", 12), fg="white", bg="Black").place(x=60, y=150)
        self.smoke = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.smoke.place(x=120, y=150)

        tk.Label(self.dnf, text="Drink", font=("Times New Roman", 12), fg="white", bg="Black").place(x=70, y=190)
        self.drink = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.drink.place(x=120, y=190)

        tk.Label(self.dnf, text="Age", font=("Times New Roman", 12), fg="white", bg="Black").place(x=70, y=230)
        self.ag = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.ag.place(x=120, y=230)
        
        tk.Label(self.dnf, text="Height", font=("Times New Roman", 12), fg="white", bg="Black").place(x=70, y=270)
        self.height = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.height.place(x=120, y=270)
        
        tk.Label(self.dnf, text="Weight", font=("Times New Roman", 12), fg="white", bg="Black").place(x=70, y=310)
        self.weight = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.weight.place(x=120, y=310)

        tk.Label(self.dnf, text="BMI", font=("Times New Roman", 12), fg="white", bg="Black").place(x=70, y=350)
        self.bmi = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.bmi.place(x=120, y=350)

        tk.Label(self.dnf, text="LDLC", font=("Times New Roman", 12), fg="white", bg="Black").place(x=70, y=390)
        self.ldlc = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.ldlc.place(x=120, y=390)

        tk.Label(self.dnf, text="SBP", font=("Times New Roman", 12), fg="white", bg="Black").place(x=70, y=430)
        self.sbp = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.sbp.place(x=120, y=430)

#   ######

        tk.Label(self.dnf, text="DBP", font=("Times New Roman", 12), fg="white", bg="Black").place(x=400, y=70)
        self.dbp = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.dbp.place(x=450, y=70)

        tk.Label(self.dnf, text="C-Peptide", font=("Times New Roman", 12), fg="white", bg="Black").place(x=365, y=110)
        self.cp = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.cp.place(x=450, y=110)

        tk.Label(self.dnf, text="Metformin", font=("Times New Roman", 12), fg="white", bg="Black").place(x=365, y=150)
        self.mtf = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.mtf.place(x=450, y=150)

        tk.Label(self.dnf, text="Lipid Drug", font=("Times New Roman", 12), fg="white", bg="Black").place(x=365, y=190)
        self.lip = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.lip.place(x=450, y=190)

        tk.Label(self.dnf, text="HbA1c", font=("Times New Roman", 12), fg="white", bg="Black").place(x=380, y=230)
        self.ha1c = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.ha1c.place(x=450, y=230)

        tk.Label(self.dnf, text="FBG", font=("Times New Roman", 12), fg="white", bg="Black").place(x=400, y=270)
        self.fbg = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.fbg.place(x=450, y=270)

        tk.Label(self.dnf, text="Triglycerides", font=("Times New Roman", 12), fg="white", bg="Black").place(x=350, y=310)
        self.tg = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.tg.place(x=450, y=310)

        tk.Label(self.dnf, text="T Cholesterol", font=("Times New Roman", 12), fg="white", bg="Black").place(x=350, y=350)
        self.tc = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.tc.place(x=450, y=350)

        tk.Label(self.dnf, text="HDLC", font=("Times New Roman", 12), fg="white", bg="Black").place(x=390, y=390)
        self.hdlc = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.hdlc.place(x=450, y=390)

        tk.Label(self.dnf, text="Insulin", font=("Times New Roman", 12), fg="white", bg="Black").place(x=390, y=430)
        self.ins = tk.Entry(self.dnf, font=("Times New Roman", 12), width=20)
        self.ins.place(x=450, y=430)

        tk.Button(self.dnf, text="Logout", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_login).place(x=600, y=20)

        tk.Button(self.dnf, text="Continue", font=("Times New Roman", 16, "bold"), fg="white", bg="Black", command=self.go_to_nxt).place(x=287, y=455)

        tk.Button(self.dnf, text="Back", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=self.go_to_prev).place(x=20, y=20)
        
    def go_to_login(self):        
        cursor.execute("delete from tpt")
        conn.commit()
        self.dnf.place_forget()  # Hide admin frame
        login.LoginPage(self.root)  # Show Login Page
        
    def go_to_prev(self):
        self.dnf.place_forget()  # Hide admin frame
        select.SelectDisease(self.root)  # Show Login Page

        
    def go_to_nxt(self):
        # age = self.ag.get()
        # dur = self.dur.get()
        # dret = self.dr.get()
        # smk = self.smoke.get()
        # drk = self.drink.get()
        # h = self.height.get()
        # w = self.weight.get()
        # bmi = self.bmi.get()
        # sbp = self.sbp.get()
        # dbp = self.dbp.get()
        # hb = self.ha1c.get()
        # fbg = self.fbg.get()
        # tg = self.tg.get()
        # tc = self.tc.get()
        # cp = self.cp.get()
        # hdlc = self.hdlc.get()
        # ldlc = self.ldlc.get()
        # ins = self.ins.get()
        # met = self.mtf.get()
        # lip = self.lip.get()

        # cursor.execute("Insert into tdn values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (age,dur,dret,smk,drk,h,w,bmi,sbp,dbp,hb,fbg,tg,cp,tc,hdlc,ldlc,ins,met,lip))
        # conn.commit()

        input_values = [
        self.ag.get(), self.dur.get(), self.dr.get(), self.smoke.get(), self.drink.get(), self.height.get(),
        self.weight.get(), self.bmi.get(), self.sbp.get(), self.dbp.get(), self.ha1c.get(), self.fbg.get(),
        self.tc.get(), self.cp.get(), self.tc.get(), self.hdlc.get(), self.ldlc.get(), self.ins.get(),
        self.mtf.get(), self.lip.get()
    ]
        
        processed_input = [float(val) for val in input_values]

        column_names = [
            'Age', 'Diabetes duration (y)', 'Diabetic retinopathy (DR)', 'Smoking', 'Drinking', 'Height(cm)',
            'Weight(kg)', 'BMI (kg/m2)', 'SBP (mmHg) ', 'DBP (mmHg)', 'HbA1c (%)', 'FBG (mmol/L)', 'TG（mmoll）',
            'C-peptide (ng/ml）', 'TC（mmoll）', 'HDLC（mmoll）', 'LDLC（mmoll）', 'Insulin', 'Metformin', 'Lipid lowering drugs'
        ]

        input_df = pd.DataFrame([processed_input], columns=column_names)

        res = model.predict(input_df)[0]

        cursor.execute("select * from tpt")
        r = cursor.fetchone()
        if r:
            page = self.agnus = r['a']
            pname = self.nemes = r["nm"]
            pgender = self.genpac = r["g"]

        if res == 1:
            cursor.execute("Insert into tresult values (?,?,?,?,?)", (pname,page,pgender,'Diabetic Nephropathy','Positive'))
            conn.commit()
            # messagebox.showinfo("Prediction Result", "⚠️ Diabetic Nephropathy Detected!")
        else:
            cursor.execute("Insert into tresult values (?,?,?,?,?)", (pname,page,pgender,'Diabetic Nephropathy','Negative'))
            conn.commit()
            # messagebox.showinfo("Prediction Result", "✅ No Diabetic Nephropathy Detected.")

        self.dnf.place_forget()  # Hide admin frame
        result.ResultPage(self.root)  # Show Login Page


if __name__ == "__main__":
    root = tk.Tk()
    app = DiabeticNephropathy(root)
    root.mainloop()