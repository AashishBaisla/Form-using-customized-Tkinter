from tkinter import *
import mysql.connector
from tkcalendar import Calendar, DateEntry
import customtkinter
#customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
window = customtkinter.CTk()
window.minsize(1000,800)
window.title("Registration Form - Created by Aashish Baisla")
window.configure(border=20)
window.grid_columnconfigure([0,1,2,3,4], weight=1)
window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13], weight=1)
#window.config(padx=20, bg="#FF9966")
window.wm_iconbitmap('form_icon.ico')
screen_width = window.winfo_screenwidth()
screen_width = window.winfo_screenheight()
#window.attributes('-fullscreen', True)
#window.wm_attributes('-transparentcolor','yellow')

#Get all values from Registration Form
def store_in_DB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="registrations_2022"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO reg_details (First_Name, Last_Name, Gender, Date_of_Birth, Email, Contact_No, Blood_Group, Country, State, Address, Skills) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (first_name.get(), last_name.get(), gender.get(), sel.get(), email.get(), contact.get(), blood.get(), country.get(), state.get(),
           Entry_Address.get(), f"{var_python.get()} {var_C.get()} {var_Java.get()} {var_SQL.get()}")

    mycursor.execute(sql, val)
    mydb.commit()

    Label_Submit = Label(text="Details Submitted!", fg="blue", font="Ariel 15")
    Label_Submit.grid(row=13, column=0, columnspan=4)

def check_entries(event=None):
    if ( first_name.get()=='' or last_name.get()=='' or gender.get()=='' or email.get()=='' or contact.get()=='' or blood.get()==''
            or country.get()=='' or state.get()=='' or Entry_Address.get()=='' or f"{var_python.get()} {var_C.get()} {var_Java.get()} {var_SQL.get()}"=='   '):

        Label_Error = customtkinter.CTkLabel(text="Please fill all Details!",fg_color="red", pady=5)
        Label_Error.grid(row=13, column=0, columnspan=5)
        def delay_in_label(l):
            l.after(2000, l.destroy)
        delay_in_label(Label_Error)

    else:
        store_in_DB()

def clear_all_details():
    first_name.set(''), last_name.set(''), gender.set(''), sel.set('YYYY-MM-DD'), email.set(''), contact.set(''),
    blood.set(''), country.set(''), state.set(''), address.set(''),
    var_python.set(''), var_C.set(''), var_Java.set(''), var_SQL.set('')

#Variables for storing inserted data
first_name = customtkinter.StringVar()
last_name = customtkinter.StringVar()
gender = customtkinter.StringVar()
sel= customtkinter.StringVar()
email = customtkinter.StringVar()
contact = customtkinter.StringVar()
blood = customtkinter.StringVar()
country = customtkinter.StringVar()
state = customtkinter.StringVar()
address = customtkinter.StringVar()
#Variables for storing checkbutton values
var_python = customtkinter.StringVar()
var_C = customtkinter.StringVar()
var_Java = customtkinter.StringVar()
var_SQL = customtkinter.StringVar()

#Title
Title_Label = customtkinter.CTkLabel(window, text="Registration Form - Created by Aashish Baisla")
Title_Label.grid(row=0, column=0, columnspan=5, pady=10)

#Label & Entry
firsName = customtkinter.CTkLabel(window, text="First Name").grid(row=1, column=0, padx=4, pady=4, sticky="w")
Entry_first_Name = customtkinter.CTkEntry(window,textvariable=first_name, corner_radius=15)
Entry_first_Name.grid(row=1, column=1, columnspan=4, padx=50, pady=4, ipady=7, sticky="we")

Label_Lang = customtkinter.CTkLabel(window, text="Last Name").grid(row=2, column=0, padx=4, pady=4, sticky="w")
Entry_last_Name = customtkinter.CTkEntry(window, textvariable=last_name, corner_radius=15)
Entry_last_Name.grid(row=2, column=1, columnspan=4, padx=50, pady=4, ipady=7, sticky="we")

Label_Gender = customtkinter.CTkLabel(window, text="Gender").grid(row=3, column=0, padx=4, pady=4, sticky="w")
Entry_Gender1 = customtkinter.CTkRadioButton(window, text="Male", variable=gender, value="Male")
Entry_Gender1.grid(row=3, column=1, padx=100, pady=6, sticky="we")
Entry_Gender2 = customtkinter.CTkRadioButton(window, text="Female", variable=gender, value="Female")
Entry_Gender2.grid(row=3, column=2, sticky="we")
Entry_Gender3 = customtkinter.CTkRadioButton(window, text="Other", variable=gender, value="Other")
Entry_Gender3.grid(row=3, column=3, sticky="e")

Label_Date = customtkinter.CTkLabel(window, text="Date of Birth").grid(row=4, column=0, padx=4, pady=4, sticky="w")
Entry_Date = DateEntry(window, textvariable=sel, locale='en_US', date_pattern='YYYY-MM-DD')
Entry_Date.grid(row=4, column=1, padx=50, pady=4, ipady=7, sticky="w")

Label_Email = customtkinter.CTkLabel(window, text="Email").grid(row=5, column=0, padx=4, pady=4, sticky="w")
Entry_Email = customtkinter.CTkEntry(window, textvariable=email, corner_radius=15)
Entry_Email.grid(row=5, column=1, columnspan=4, padx=50, pady=4, ipady=7, sticky="we")

Label_Contact = customtkinter.CTkLabel(window, text="Contact No").grid(row=6, column=0, padx=4, pady=4, sticky="w")
Entry_Contact = customtkinter.CTkEntry(window, textvariable=contact, corner_radius=15)
Entry_Contact.grid(row=6, column=1, columnspan=4, padx=50, pady=4, ipady=7, sticky="we")

Label_Blood_Grp = customtkinter.CTkLabel(window, text="Blood Group").grid(row=7, column=0, padx=4, pady=4, sticky="w")
Entry_Blood_Grp = customtkinter.CTkEntry(window, textvariable=blood, corner_radius=15)
Entry_Blood_Grp.grid(row=7, column=1, columnspan=4, padx=50, pady=4, ipady=7, sticky="we")

Label_Country = customtkinter.CTkLabel(window, text="Country").grid(row=8, column=0, padx=4, pady=4, sticky="w")
Entry_Country = customtkinter.CTkOptionMenu(window, height=1, corner_radius=15, fg_color="grey", variable=country, values = ['India', 'Australia', 'United States', 'United Kingdom', 'Germany', 'Japan', 'France', 'Russia'])
Entry_Country.grid(row=8, column=1, padx=50, pady=4, ipady=7, sticky="w")

Label_State = customtkinter.CTkLabel(window, text="State").grid(row=9, column=0, padx=4, pady=4, sticky="w")
Entry_State = customtkinter.CTkEntry(window, textvariable=state, corner_radius=15)
Entry_State.grid(row=9, column=1, columnspan=4, padx=50, pady=4, ipady=7, sticky="we")

Label_Address = customtkinter.CTkLabel(window, text="Address").grid(row=10, column=0, padx=4, pady=4, sticky="w")
Entry_Address = customtkinter.CTkEntry(window, textvariable=address, corner_radius=15)
Entry_Address.grid(row=10, column=1, columnspan=4, padx=50, pady=4, ipady=7, sticky="we")

Label_Skills = customtkinter.CTkLabel(window, text="Skills").grid(row=11, column=0, padx=4, pady=4, sticky="w")
Skills_Check1 = customtkinter.CTkCheckBox(window, text="Python", variable=var_python, onvalue="Python", offvalue='')
Skills_Check1.grid(row=11, column=1, padx=20)
Skills_Check2 = customtkinter.CTkCheckBox(window, text="C/C++", variable=var_C, onvalue="C/C++", offvalue='')
Skills_Check2.grid(row=11, column=2, sticky="w")
Skills_Check3 = customtkinter.CTkCheckBox(window, text="Java", variable=var_Java, onvalue="Java", offvalue='')
Skills_Check3.grid(row=11, column=3, sticky="w")
Skills_Check4 = customtkinter.CTkCheckBox(window, text="SQL", variable=var_SQL, onvalue="SQL", offvalue='')
Skills_Check4.grid(row=11, column=4, sticky="w")

#Button to Submit the Registration form
Button_Submit = customtkinter.CTkButton(window, text="SUBMIT", width=20, command=check_entries, corner_radius=8)
Button_Submit.grid(row=12, column=1, pady=10)

Button_Clear = customtkinter.CTkButton(window, text="Clear", width=20, command=clear_all_details, corner_radius=8)
Button_Clear.grid(row=12, column=3, pady=10)

window.mainloop()