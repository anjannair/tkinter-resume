import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import json
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from cryptography.fernet import Fernet


with open("database/cookie.json") as f:
    position = json.load(f)['log'][1]['position']
with open("database/cookie.json") as files:
    resume = json.load(files)['resume'][0]
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
    data = json.load(f)['users'][position]
# Text Variables
if (len(data['first']+data['last']) > 20):
    middle = data['first'].split(
        ' ')[0]+' '+list(data['first'].split(' ')[1])[0]+' '+data['last']
else:
    middle = data['first'].split(
        ' ')[0]+' '+data['first'].split(' ')[1]+' '+data['last']
Name = middle
Title = resume['position']
Contact = data['curmaddress'][0]['street']+', '+data['curmaddress'][0]['locality']+'\n'+data['curmaddress'][0]['city']+' - '+data['curmaddress'][0]['pin']+'\n' + \
    data['curmaddress'][0]['state']+' '+data['curmaddress'][0]['country'] + \
    '\nPhone - '+data['phone']+'\nMobile - ' + \
    data['mobile']+'\nEmail - '+data['email']
ProjectsHeader = 'PROJECTS/PUBLICATIONS'
ProjectOneTitle = 'Title - '+data['projects'][0]['title']
ProjectOneDesc = data['projects'][0]['description']
ProjectTwoTitle = 'Title - '+data['projects'][1]['title']
ProjectTwoDesc = data['projects'][1]['description']
ProjectThreeTitle = 'Title - '+data['projects'][2]['title']
ProjectThreeDesc = data['projects'][2]['description']
Linkedin = 'Linkedin - '+data['linkedin']
WorkHeader = 'EXPERIENCE'
WorkOneTitle = data['job'][0]['job']
WorkOneTime = data['job'][0]['start']+" - "+data['job'][0]['end']
WorkOneDesc = data['job'][0]['description']
WorkTwoTitle = data['job'][1]['job']
WorkTwoTime = data['job'][1]['start']+" - "+data['job'][1]['end']
WorkTwoDesc = data['job'][1]['description']
WorkThreeTitle = data['job'][2]['job']
WorkThreeTime = data['job'][2]['start']+" - "+data['job'][2]['end']
WorkThreeDesc = data['job'][2]['description']
EduHeader = 'EDUCATION'
EduOneTitle = 'College - '+data['academic'][0]['college']
CGPA = 'CGPA - '+str(data['academic'][0]['cgpa'])
EduOneDesc = 'Degree - '+data['academic'][0]['degree']
SkillsHeader = 'Skills'
SkillsDesc = data['tskills']+"\n"+data['sskills']+"\n"+data['anyskill']
ExtrasTitle = 'ACTIVITIES'
ExtrasDesc = data['anyact']

# Setting style for bar graphs

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

fig, ax = plt.subplots(figsize=(8.5, 11))
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# add text
plt.annotate(Name, (.25, .94), weight='bold', fontsize=20)
plt.annotate(Title, (.30, .91), weight='regular', fontsize=14)
plt.annotate(Contact, (.7, .906), weight='regular',
             fontsize=8, color='#ffffff')
plt.annotate(ProjectsHeader, (.02, .86), weight='bold',
             fontsize=10, color='#58C1B2')
plt.annotate(ProjectOneTitle, (.02, .832), weight='bold', fontsize=10)
plt.annotate(ProjectOneDesc, (.04, .78), weight='regular', fontsize=9)
plt.annotate(ProjectTwoTitle, (.02, .745), weight='bold', fontsize=10)
plt.annotate(ProjectTwoDesc, (.04, .71), weight='regular', fontsize=9)
plt.annotate(ProjectThreeTitle, (.02, .672), weight='bold', fontsize=10)
plt.annotate(ProjectThreeDesc, (.04, .638), weight='regular', fontsize=9)
plt.annotate(Linkedin, (.06, .6), weight='bold', fontsize=10)
plt.annotate(WorkHeader, (.02, .54), weight='bold',
             fontsize=10, color='#58C1B2')
plt.annotate(WorkOneTitle, (.02, .508), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.02, .493), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkOneDesc, (.04, .445), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.02, .4), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (.02, .385), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkTwoDesc, (.04, .337), weight='regular', fontsize=9)
plt.annotate(WorkThreeTitle, (.02, .295), weight='bold', fontsize=10)
plt.annotate(WorkThreeTime, (.02, .28), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkThreeDesc, (.04, .247), weight='regular', fontsize=9)
plt.annotate(EduHeader, (.02, .185), weight='bold',
             fontsize=10, color='#58C1B2')
plt.annotate(EduOneTitle, (.02, .155), weight='bold', fontsize=10)
plt.annotate(EduOneDesc, (.02, .14), weight='regular', fontsize=9)
plt.annotate(CGPA, (.02, .125), weight='regular', fontsize=9, alpha=.6)
plt.annotate(SkillsHeader, (.7, .8), weight='bold',
             fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (.7, .56), weight='regular',
             fontsize=10, color='#ffffff')
plt.annotate(ExtrasTitle, (.7, .43), weight='bold',
             fontsize=10, color='#ffffff')
plt.annotate(ExtrasDesc, (.7, .345), weight='regular',
             fontsize=10, color='#ffffff')

# add user image
arr_code = mpimg.imread(data['image'])
imagebox = OffsetImage(arr_code, zoom=0.3)
ab = AnnotationBbox(imagebox, (.1, .94))
ax.add_artist(ab)

img = mpimg.imread('database/linkedin.png')
imagebox1 = OffsetImage(img, zoom=0.3)
ab1 = AnnotationBbox(imagebox1, (.03, .605))
ax.add_artist(ab1)

plt.savefig('builder/resumeexample.png', dpi=300, bbox_inches='tight')
plt.savefig('builder/resumeexample.pdf', dpi=300, bbox_inches='tight')

# opening the original file to encrypt
with open('database/user.json', 'rb') as file:
    original = file.read()

# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
with open('database/user.json', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
