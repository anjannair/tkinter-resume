from tkinter.ttk import *
from tkinter import *
from datetime import datetime
import tkinter.messagebox
import json
import os
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tkcalendar import Calendar
from cryptography.fernet import Fernet
import shutil

# --------------------------------------BACKEND---------------------------------

with open("database/cookie.json") as f:
    cookiedata = json.load(f)
    delete1 = cookiedata['resume']
delete1.clear()
with open("database/cookie.json", 'w') as f:
    json.dump(cookiedata, f, indent=4)


imgpath = ''


def choose():
    path = askopenfilename(filetypes=[("Image File", '.png')])
    im = Image.open(path)
    global imgpath
    imgpath = path
    path1 = imgpath.split('/')
    path1 = path1[len(path1)-1]
    im = im.resize((138, 177), Image.ANTIALIAS)
    im.save('database/images/'+path1)
    tkimage = ImageTk.PhotoImage(im)
    myvar = Label(page, image=tkimage)
    myvar.image = tkimage
    myvar.place(x=970, y=283)


def onnext():
    if(linkedin.get("1.0", "end-1c") == '' or uni.get("1.0", "end-1c") == '' or year.get() == '' or otherqual.get("1.0", "end-1c") == ''
       or job1.get("1.0", "end-1c") == '' or start1.get("1.0", "end-1c") == '' or end1.get("1.0", "end-1c") == '' or jobdesc1.get("1.0", "end-1c") == '' or
       job2.get("1.0", "end-1c") == '' or start2.get("1.0", "end-1c") == '' or end2.get("1.0", "end-1c") == '' or jobdesc2.get("1.0", "end-1c") == '' or
       job3.get("1.0", "end-1c") == '' or start3.get("1.0", "end-1c") == '' or end3.get("1.0", "end-1c") == '' or jobdesc3.get("1.0", "end-1c") == '' or
       projtext1.get("1.0", "end-1c") == '' or projedesc1.get("1.0", "end-1c") == '' or projtext2.get(
           "1.0", "end-1c") == '' or projedesc2.get("1.0", "end-1c") == ''
       or projtext3.get("1.0", "end-1c") == '' or projedesc3.get("1.0", "end-1c") == '' or achievements.get("1.0", "end-1c") == ''
       or obj.get("1.0", "end-1c") == '' or position.get("1.0", "end-1c") == ''):
        tkinter.messagebox.showwarning(
            '', 'One of the inputs are empty!')
        return
    with open("database/cookie.json") as f:
        cookiedata = json.load(f)
        data = cookiedata['log'][0]
    if not 'image' in data:
        if(imgpath == ''):
            tkinter.messagebox.showwarning(
                '', 'Image is missing!')
            return
        path = imgpath.split('/')
        path = path[len(path)-1]
    else:
        path = data['image'].split('/')
        path = path[len(path)-1]
    y = {
        "objective": obj.get("1.0", "end-1c"),
        "position": position.get("1.0", "end-1c"),
    }
    z = {
        "linkedin": linkedin.get("1.0", "end-1c"),
        "image": 'database/images/'+path,
        "uni": uni.get("1.0", "end-1c"),
        "passing_year": year.get(),
        "otherqual": otherqual.get("1.0", "end-1c"),
        "job": [
            {
                "job": job1.get("1.0", "end-1c"),
                "start": start1.get("1.0", "end-1c"),
                "end": end1.get("1.0", "end-1c"),
                "description": jobdesc1.get("1.0", "end-1c")
            },
            {
                "job": job2.get("1.0", "end-1c"),
                "start": start2.get("1.0", "end-1c"),
                "end": end2.get("1.0", "end-1c"),
                "description": jobdesc2.get("1.0", "end-1c")
            },
            {
                "job": job3.get("1.0", "end-1c"),
                "start": start3.get("1.0", "end-1c"),
                "end": end3.get("1.0", "end-1c"),
                "description": jobdesc3.get("1.0", "end-1c")
            }
        ],
        "projects": [
            {
                "title": projtext1.get("1.0", "end-1c"),
                "description": projedesc1.get("1.0", "end-1c")
            },
            {
                "title": projtext2.get("1.0", "end-1c"),
                "description": projedesc2.get("1.0", "end-1c")
            },
            {
                "title": projtext3.get("1.0", "end-1c"),
                "description": projedesc3.get("1.0", "end-1c")
            }
        ],
        "achivements": achievements.get("1.0", "end-1c")
    }
    # Saving in cookie
    with open("database/cookie.json") as f:
        data = json.load(f)
        users = data['resume']
        positionof = data['log'][1]['position']
    users.append(y)
    with open("database/cookie.json", 'w') as f:
        json.dump(data, f, indent=4)

# -----------------------------------------------------------------------------
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
    users.update(z)
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

    root.destroy()
    os.system("py resume/resume2.py")

# --------------------------------------------------------------------------------


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
photo = PhotoImage(file="Logo.png").subsample(3)
Label(logo, image=photo).grid(column=0, row=0, rowspan=2)
Label(logo, text="WeJob", font=('Aileron Bold', 22), fg='midnight blue').grid(
    column=1, row=0, columnspan=5, padx=10)
Label(logo, text="India's preferred job site", font=('Penna', 15),
      fg='dark slate blue').grid(column=1, row=1, sticky=W, padx=10)
Res = Label(page, fg='midnight Blue', text='RESUME',
            font=("Times", 25, "bold")).pack(pady=10)
xm = Label(page, fg='red', text='Whenever you apply to an internship or fresher job, this is the resume that the employer will see. Always make sure it is up to date.', font=("Times", 15)).pack(pady=2)


# personal-info------------------------------------------------------------------------------------------------------------------------------
Person_title = Label(page, fg='white', text='Personal Information',
                     bg='midnight Blue', width=235).pack(pady=10)

with open("database/cookie.json") as f:
    cookiedata = json.load(f)
    data = cookiedata['log'][0]


first_name = Label(page, text="First Name:").place(x=150, y=270)
first = Text(page, width=50, height=1)
first.insert(INSERT, data['first'])
first.configure(state='disabled')
first.place(x=230, y=270)
last_name = Label(page, text="Last Name:").place(x=150, y=295)
last = Text(page, width=50, height=1)
last.insert(INSERT, data['last'])
last.configure(state='disabled')
last.place(x=230, y=295)
email_address = Label(page, text="Email Address:").place(x=150, y=320)
email = Text(page, width=50, height=1)
email.insert(INSERT, data['email'])
email.configure(state='disabled')
email.place(x=230, y=320)
contact_no = Label(page, text="Contact No.:").place(x=150, y=345)
mobile = Text(page, width=50, height=1)
mobile.insert(INSERT, data['mobile'])
mobile.configure(state='disabled')
mobile.place(x=230, y=345)
linkedin_url = Label(page, text="LinkedIn URL:").place(x=150, y=370)
linkedin = Text(page, width=50, height=1)
if 'linkedin' in data:
    linkedin.insert(INSERT, data['linkedin'])
linkedin.place(x=230, y=370)
objective = Label(page, text="Objective:").place(x=150, y=395)
obj = Text(page, width=50, height=4)
obj.place(x=230, y=395)
position_desired = Label(page, text="Position Desired:").place(x=130, y=470)
position = Text(page, width=50, height=1)
position.place(x=230, y=470)
upload_your_image_here = Label(
    page, text="Upload Your Image Here:", font=('bold', 10)).place(x=965, y=267)

up = Button(page, text='Select Image', command=choose)
up.place(x=1000, y=465)
if 'image' in data:
    up['state'] = 'disabled'
    im = Image.open(data['image'])
    im = im.resize((138, 177), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(im)
    myvar = Label(page, image=tkimage)
    myvar.image = tkimage
    myvar.place(x=970, y=283)

# Qualifications----------------------------------------------------------------------------------------------------------------------------

Edu_title = Label(page, fg='white', text='Educational Qualifications',
                  bg='midnight Blue', width=235).place(y=495)


degree = Label(page, text="Degree:").place(x=150, y=520)
degreetext = Text(page, width=50, height=1)
degreetext.insert(INSERT, data['academic'][0]['degree'])
degreetext.configure(state='disabled')
degreetext.place(x=230, y=520)
name_of_institution = Label(
    page, text="Name of Institution:").place(x=120, y=545)
college = Text(page, width=50, height=1)
college.insert(INSERT, data['academic'][0]['college'])
college.configure(state='disabled')
college.place(x=230, y=545)
university = Label(page, text="University:").place(x=150, y=570)
uni = Text(page, width=50, height=1)
if 'uni' in data:
    uni.insert(INSERT, data['uni'])
uni.place(x=230, y=570)
Label(page, text="Year of Passing:").place(x=135, y=595)
year = Combobox(page, width=5)
year['value'] = ('',)+tuple(i for i in range(1980, datetime.now().year+3))
year.current(0)
if 'passing_year' in data:
    year.set(data['passing_year'])
year.place(x=230, y=595)
cgpa = Label(page, text="CGPA:").place(x=360, y=595)
cgpatext = Text(page, width=10, height=1)
cgpatext.insert(INSERT, data['academic'][0]['cgpa'])
cgpatext.configure(state='disabled')
cgpatext.place(x=400, y=595)
other_qualification = Label(
    page, text="Other Qualifications:").place(x=117, y=620)
otherqual = Text(page, width=50, height=3)
if 'otherqual' in data:
    otherqual.insert(INSERT, data['otherqual'])
otherqual.place(x=230, y=620)

# Experience--------------------------------------------------------------------------------------------------------------------------
Exp_title = Label(page, fg='white', text='Experience',
                  bg='midnight Blue', width=235).pack(pady=405)
# 1
Job_title = Label(page, text="Job Title:").place(x=140, y=705)
job1 = Text(page, width=50, height=1)
if 'job' in data:
    job1.insert(INSERT, data['job'][0]['job'])
job1.place(x=230, y=705)

Date_title = Label(page, text="Start Date:").place(x=140, y=732)
start1 = Text(page, width=30, height=1)
if 'job' in data:
    start1.insert(INSERT, data['job'][0]['start'])
start1.place(x=230, y=732)

End_title = Label(page, text="End Date:").place(x=140, y=760)
end1 = Text(page, width=30, height=1)
if 'job' in data:
    end1.insert(INSERT, data['job'][0]['end'])
end1.place(x=230, y=760)

Job_description = Label(page, text="Description:").place(x=675, y=705)
jobdesc1 = Text(page, width=50, height=3)
if 'job' in data:
    jobdesc1.insert(INSERT, data['job'][0]['description'])
jobdesc1.place(x=760, y=705)

# 2
Job_title = Label(page, text="Job Title:").place(x=140, y=825)
job2 = Text(page, width=50, height=1)
if 'job' in data:
    job2.insert(INSERT, data['job'][1]['job'])
job2.place(x=230, y=827)

Date_title = Label(page, text="Start Date:").place(x=140, y=852)
start2 = Text(page, width=30, height=1)
if 'job' in data:
    start2.insert(INSERT, data['job'][1]['start'])
start2.place(x=230, y=854)

End_title = Label(page, text="End Date:").place(x=140, y=880)
end2 = Text(page, width=30, height=1)
if 'job' in data:
    end2.insert(INSERT, data['job'][1]['end'])
end2.place(x=230, y=882)

Job_description = Label(page, text="Description:").place(x=675, y=825)
jobdesc2 = Text(page, width=50, height=2)
if 'job' in data:
    jobdesc2.insert(INSERT, data['job'][1]['description'])
jobdesc2.place(x=760, y=825)

# 3
Job_title = Label(page, text="Job Title:").place(x=140, y=940)
job3 = Text(page, width=50, height=1)
if 'job' in data:
    job3.insert(INSERT, data['job'][2]['job'])
job3.place(x=230, y=940)

Date_title = Label(page, text="Start Date:").place(x=140, y=967)
start3 = Text(page, width=30, height=1)
if 'job' in data:
    start3.insert(INSERT, data['job'][2]['start'])
start3.place(x=230, y=967)

End_title = Label(page, text="End Date:").place(x=140, y=995)
end3 = Text(page, width=30, height=1)
if 'job' in data:
    end3.insert(INSERT, data['job'][2]['end'])
end3.place(x=230, y=995)

Job_description = Label(page, text="Description:").place(x=675, y=940)
jobdesc3 = Text(page, width=50, height=2)
if 'job' in data:
    jobdesc3.insert(INSERT, data['job'][2]['description'])
jobdesc3.place(x=760, y=940)

# Projects---------------------------------------------------------------------------------------------------------------------------
Project_title = Label(page, fg='white', text='Projects',
                      bg='midnight Blue', width=235).place(y=1100)

project_name1 = Label(page, text="Project Title").place(x=140, y=1125)
projtext1 = Text(page, width=50, height=1)
if 'projects' in data:
    projtext1.insert(INSERT, data['projects'][0]['title'])
projtext1.place(x=265, y=1125)

project_description = Label(
    page, text="Project Description:").place(x=140, y=1152)
projedesc1 = Text(page, width=50, height=3)
if 'projects' in data:
    projedesc1.insert(INSERT, data['projects'][0]['description'])
projedesc1.place(x=265, y=1152)

project_name2 = Label(page, text="Project Title").place(x=140, y=1255)
projtext2 = Text(page, width=50, height=1)
if 'projects' in data:
    projtext2.insert(INSERT, data['projects'][1]['title'])
projtext2.place(x=265, y=1255)

project_description = Label(
    page, text="Project Description:").place(x=140, y=1282)
projedesc2 = Text(page, width=50, height=2)
if 'projects' in data:
    projedesc2.insert(INSERT, data['projects'][1]['description'])
projedesc2.place(x=265, y=1282)

project_name3 = Label(page, text="Project Title").place(x=140, y=1379)
projtext3 = Text(page, width=50, height=1)
if 'projects' in data:
    projtext3.insert(INSERT, data['projects'][2]['title'])
projtext3.place(x=265, y=1379)

project_description = Label(
    page, text="Project Description:").place(x=140, y=1406)
projedesc3 = Text(page, width=50, height=2)
if 'projects' in data:
    projedesc3.insert(INSERT, data['projects'][2]['description'])
projedesc3.place(x=265, y=1406)

# _________________________________Achivements_____________________________________________________________________
Achivements_title = Label(page, fg='white', text='Achivements',
                          bg='midnight Blue', width=235).pack(pady=405)

Achivements_title = Label(page, text="Achivements:").place(x=140, y=1535)
achievements = Text(page, width=100, height=15)
if 'achivements' in data:
    achievements.insert(INSERT, data['achivements'])
achievements.place(x=230, y=1535)

# Button-----------------------------------------------------------------------------------------------------------
Button(page, text='Next Page', fg='white', bg='midnight blue',
       command=onnext).place(x=795, y=1800)

canvas.create_window(0, 0, anchor='nw', window=frame)

canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'),
                 yscrollcommand=scroll_y.set)

canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')
canvas.pack(fill='both', expand=True, side='left')

mainloop()
