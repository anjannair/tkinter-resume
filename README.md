# Tkinter Resume Generator
A tkinter project that was designed to store data of users and build resumes from the data inputted.

## How this project is different from the others?
* The project has a beautiful GUI that has a sign-up page, a login page, and 2 pages of resume data inputting page.
* It utilizes JSONs to store data of users.
* [Fernet keys](https://cryptography.io/en/latest/fernet/) are used to encrypt the `user.json` file which is used to store user data.

## How to get started?
1) Fork the project and clone it on your system or download the zipped code from [here](https://github.com/anjannair/tkinter-resume/archive/refs/heads/main.zip).
2) Next find the `example-database` folder and rename it to `database`.
3) Run the famous `pip install -r requirements.txt` or ` pip3 install -r requirements.txt `
4) Open the `fernet` folder and head to `genkey.py` and generate your Fernet key (by executing the code) and keep it a secret! Then open `encryption.py` and execute it. 
   **PS: You only have to generate the key only once!! Do not generate it again!!**
5) You need a registered user to get started so execute `reg.py` and tadaa!!! (On a side note: Once you execute `reg.py` just execute `main.py` from next time)

<div align="center">
<b>YOU ARE GOOD TO GO!!!!</b>
</div>
<br></br>

## A sneak-peek into the GUI
<div align="center">
<img src="https://github.com/anjannair/tkinter-resume/blob/main/images/Screenshots/reg.png" >
<p>The registeration page of the GUI</p>
</div>
<br></br>
<div align="center">
<img src="https://github.com/anjannair/tkinter-resume/blob/main/images/Screenshots/resume.png" >
<p>The first resume page of the GUI</p>
</div>

## Issues one may face
* There is a very small chance you may get a cryptography error (`cryptography.fernet.InvalidToken`) then all you need to do is check if the `user.json` file in the `database` folder is encrypted. If not run `encryption.py` in the `fernet` folder.
* Alignment of the GUI may not be proper because of the use of `fullscreen` mode in tkinter window attributes. Since screen of each desktop is different the alignment varies. If you want to remove it, use the search function in your IDE and search for the`.attributes('-fullscreen', True)` and replace it with `.geometry('<YOUR DIMENSION>')` (obviously replace `<YOUR DIMENSION` with the dimension you want).
* The alignment of the resume generated changes. Yes I know about this and I am looking at better solutions for generating a resume in a dynamic way. 
* The GUI may lag when scrolling up and down but that cannot be fixed.
* The GUI may lag after the `CREATE RESUME` button is clicked after the second page of the resume input. I am trying to determine a fix for it and making it faster.

## References
1) I was inspired by the GUI of this project and adopted it into mine - https://github.com/MaddyUnknown/Application-form-Tkinter
2) The resume generator was exactly built and modified from an existing project - https://github.com/e-kirkland/datascience/tree/master/Resume