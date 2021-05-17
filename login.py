from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import base64  # encoding and decoding
from cryptography.fernet import Fernet  # pip install cryptography
import time
from plyer import notification


# Clearing the cookie on start
with open("database/cookie.json") as f:
    cookiedata = json.load(f)
    delete = cookiedata['log']
    delete1 = cookiedata['resume']
delete.clear()
delete1.clear()
with open("database/cookie.json", 'w') as f:
    json.dump(cookiedata, f, indent=4)

# ---------------------------------------------------------------Login Function --------------------------------------


def clear():
    userentry.delete(0, END)
    passentry.delete(0, END)


def login():
    # Checking if the username and password is blank
    if user_name.get() == "" or password.get() == "":
        messagebox.showerror(
            "Error", "Enter User Name And Password", parent=win)
    else:
        try:
            count = 0
            position = -1
            # Checking if key is present and reading the key
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

            # opening the user.json file and loading
            with open("database/user.json") as f:
                data = json.load(f)
                users = data['users']
                for user in users:
                    position += 1
                    if(user["email"] == user_name.get() and base64.b64decode(user["password"]).decode("utf-8") == password.get()):
                        notification.notify(
                            title="LOGGED IN!",
                            message="You have successfully logged in!",
                            app_name="WeJob",
                            app_icon="images/bell.ico",
                            timeout=10
                        )
                        count += 1
                        break
            addition = {
                "position": position
            }
            if(count > 0):
                with open("database/cookie.json") as f:
                    data = json.load(f)
                    users = data['log']
                    positioned = data['log']
                with open("database/user.json") as f:
                    datauser = json.load(f)
                    userdata = datauser['users'][position]
                users.append(userdata)
                positioned.append(addition)
                with open("database/cookie.json", 'w') as f:
                    json.dump(data, f, indent=4)
            else:
                messagebox.showerror(
                    "Error", "Details inputted are wrong", parent=win)
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
            win.destroy()
            os.system("py resume/resume.py")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Error due to : {str(es)}", parent=win)


def sign_up():
    win.destroy()
    os.system("py reg.py")


# ---------------------------------------------------------------End Login Function ---------------------------------


# ------------------------------------------------------------ Login Window -----------------------------------------

# Tkinter window/app is created here
win = Tk()

# app title
win.title("WeJob Login")

# window size is set to fullscreen
win.attributes("-fullscreen", True)


# heading, usernam, userpass labels are created and placed
heading = Label(win, text="Login", font='Verdana 30 bold')
heading.place(x=680, y=250)

username = Label(win, text="Email Address:", font='Verdana 15 bold')
username.place(x=480, y=350)

userpass = Label(win, text="Password :", font='Verdana 15 bold')
userpass.place(x=480, y=430)

# They read the image and set the image at the top of the window
logo = Frame(win)
logo.pack()
photo = PhotoImage(file="images/Logo.png").subsample(3)
Label(logo, image=photo).grid(column=0, row=0, rowspan=2)
Label(logo, text="WeJob", font=('Aileron Bold', 50), fg='midnight blue').grid(
    column=1, row=0, columnspan=5, padx=10)
Label(logo, text="India's preferred job site", font=('Penna', 25),
      fg='dark slate blue').grid(column=1, row=1, padx=10)

# Creating the blue line
Label(win,
      bg='midnight Blue', width=235).pack(pady=10)

# Entry Box/ Text input
user_name = StringVar()
password = StringVar()

userentry = Entry(win, width=40, textvariable=user_name)
userentry.place(x=680, y=356)

passentry = Entry(win, width=40, show="*", textvariable=password)
passentry.place(x=680, y=436)


# button login and clear

btn_login = Button(win, text="Login", font='Verdana 13 bold',
                   fg='white', bg='midnight blue', command=login)
btn_login.place(x=780, y=500)


btn_login = Button(win, text="Clear", font='Verdana 13 bold',
                   fg='white', bg='midnight blue', command=clear)
btn_login.place(x=530, y=500)

# signup button

sign_up_btn = Button(win, text="Switch To Sign Up",
                     font='Verdana 10 bold', command=sign_up, width=20, fg='white', bg='midnight blue')
sign_up_btn.place(x=1200, y=200)


win.mainloop()

# -------------------------------------------------------------------------- End Login Window ---------------------------------------------------
