from tkinter.ttk import *
from tkinter import *
from datetime import datetime
import tkinter.messagebox
import json
import os
import base64
from cryptography.fernet import Fernet
from plyer import notification


def add():
    # ...............PERSONAL......................................................................
    passw = password.get()
    confpassw = confpassword.get()
    try:
        if(passw == '' or confpassw == ''):
            tkinter.messagebox.showwarning(
                '', 'Password should not be empty')
            return
        if(passw != confpassw):
            tkinter.messagebox.showwarning(
                '', 'Passwords do not match')
            return
    except NameError:
        tkinter.messagebox.showerror(
            'Error', 'Your password should only comprise of characters!')
        return
    l = last_name.get()  # '''last name'''
    fi = first_name.get()  # '''first name'''
    try:
        if(l == '' or fi == ''):
            tkinter.messagebox.showwarning(
                '', 'Last name or first name fields are empty')
            return
        if (l.isdigit() or fi.isdigit()):
            raise NameError
    except NameError:
        tkinter.messagebox.showerror(
            'Error', 'Your name should only comprise of characters!')
        return

    # try:
    #     if(len(fi.split(" ") < 2)):
    #         tkinter.messagebox.showwarning(
    #             '', 'Your first name or last name is missing')
    #         return
    # except:
    #     tkinter.messagebox.showwarning(
    #         '', 'Your first name or last name is missing')
    #     return
    
    y = year.get()  # '''year'''
    m = month.get()  # '''month'''
    d = day.get()  # '''day'''
    DOB = y+'/'+m+'/'+d  # '''DOB'''
    try:
        if(y == '' or m == '' or d == ''):
            tkinter.messagebox.showwarning(
                '', 'Date of birth field is empty')
            return
        import datetime
        datetime.datetime(int(y), int(m), int(d))
    except ValueError:
        tkinter.messagebox.showerror('Error', 'Enter valid DOB!')
        return

    s = gender.get()  # '''gender'''
    s = int(s)
    l2 = ['Male', 'Female', 'Other']

    p = phone.get()  # '''phone no.'''
    m = mobile.get()  # '''mobile no.'''
    try:
        if(p == '' or m == ''):
            tkinter.messagebox.showwarning(
                '', 'Phone number or mobile number field is empty')
            return
        if(p.isdigit() == False and m.isdigit() == False):
            raise ValueError
        if(len(p) and len(m) != 10):
            raise ValueError
    except ValueError:
        tkinter.messagebox.showerror(
            'Error', 'Phone number should only have 10 digits!')
        return

    e = email.get()  # '''email'''
    try:
        if(e == ''):
            tkinter.messagebox.showwarning(
                '', 'Email field is empty')
            return
        l5 = e.split('@')
        if(len(l5) != 2):
            raise IndexError
        l6 = l5[1].split('.')
        if(len(l6) != 2):
            raise IndexError
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()

        # using the key
        fernet = Fernet(key)

        # opening the encrypted file
        with open('database/user.json', 'rb') as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        count = 0
        # opening the file in write mode and
        # writing the decrypted data
        with open('database/user.json', 'wb') as dec_file:
            dec_file.write(decrypted)
        with open("database/user.json") as f:
            data = json.load(f)
            users = data['users']
            for user in users:
                if(user["email"] == e):
                    count += 1
        if(count > 0):
            tkinter.messagebox.showwarning(
                '', 'Email already registered')
            with open('filekey.key', 'rb') as filekey:
                key = filekey.read()

            # using the generated key
            fernet = Fernet(key)

            # opening the original file to encrypt
            with open('database/user.json', 'rb') as file:
                original = file.read()

            # encrypting the file
            encrypted = fernet.encrypt(original)

            # opening the file in write mode and
            # writing the encrypted data
            with open('database/user.json', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
            return
        else:
            with open('filekey.key', 'rb') as filekey:
                key = filekey.read()

            # using the generated key
            fernet = Fernet(key)

            # opening the original file to encrypt
            with open('database/user.json', 'rb') as file:
                original = file.read()

            # encrypting the file
            encrypted = fernet.encrypt(original)

            # opening the file in write mode and
            # writing the encrypted data
            with open('database/user.json', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)

    except IndexError:
        tkinter.messagebox.showerror('Error', 'Enter valid Email id!')
        return

    # ................PERM ADDRESS...........................................................
    st = street.get()
    lo = local.get()
    p_s = ps.get()
    p_o = po.get()
    d = district.get()
    ci = city.get()
    ur = ub.get()
    l4 = ['Urban', 'Rural']
    sta = state.get()
    co = country.get()

    pi = pin.get()
    if(pi == ''):
        tkinter.messagebox.showwarning(
            '', 'Please fill all the required fields')
        return
    if(len(pi) != 6):
        tkinter.messagebox.showerror('Error', 'Enter valid PIN!')
        return

    # ...............CURRENT ADD.........................................................
    cst = c_street.get()
    clo = c_local.get()
    cp_s = c_ps.get()
    cp_o = c_po.get()
    cd = c_district.get()
    cci = c_city.get()
    cur = c_ub.get()
    cur = int(cur)
    cl4 = ['Urban', 'Rural']
    csta = c_state.get()
    cco = c_country.get()

    cpi = c_pin.get()
    if(cpi == ''):
        tkinter.messagebox.showwarning(
            '', 'Please fill all the required fields')
        return
    if(len(cpi) != 6):
        tkinter.messagebox.showerror('Error', 'Enter valid PIN!')
        return

    # .......................................................................................

    if (l == '' or p == '' or fi == '' or y == '' or m == '' or d == '' or s == '' or m == '' or e == '' or
        st == '' or lo == '' or p_s == '' or p_o == '' or d == '' or ci == '' or ur == '' or sta == '' or co == '' or pi == '' or
            cst == '' or clo == '' or cp_s == '' or cp_o == '' or cd == '' or cci == '' or cur == '' or csta == '' or cco == '' or cpi == '' or re == ''):
        tkinter.messagebox.showwarning(
            '', 'Please fill all the required fields')
        return

    # ............................MARKS....................................................................................

    sch = entry1.get()
    boa = entry2.get()
    phys = entry3.get()
    phys = float(phys)
    if(phys == ''):
        tkinter.messagebox.showwarning('', 'Please enter your CGPA!')
        return

    zz = tkinter.messagebox.askyesno(
        "Application Form", 'Are you sure you want to submit?')
    if zz > 0:

        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()

        # using the key
        fernet = Fernet(key)

        # opening the encrypted file
        with open('database/user.json', 'rb') as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open('database/user.json', 'wb') as dec_file:
            dec_file.write(decrypted)

        with open("database/user.json") as f:
            data = json.load(f)
            users = data['users']
            y = {
                "last": l,
                "first": fi,
                "password": str(base64.b64encode(passw.encode("utf-8")))[1:],
                "dob": DOB,
                "gender": l2[s-1],
                "phone": p,
                "mobile": m,
                "email": e,
                "permaddress": [{
                    "street": st,
                    "locality": lo,
                    "police": p_s,
                    "post": p_o,
                    "district": d,
                    "city": ci,
                    "pin": pi,
                    "urban": l4[ur-1],
                    "state":sta,
                    "country":co
                }
                ],
                "curmaddress": [{
                    "street": cst,
                    "locality": clo,
                    "police": cp_s,
                    "post": cp_o,
                    "district": cd,
                    "city": cci,
                    "pin": cpi,
                    "urban": cl4[ur-1],
                    "state":csta,
                    "country":cco
                }
                ],
                "academic": [{
                    "college": sch,
                    "degree": boa,
                    "cgpa": phys,
                }
                ],
            }
            users.append(y)
            #json.dump(data, f, indent=4)
        with open("database/user.json", 'w') as f:
            json.dump(data, f, indent=4)

        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()

        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        with open('database/user.json', 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open('database/user.json', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        notification.notify(
            title="Signed Up!!",
            message="You have successfully signed up!",
            app_name="WeJob",
            app_icon="images/bell.ico",
            timeout=10
        )
        root.destroy()
        os.system("py login.py")
    else:
        return


def ex():
    ee = tkinter.messagebox.askyesno(
        "Alert", 'Are you sure you want to cancel?')
    if ee == True:
        root.destroy()
        return


def login():
    root.destroy()
    os.system("py login.py")


def cur_add():
    if(add_svar.get() == 1):
        c_street.insert(INSERT, street.get())
        c_local.insert(INSERT, local.get())
        c_ps.insert(INSERT, ps.get())
        c_po.insert(INSERT, po.get())
        c_district.insert(INSERT, district.get())
        c_city.insert(INSERT, city.get())

        if(ub.get() == 1):
            c_ub.set(1)
        elif(ub.get() == 2):
            c_ub.set(2)
        c_state.insert(INSERT, state.get())
        c_country.insert(INSERT, country.get())
        c_pin.insert(INSERT, pin.get())

    else:
        c_street.delete(0, END)
        c_local.delete(0, END)
        c_ps.delete(0, END)
        c_po.delete(0, END)
        c_district.delete(0, END)
        c_city.delete(0, END)
        c_ub.set(0)
        c_state.delete(0, END)
        c_country.delete(0, END)
        c_pin.delete(0, END)


######``````````````````````````````````````````````````````            FORM PAGE              ````````````````````````````````````````````````````````######
root = Tk()
root.title('Personal Information')
root.attributes('-fullscreen', True)

canvas = Canvas(root, width=1200, height=2000)

frame = Frame(canvas)
page = Frame(frame, height=2200, width=1600)
page.pack(expand=True, fill=BOTH)


logo = Frame(page)
logo.pack()
photo = PhotoImage(file="images/Logo.png").subsample(3)
Label(logo, image=photo).grid(column=0, row=0, rowspan=2)

########################################################            PERSONAL INFO                 ###########################################################
Label(logo, text="WeJob", font=('Aileron Bold', 22), fg='midnight blue').grid(
    column=1, row=0, columnspan=5, padx=10)
Label(logo, text="India's preferred job site", font=('Penna', 15),
      fg='dark slate blue').grid(column=1, row=1, sticky=W, padx=10)


Person_title = Label(page, fg='white', text='Personal Information',
                     bg='midnight Blue', width=235).pack(pady=10)
Name = Frame(page)
Name.pack()
Label(Name, text="Last Name: ").grid(column=0, row=0, sticky=E)
last_name = Entry(Name, width=100)
last_name.grid(column=1, row=0, columnspan=20)

Label(Name, text='First and Middle Name: ').grid(column=0, row=1, sticky=E)
first_name = Entry(Name, width=100)
first_name.grid(column=1, row=1, columnspan=20)

Label(Name, text='Password: ').grid(column=0, row=2, sticky=E)
password = Entry(Name, width=100, show="*")
password.grid(column=1, row=2, columnspan=20)

Label(Name, text='Confirm Password: ').grid(column=0, row=3, sticky=E)
confpassword = Entry(Name, width=100, show="*")
confpassword.grid(column=1, row=3, columnspan=20)


Label(Name, text='Date Of Birth: ').grid(column=0, row=4)
Label(Name, text='Year: ', width=10).grid(column=1, row=4, sticky=E)
year = Combobox(Name, width=5)
year['value'] = ('',)+tuple(i for i in range(1980, datetime.now().year))
year.current(0)
year.grid(column=2, row=4)
#
Label(Name, text='Month: ', width=10).grid(column=3, row=4, sticky=E, pady=10)
month = Combobox(Name, width=5)
month['value'] = ('',)+tuple(i for i in range(1, 13))
month.current(0)
month.grid(column=4, row=4)
#
Label(Name, text='Day: ', justif=RIGHT,  width=8).grid(column=5, row=4, padx=5)
day = Combobox(Name, width=5)
day['value'] = ('',)+tuple(i for i in range(1, 32))
day.current(0)
day.grid(column=6, row=4)

gender = StringVar()
gender.set(0)
Label(Name, text='Gender: ').grid(column=7, row=4, padx=20, sticky=E)
rb1 = Radiobutton(Name, text="Male", variable=gender,
                  value=1).grid(column=8, row=4)
rb2 = Radiobutton(Name, text="Female", variable=gender,
                  value=2).grid(column=9, row=4, padx=10)
rb3 = Radiobutton(Name, text="Other", variable=gender,
                  value=3).grid(column=10, row=4)


Label(Name, text='Landline: ').grid(column=0, row=5, sticky=E)
phone = Entry(Name, width=20)
phone.grid(column=1, row=5, columnspan=2)

Label(Name, text='Mobile Number: ').grid(column=3, row=5, sticky=E)
mobile = Entry(Name, width=20)
mobile.grid(column=4, row=5, columnspan=2)

Label(Name, text='Email Address: ').grid(
    column=6, row=5, columnspan=2, sticky=E, padx=7)
email = Entry(Name, width=26)
email.grid(column=8, row=5, columnspan=3)

#############################################################      ADDRESS       ###########################################################################

Label(page, text='Address', bg='midnight Blue',
      fg='white', width=235).pack(pady=10)
address_master = Frame(page)
address_master.pack()
##############PERMANENT##############
address = Frame(address_master)
address.pack(side=LEFT)
Label(address, text="Permanent:", fg='midnight blue',
      font=('bold', 10)).grid(column=0, row=0, sticky=W)
Label(address, text='Street Name and Number:').grid(
    column=0, row=1, columnspan=2)
street = Entry(address, width=64)
street.grid(column=2, row=1, columnspan=10, pady=2)
#
Label(address, text='Locality: ').grid(column=0, row=2)
local = Entry(address, width=20)
local.grid(column=1, row=2)
#
Label(address, text='Police Station: ').grid(column=2, row=2)
ps = Entry(address, width=20)
ps.grid(column=3, row=2)
#
Label(address, text='Post Office: ').grid(column=4, row=2)
po = Entry(address, width=20)
po.grid(column=5, row=2)
#
Label(address, text='District: ').grid(column=0, row=3)
district = Entry(address, width=20)
district.grid(column=1, row=3, pady=2)
#
Label(address, text='City: ').grid(column=2, row=3)
city = Entry(address, width=20)
city.grid(column=3, row=3)
#
ub = IntVar()
ub.set(0)
Radiobutton(address, text="Urban", variable=ub, value=1).grid(column=4, row=3)
Radiobutton(address, text="Rural", variable=ub, value=2).grid(column=5, row=3)
#
Label(address, text='State: ').grid(column=0, row=4)
state = Entry(address, width=20)
state.grid(column=1, row=4)
#
Label(address, text='Country: ').grid(column=2, row=4)
country = Entry(address, width=20)
country.grid(column=3, row=4)
#
Label(address, text='Pin: ').grid(column=4, row=4)
pin = Entry(address, width=20)
pin.grid(column=5, row=4)

#########CURRENT#############
c_address = Frame(address_master)
c_address.pack(side=LEFT, padx=50)
Label(c_address, text="Current:", fg='midnight blue',
      font=('bold', 10)).grid(column=0, row=0)
Label(c_address, text='Street Name and Number:').grid(
    column=0, row=1, columnspan=2)
c_street = Entry(c_address, width=64)
c_street.grid(column=2, row=1, columnspan=10, pady=2)
#
Label(c_address, text='Locality: ').grid(column=0, row=2)
c_local = Entry(c_address, width=20)
c_local.grid(column=1, row=2)
#
Label(c_address, text='Police Station: ').grid(column=2, row=2)
c_ps = Entry(c_address, width=20)
c_ps.grid(column=3, row=2)
#
Label(c_address, text='Post Office: ').grid(column=4, row=2)
c_po = Entry(c_address, width=20)
c_po.grid(column=5, row=2)
#
Label(c_address, text='District: ').grid(column=0, row=3)
c_district = Entry(c_address, width=20)
c_district.grid(column=1, row=3, pady=2)
#
Label(c_address, text='City: ').grid(column=2, row=3)
c_city = Entry(c_address, width=20)
c_city.grid(column=3, row=3)
#
c_ub = IntVar()
c_ub.set(0)
Radiobutton(c_address, text="Urban", variable=c_ub,
            value=1).grid(column=4, row=3)
Radiobutton(c_address, text="Rural", variable=c_ub,
            value=2).grid(column=5, row=3)
#
Label(c_address, text='State: ').grid(column=0, row=4)
c_state = Entry(c_address, width=20)
c_state.grid(column=1, row=4)
#
Label(c_address, text='Country: ').grid(column=2, row=4)
c_country = Entry(c_address, width=20)
c_country.grid(column=3, row=4)
#
Label(c_address, text='Pin: ').grid(column=4, row=4)
c_pin = Entry(c_address, width=20)
c_pin.grid(column=5, row=4)

add_svar = IntVar()
add_same = Checkbutton(page, text="Permanent and Current Address are the same", variable=add_svar,
                       onvalue=1, offvalue=0, width=100, fg='midnight blue', font=('bold', 10), command=cur_add)

add_same.pack()


#####################################################################     Educational Qualification     ############################################################
Label(page, text='Educational Qualification', bg='midnight blue',
      fg='white', width=234).pack(pady=10)

college = Label(root, text="College:").place(x=400, y=545)
degree = Label(root, text="Degree:").place(x=900, y=545)
cgpa = Label(root, text="CGPA:").place(x=650, y=600)
entry1 = Entry(root, width=50)
entry1.place(x=500, y=545)
entry2 = Entry(root, width=21)
entry2.place(x=950, y=545)
entry3 = Entry(root, width=25)
entry3.place(x=750, y=600)

#################################################################    Submit   #################################################################
actionbtn = Button(root, text='CANCEL', fg='white', bg='midnight blue',
                   width=10, command=ex).place(x=700, y=670)

actionbtn = Button(root, text='SUBMIT', fg='white', bg='midnight blue',
                   width=10, command=add).place(x=800, y=670)

actionbtn = Button(root, text='SIGN IN', fg='white', bg='midnight blue',
                   width=10, command=login).place(x=750, y=700)

Label(root, text="(Already have an account?)",
      fg='black').place(x=720, y=730)

canvas.create_window(0, 0, anchor='nw', window=frame)

canvas.update_idletasks()

canvas.configure()

canvas.pack(fill='both', expand=True, side='left')

mainloop()
