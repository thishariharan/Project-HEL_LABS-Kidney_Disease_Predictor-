import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

                                                                            # Initialize the main window


root = tk.Tk()
root.title("HEL Labs")
root.geometry("700x500")



# Load the background image from the system
try:
    # Use r to make the string a raw string, or double backslashes for Windows paths
    # background_image = Image.open(r"D:\stds\Final Year Project - Disease Prediction\The Application\App\Images\page 1.png")
    background_image = Image.open(r"Images\page 1.png")
    background_image = background_image.resize((700, 500), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
    bg_image = ImageTk.PhotoImage(background_image)
except Exception as e:
    print(f"Error loading background image: {e}")
    bg_image = None
    
# Frame 1: Login Page
login_frame = tk.Frame(root)
login_frame.place(relwidth=1, relheight=1)

# Set the background image login page
if bg_image:
    background_label = tk.Label(root, image=bg_image)
    background_label.image = bg_image  # Keep a reference to avoid garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add username label and entry
username_label = tk.Label(root, text="Username:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black")
username_label.place(x=200, y=298)
username_entry = tk.Entry(root, font=("Times New Roman", 12), width=20)
username_entry.place(x=300, y=300)

# Add password label and entry
password_label = tk.Label(root, text="Password:", font=("Times New Roman", 14, "bold"), fg="white", bg="Black")
password_label.place(x=200, y=348)
password_entry = tk.Entry(root, font=("Times New Roman", 12), width=20, show="*")
password_entry.place(x=300, y=350)

# Define a function to show the second page (patient details page)
def show_patient_page():
    login_frame.place_forget()  # Hide the login page
    patient_frame.place(relwidth=1, relheight=1)  # Show the patient details page

# Define a function for the login button
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username=="Kumar007" and password=="helloworld":
        if username and password:
            messagebox.showinfo("Login", "Login successful!")
        # Code to proceed to the next page goes here
    else:
        messagebox.showwarning("Login", "Please enter both username and password")

# Add login button
login_button = tk.Button(root, text="Login", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=show_patient_page)
login_button.place(x=320, y=400)



                                                                            # Frame 2: Patient Details Page
patient_frame = tk.Frame(root)

try:
    # Replace with the correct path to the second image
    # second_background_image = Image.open(r"D:\stds\Final Year Project - Disease Prediction\The Application\Phase - 1\Images\others.png")
    second_background_image = Image.open(r"Images\others.png")
    second_background_image = second_background_image.resize((700, 500), Image.LANCZOS)
    patient_bg_image = ImageTk.PhotoImage(second_background_image)
except Exception as e:
    print(f"Error loading second background image: {e}")
    patient_bg_image = None

# Set the second background image on the patient frame
if patient_bg_image:
    patient_background_label = tk.Label(patient_frame, image=patient_bg_image)
    patient_background_label.image = patient_bg_image  # Keep a reference to avoid garbage collection
    patient_background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Patiets details
patient_name_label = tk.Label(patient_frame, text=" Patient Details ", font=("Times New Roman", 16, "bold"), fg="white", bg="Black")
patient_name_label.place(x=270, y=60)

# Add patient name label and entry
patient_name_label = tk.Label(patient_frame, text="Name", font=("Times New Roman", 14, "bold"), fg="white", bg="Black")
patient_name_label.place(x=200, y=128)
patient_name_entry = tk.Entry(patient_frame, font=("Times New Roman", 12), width=20)
patient_name_entry.place(x=300, y=130)

# Add age label and entry
age_label = tk.Label(patient_frame, text="Age", font=("Times New Roman", 14, "bold"), fg="white", bg="Black")
age_label.place(x=200, y=178)
age_entry = tk.Entry(patient_frame, font=("Times New Roman", 12), width=20)
age_entry.place(x=300, y=180)

# Add height label and entry
height_label = tk.Label(patient_frame, text="Height", font=("Times New Roman", 14, "bold"), fg="white", bg="Black")
height_label.place(x=200, y=228)
height_entry = tk.Entry(patient_frame, font=("Times New Roman", 12), width=20)
height_entry.place(x=300, y=230)

# Add weight label and entry
weight_label = tk.Label(patient_frame, text="Weight", font=("Times New Roman", 14, "bold"), fg="white", bg="Black")
weight_label.place(x=200, y=278)
weight_entry = tk.Entry(patient_frame, font=("Times New Roman", 12), width=20)
weight_entry.place(x=300, y=280)

# Add gender label and dropdown menu
gender_label = tk.Label(patient_frame, text="Gender", font=("Times New Roman", 14, "bold"), fg="white", bg="Black")
gender_label.place(x=200, y=334)
gender_var = tk.StringVar()
gender_var.set("Select one")  # Default value
gender_dropdown = tk.OptionMenu(patient_frame, gender_var, "Male", "Female")
gender_dropdown.config(font=("Times New Roman", 12))
gender_dropdown.place(x=300, y=330)

# Define a function to go back to the login page appears in all pages exept 1st page
def login():
    patient_frame.place_forget()  # Hide the patient details page
    login_frame.place(relwidth=1, relheight=1)  # Show the login page

# Continue button (for next page or action)
def select_page():
    patient_frame.place_forget()  # Hide the login page
    options_frame.place(relwidth=1, relheight=1)  # Show the patient details page

def continue_1():
    patient_name = patient_name_entry.get()
    age = age_entry.get()
    height = height_entry.get()
    weight = weight_entry.get()
    gender = gender_var.get()

    # Here, you can add validation or actions to proceed further.
    messagebox.showinfo("Patient Details", f"Patient {patient_name} registered successfully!")
    # You can proceed with further actions, such as saving the data or moving to another page.

# Back button (to go back to the login page)
back_button = tk.Button(patient_frame, text="Back", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=login)
back_button.place(x=25, y=25)

continue_button = tk.Button(patient_frame, text="Continue", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=select_page)
continue_button.place(x=300, y=400)


                                                                    # Frame 3 - Selection of Disease


options_frame = tk.Frame(root)

# Load the background image for the options page
try:
    # options_background_image = Image.open(r"D:\stds\Final Year Project - Disease Prediction\The Application\Phase - 1\Images\others.png")
    options_background_image = Image.open(r"Images\others.png")
    options_background_image = options_background_image.resize((700, 500), Image.LANCZOS)
    options_bg_image = ImageTk.PhotoImage(options_background_image)
except Exception as e:
    print(f"Error loading options background image: {e}")
    options_bg_image = None

# Set the background image on the options frame
if options_bg_image:
    options_background_label = tk.Label(options_frame, image=options_bg_image)
    options_background_label.image = options_bg_image  # Keep a reference
    options_background_label.place(x=0, y=0, relwidth=1, relheight=1)

option_label = tk.Label(options_frame, text=" Select the Disease Prediction Model ", font=("Times New Roman", 16, "bold"), fg="white", bg="Black")
option_label.place(x=180, y=80)

# To DN Page
def to_dn():
    options_frame.place_forget()  # Hide the login page 
    dn_frame.place(relwidth=1, relheight=1)  # Show the patient details page

# To CKD Page
def to_ckd():
    options_frame.place_forget()  # Hide the login page 
    ckd_frame.place(relwidth=1, relheight=1)  # Show the patient details page


#Diabetic Nephropathy Button
dn_button = tk.Button(options_frame, text=" Diabetic Nephropathy \n by \n Random Forest ", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=to_dn)
dn_button.place(x=80, y=150)

#Chronic Kidney Disease Button
ckd_button = tk.Button(options_frame, text=" Chronic Kidney Disease \n by \n Random Forest ", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=to_ckd)
ckd_button.place(x=370, y=150)


# Back button (for next page or action)
def op_to_pat():
    options_frame.place_forget()  # Hide the login page 
    patient_frame.place(relwidth=1, relheight=1)  # Show the patient details page

# Back button (to go back to the login page)
back_button = tk.Button(options_frame, text="Back", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=op_to_pat)
back_button.place(x=25, y=25)


                                                                        # DN Frame - 4

dn_frame = tk.Frame(root)

# Load the background image for the options page
try:
    # dn_background_image = Image.open(r"D:\stds\Final Year Project - Disease Prediction\The Application\Phase - 1\Images\others.png")
    dn_background_image = Image.open(r"Images\others.png")
    dn_background_image = dn_background_image.resize((700, 500), Image.LANCZOS)
    dn_bg_image = ImageTk.PhotoImage(dn_background_image)
except Exception as e:
    print(f"Error loading options background image: {e}")
    dn_bg_image = None

# Set the background image on the options frame
if dn_bg_image:
    dn_background_label = tk.Label(dn_frame, image=dn_bg_image)
    dn_background_label.image = dn_bg_image  # Keep a reference
    dn_background_label.place(x=0, y=0, relwidth=1, relheight=1)

dn_label = tk.Label(dn_frame, text=" Datas for Diabetic Nephropathy ", font=("Times New Roman", 16, "bold"), fg="white", bg="Black")
dn_label.place(x=200, y=50)

dr_label = tk.Label(dn_frame, text="DR", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=70, y=100)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=120, y=100)

dr_label = tk.Label(dn_frame, text="DN", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=70, y=150)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=120, y=150)

dr_label = tk.Label(dn_frame, text="Smk", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=70, y=200)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=120, y=200)

dr_label = tk.Label(dn_frame, text="Drk", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=70, y=250)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=120, y=250)

dr_label = tk.Label(dn_frame, text="BMI", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=70, y=300)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=120, y=300)

dr_label = tk.Label(dn_frame, text="SBP", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=70, y=350)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=120, y=350)

dr_label = tk.Label(dn_frame, text="DBP", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=70, y=400)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=120, y=400)

dr_label = tk.Label(dn_frame, text="C-P", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=70, y=450)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=120, y=450)

dr_label = tk.Label(dn_frame, text="Mtf", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=400, y=100)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=450, y=100)

dr_label = tk.Label(dn_frame, text="LiD", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=400, y=150)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=450, y=150)

dr_label = tk.Label(dn_frame, text="HA1c", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=400, y=200)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=450, y=200)

dr_label = tk.Label(dn_frame, text="FBG", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=400, y=250)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=450, y=250)

dr_label = tk.Label(dn_frame, text="TG", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=400, y=300)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=450, y=300)

dr_label = tk.Label(dn_frame, text="TC", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=400, y=350)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=450, y=350)

dr_label = tk.Label(dn_frame, text="HDLC", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=400, y=400)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=450, y=400)

dr_label = tk.Label(dn_frame, text="Ins", font=("Times New Roman", 12), fg="white", bg="Black")
dr_label.place(x=400, y=450)
dr_entry = tk.Entry(dn_frame, font=("Times New Roman", 12), width=20)
dr_entry.place(x=450, y=450)

continue_button = tk.Button(dn_frame, text="Continue", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=select_page)
continue_button.place(x=300, y=460)

# Back button (for next page or action)
def dn_to_op():
    dn_frame.place_forget()  # Hide the login page 
    options_frame.place(relwidth=1, relheight=1)  # Show the patient details page

# Back button (to go back to the login page)
back_button = tk.Button(dn_frame, text="Back", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=dn_to_op)
back_button.place(x=25, y=25)



                                                                        # CKD Frame - 5


ckd_frame = tk.Frame(root)

# Load the background image for the options page
try:
    # ckd_background_image = Image.open(r"D:\stds\Final Year Project - Disease Prediction\The Application\Phase - 1\Images\others.png")
    ckd_background_image = Image.open(r"Images\others.png")
    ckd_background_image = ckd_background_image.resize((700, 500), Image.LANCZOS)
    ckd_bg_image = ImageTk.PhotoImage(ckd_background_image)
except Exception as e:
    print(f"Error loading options background image: {e}")
    options_bg_image = None

# Set the background image on the options frame
if ckd_bg_image:
    ckd_background_label = tk.Label(ckd_frame, image=ckd_bg_image)
    ckd_background_label.image = ckd_bg_image  # Keep a reference
    ckd_background_label.place(x=0, y=0, relwidth=1, relheight=1)

ckd_label = tk.Label(ckd_frame, text=" Datas for Chronic Kidney Disease ", font=("Times New Roman", 16, "bold"), fg="white", bg="Black")
ckd_label.place(x=200, y=50)

ckd_label = tk.Label(ckd_frame, text="BP", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=70, y=100)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=120, y=100)

ckd_label = tk.Label(ckd_frame, text="SG", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=70, y=130)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=120, y=130)

ckd_label = tk.Label(ckd_frame, text="Alb", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=70, y=160)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=120, y=160)

ckd_label = tk.Label(ckd_frame, text="Sg", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=70, y=190)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=120, y=190)

ckd_label = tk.Label(ckd_frame, text="rbc", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=70, y=220)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=120, y=220)

ckd_label = tk.Label(ckd_frame, text="pc", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=70, y=250)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=120, y=250)

ckd_label = tk.Label(ckd_frame, text="pcc", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=70, y=280)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=120, y=280)

ckd_label = tk.Label(ckd_frame, text="Bac", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=70, y=310)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=120, y=310)

ckd_label = tk.Label(ckd_frame, text="BGR", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=70, y=340)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=120, y=340)

ckd_label = tk.Label(ckd_frame, text="BUr", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=70, y=370)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=120, y=370)

ckd_label = tk.Label(ckd_frame, text="SCr", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=70, y=400)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=120, y=400)

ckd_label = tk.Label(ckd_frame, text="Sod", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=400, y=100)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=450, y=100)

ckd_label = tk.Label(ckd_frame, text="Pot", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=400, y=130)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=450, y=130)

ckd_label = tk.Label(ckd_frame, text="Hb", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=400, y=160)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=450, y=160)

ckd_label = tk.Label(ckd_frame, text="PCV", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=400, y=190)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=450, y=190)

ckd_label = tk.Label(ckd_frame, text="wbc", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=400, y=220)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=450, y=220)

ckd_label = tk.Label(ckd_frame, text="HyT", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=400, y=250)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=450, y=250)

ckd_label = tk.Label(ckd_frame, text="DM", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=400, y=280)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=450, y=280)

ckd_label = tk.Label(ckd_frame, text="CAD", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=400, y=310)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=450, y=310)

ckd_label = tk.Label(ckd_frame, text="Ape", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=400, y=340)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=450, y=340)

ckd_label = tk.Label(ckd_frame, text="Phy", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=400, y=370)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=450, y=370)

ckd_label = tk.Label(ckd_frame, text="Ane", font=("Times New Roman", 12), fg="white", bg="Black")
ckd_label.place(x=400, y=400)
ckd_entry = tk.Entry(ckd_frame, font=("Times New Roman", 12), width=20)
ckd_entry.place(x=450, y=400)

continue_button = tk.Button(ckd_frame, text="Continue", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=select_page)
continue_button.place(x=300, y=440)

# Back button (for next page or action)
def ckd_to_op():
    ckd_frame.place_forget()  # Hide the login page 
    options_frame.place(relwidth=1, relheight=1)  # Show the patient details page

# Back button (to go back to the login page)
back_button = tk.Button(ckd_frame, text="Back", font=("Times New Roman", 14, "bold"), fg="white", bg="Black", command=ckd_to_op)
back_button.place(x=25, y=25)


# Run the Tkinter main loop
root.mainloop()
