from tkinter.ttk import *
from tkinter import *
from datetime import datetime
import time
import tkinter.messagebox
import json
import os
from tkinter.filedialog import askopenfilename
from cryptography.fernet import Fernet
from PIL import Image
import pathlib

# logo
root = Tk()
root.title('Personal Information')
root.attributes('-fullscreen', True)

canvas = Canvas(root, width=1200, height=5000)
scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)

frame = Frame(canvas)
page = Frame(frame, height=4000, width=1600)
page.pack(expand=True, fill=BOTH)
logo = Frame(page)
logo.pack()
photo = PhotoImage(file="images/Logo.png").subsample(3)
Label(logo, image=photo).grid(column=0, row=0, rowspan=2)
Label(logo, text="WeJob", font=('Aileron Bold', 22), fg='midnight blue').grid(
    column=1, row=0, columnspan=5, padx=10)
Label(logo, text="India's preferred job site", font=('Penna', 15),
      fg='dark slate blue').grid(column=1, row=1, sticky=W, padx=10)
Res = Label(page, fg='midnight Blue', text='RESUME',
            font=("Times", 25, "bold")).pack(pady=10)
xm = Label(page, fg='red', text='Whenever you apply to an internship or fresher job, this is the resume that the employer will see. Always make sure it is up to date.', font=("Times", 15)).pack(pady=2)

# Next Page


def onsubmit():
    if(tech.get("1.0", "end-1c") == '' or soft.get("1.0", "end-1c") == '' or anyskill.get("1.0", "end-1c") == '' or text1.get("1.0", "end-1c") == ''
       or text2.get("1.0", "end-1c") == '' or text3.get("1.0", "end-1c") == '' or text4.get("1.0", "end-1c") == '' or text5.get("1.0", "end-1c") == ''
       or text6.get("1.0", "end-1c") == '' or anyact.get("1.0", "end-1c") == ''):
        tkinter.messagebox.showwarning(
            '', 'One of the inputs are empty!')
        return
    y = {
        "tskills": tech.get("1.0", "end-1c"),
        "sskills": soft.get("1.0", "end-1c"),
        "anyskill": anyskill.get("1.0", "end-1c"),
        "reference": [
            {
                "name": text1.get("1.0", "end-1c"),
                "jobt": text2.get("1.0", "end-1c"),
                "company": text3.get("1.0", "end-1c"),
                "address": text4.get("1.0", "end-1c"),
                "contact": text5.get("1.0", "end-1c"),
                "email": text6.get("1.0", "end-1c")
            }
        ],
        "anyact": anyact.get("1.0", "end-1c")
    }
    # -----------------------------------------------------------------------------
    with open("database/cookie.json") as f:
        data = json.load(f)
        users = data['resume']
        positionof = data['log'][1]['position']
    # Saving in user database
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
        users = data['users'][positionof]
    users.update(y)
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
    os.system("py builder/builder.py")
    root.destroy()
    # ------------------- PROGRESS BAR ---------------- #
    # Create the master object
    # Create the master object

    def disable_event():
        pass
    master = Tk()
    master.title("Loading")
    master.geometry('235x40+300+100')
    master.protocol("WM_DELETE_WINDOW", disable_event)
    # Create a progressbar widget
    progress_bar = Progressbar(master, orient="horizontal",
                               mode="determinate", maximum=100, value=0)

    # And a label for it
    label_1 = Label(master, text="Your resume is building")

    # Use the grid manager
    label_1.grid(row=0, column=0)
    progress_bar.grid(row=0, column=1)

    # Necessary, as the master object needs to draw the progressbar widget
    # Otherwise, it will not be visible on the screen
    master.update()

    progress_bar['value'] = 0
    master.update()

    while progress_bar['value'] < 100:
        progress_bar['value'] += 10
        # Keep updating the master object to redraw the progress bar
        master.update()
        time.sleep(0.5)
        if(progress_bar['value'] == 100):
            ee = tkinter.messagebox.askyesno(
                "Application Form", 'Do you want to be redirected to the resume?')
            if ee == True:
                pathfind = str(pathlib.Path(__file__).parent.absolute())
                os.startfile(pathfind[:len(pathfind) - 7] +
                             '\\builder\\resumeexample.pdf')
                os.startfile(pathfind[:len(pathfind) - 7] +
                             '\\builder\\resumeexample.png')
                master.destroy()
            else:
                master.destroy()
                root1 = Tk()
                file = "images/giphy.gif"

                info = Image.open(file)

                frames = info.n_frames  # gives total number of frames that gif contains

                # creating list of PhotoImage objects for each frames
                im = [PhotoImage(
                    file=file, format=f"gif -index {i}") for i in range(frames)]

                count = 0
                anim = None

                def animation(count):
                    im2 = im[count]

                    gif_label.configure(image=im2)
                    count += 1
                    if count == frames:
                        count = 0
                    anim = root1.after(50, lambda: animation(count))

                gif_label = Label(root1, image="")
                gif_label.pack()
                animation(count)
                root.mainloop()

# Skills----------------------------------------------------------------------------------------------------------------------------


with open("database/cookie.json") as f:
    cookiedata = json.load(f)
    data = cookiedata['log'][0]

Ski_title = Label(page, fg='white', text='Skills',
                  bg='midnight Blue', width=235).pack(pady=10)

technical_skills = Label(page, text="Technical Skills:").place(x=140, y=270)
tech = Text(page, width=50, height=5)
if 'tskills' in data:
    tech.insert(INSERT, data['tskills'])
tech.place(x=230, y=270)
soft_skills = Label(page, text="Soft Skills:").place(x=170, y=365)
soft = Text(page, width=50, height=5)
if 'sskills' in data:
    soft.insert(INSERT, data['sskills'])
soft.place(x=230, y=365)
any_other_skills = Label(page, text="Any Other Skills:").place(x=140, y=460)
anyskill = Text(page, width=50, height=5)
if 'anyskill' in data:
    anyskill.insert(INSERT, data['anyskill'])
anyskill.place(x=230, y=460)

# References-------------------------------------------------------------------------------------------------------------------------

Ref_title = Label(page, fg='white', text='References',
                  bg='midnight Blue', width=235).pack(pady=300)

name = Label(page, text="Name:").place(x=180, y=600)
text1 = Text(page, width=50, height=1)
if 'reference' in data:
    text1.insert(INSERT, data['reference'][0]['name'])
text1.place(x=230, y=600)
job_title = Label(page, text="Job Title:").place(x=170, y=625)
text2 = Text(page, width=50, height=1)
if 'reference' in data:
    text2.insert(INSERT, data['reference'][0]['jobt'])
text2.place(x=230, y=625)
company = Label(page, text="Company:").place(x=170, y=650)
text3 = Text(page, width=50, height=1)
if 'reference' in data:
    text3.insert(INSERT, data['reference'][0]['company'])
text3.place(x=230, y=650)
address = Label(page, text="Address:").place(x=170, y=675)
text4 = Text(page, width=50, height=3)
if 'reference' in data:
    text4.insert(INSERT, data['reference'][0]['address'])
text4.place(x=230, y=675)
contact_no = Label(page, text="Contact No:").place(x=160, y=730)
text5 = Text(page, width=50, height=1)
if 'reference' in data:
    text5.insert(INSERT, data['reference'][0]['contact'])
text5.place(x=230, y=730)
email_address = Label(page, text="Email Address:").place(x=145, y=755)
text6 = Text(page, width=50, height=1)
if 'reference' in data:
    text6.insert(INSERT, data['reference'][0]['email'])
text6.place(x=230, y=755)

# Any Other Activities-------------------------------------------------------------------------------------------------------------------------

any_other_activities_title = Label(page, fg='white', text='Any Other Activities',
                                   bg='midnight Blue', width=235).place(y=800)

any_other_activities = Label(
    page, text="Any Other Activities:").place(x=110, y=825)
anyact = Text(page, width=50, height=5)
if 'anyact' in data:
    anyact.insert(INSERT, data['anyact'])
anyact.place(x=230, y=825)

# Submit----------------------------------------------------------------------------------------------------------------------------------------
submit = Frame(page)
submit.pack(side=BOTTOM, pady=20)
Button(submit, text='SUBMIT', fg='white', bg='midnight blue',
       width=10, command=onsubmit).grid(column=1, row=1, padx=20)


canvas.create_window(0, 0, anchor='nw', window=frame)
canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'),
                 yscrollcommand=scroll_y.set)

canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')
canvas.pack(fill='both', expand=True, side='left')

mainloop()
