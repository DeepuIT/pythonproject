from tkinter import *
#For GUI and program
from PIL import Image, ImageTk
#The actual backend logic
import image_convertor as imgc
#To save and open PDF
import os
import tkinter as tk
#To choose and open a file 
from tkinter import filedialog 
from gtts import gTTS
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import smtplib


imagelist = []
BG = imgc.Image.open("Letters/bg.png")
sizeOfSheet =BG.width
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890'
HandwritingStyle=''

#Actual GUI window
root = tk.Tk() 
root.geometry("1000x600")
root.state('zoomed')
root.configure(background='snow')
root.title('Transfiguiring Typed Text and Handwritten Text')

#Deletes previously saved files
def del_old():
    cwd = os.getcwd()
    test=os.listdir(cwd)
    for item in test:
        if item.endswith(".pdf") or item.endswith(".png") or item.endswith(".txt"):
            os.remove(item)
			
#Program
def success():
    del_old()
    curr_directory = os.getcwd()
    name = filedialog.askopenfilename(initialdir = curr_directory,title = "Select A file",filetypes = (("Text files", "*.txt*"),("all files","*.*")))
    HandwritingStyle = clicked.get()
    print("File uploaded")
    #print(HandwritingStyle)
    img = imgc.convertor(BG,sizeOfSheet,allowedChars,HandwritingStyle)
    f = open(name,'r')
    txt=f.read()
    img.run(name)
    img.makeimage()
    img.makepdf()
    label_file_explorer.configure(text="FILE UPLOADED!")
    ttmp3 = gTTS(text=txt,lang="en",tld="com")
    ttmp3.save("output.mp3")
	
	
#Opens the PDF
def download():
    os.startfile("final.pdf")
    print("File downloaded")
    f = open("final.pdf","r")
	# filedialog.askopenfilename()
    # return send_file("final.pdf", as_attachment=True)


filename=""
def browseFiles(): 
	filename = filedialog.askopenfilename(initialdir = "/", 
										title = "Select a File", 
										filetypes = (("Text files", 
														"*.txt*"), 
												      ))  													
	
	
    
def listen():
    os.system(" start output.mp3")
    
    
    
    
def sendmail(event=None):
    msg = MIMEMultipart()
    fromaddr='deepika.usapp@gmail.com'
    toaddr=mailid.get()
    msg['From'] = fromaddr
    # storing the receivers email address
    msg['To'] = toaddr
    # storing the subject
    msg['Subject'] = "Output file of the application Transfiguring Handwritten Text and Typewritten Text"
    # string to store the body of the mail 
    body = "This mail has the converted output pdf file"
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain'))
    # open the file to be sent
    filename = "final.pdf"
    attachment = open(filename, "rb")
    #attachment = open('StudentDetails\StudentDetails.csv', "rb")
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p.set_payload((attachment).read())
    # encode into base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    #s=smtplib.SMTP('smtp,googlemail.com',465)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(fromaddr, "Deepam@123")
    # Converts the Multipart msg into a string
    text = msg.as_string()
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
    # terminating the session
    s.quit()
    print("Mail sent")

def userText(event):
    mailid.delete(0,END)
    usercheck=True
    
#GUI window elements
#Headings- Labels
#Setting the label at a particular place-place()
#Makes it visible- pack()
w = Label(root, 
		  text='\n\n Transfiguiring Typewritten Text to',
		  fg = "black",
		  bg='snow',font=("Times New Roman", 19, "bold")) 
w.pack() 
w.place(x=400,y=0)
wh=Label(root,
		text='\nHandwritten Text\n',
		fg='black',
		bg='snow',
		font=("Segoe Script",19,'bold'))

wh.pack()
wh.place(x=800,y=12)
usercheck=False

#Canvas- For the image
canvas = Canvas(root, width = 300, height = 320)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("cap.png"))  
canvas.create_image(20, 20, anchor=NW, image=img) 
canvas.place(x=800,y=150)


w2=Label(root,
		  text='Steps To Follow:\n\n 1)Upload a file(.txt)\n 2)Click on the Convert to PDF button to open the PDF file in handwritten style.\n 3)Listen to the output to validate it.\n 4)Enter your mail-id and then click on send mail to send the output file',
		  anchor='e',
		  justify='left',
		  fg="black",font=("Comic Sans MS", 12),
		  bg='snow')
w2.pack()
w2.place(x=100,y=120)

label_file_explorer = Label(root, 
							text = "UPLOAD A FILE!\n\n", 
							width = 15, height = 4, 
							fg = "gray",bg='snow',
							font=("Comic Sans MS",10)) 

btn = Button(root, text = 'Upload File', bd = '5', 
                          command = browseFiles)  
space = Label(root, bg='snow', 
		  text='\n')
options = [
    "First",
	"Second"
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set("Choose a Handwriting Style" )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.config(font=("Comic Sans MS",10),bg='snow')
drop['menu'].config(font=("Comic Sans MS",10),bg='snow')
drop.pack()	
#When clicked, success() function runs.
btnOpen = Button(root, text = 'Select a File', width=15, bd = '5',font=("Comic Sans MS",10), command = success,bg='snow')  
					  
#When clicked, runs the download() function
btnConvert= Button(root,text='Convert to PDF', width=15, bd='5',font=("Comic Sans MS",10), command=download,bg='snow')
	
btn1 = Button(root, text = 'Listen the File', width=15, bd = '5',font=("Comic Sans MS",10), command = listen,bg='snow')  
# mailid = tk.Entry(root,width=30  ,bg="snow"  ,fg="black",font=("Comic Sans MS", 15)  )
# mailid.place(x=320, y=540)
# mailid.insert(0, "Enter your mail-id")
# mailid.bind("<Button>",userText)
def on_click(event):
    my_entry.configure(state=NORMAL)
    my_entry.delete(0, END)
# button2 = tk.Button(root, text='Send Mail', command=sendmail,width=15, bd = '5',font=("Comic Sans MS",10),bg='snow')
# button2.place(x=400, y=630)   
# Set the position of button on the top of window.
label_file_explorer.pack()
label_file_explorer.place(x=400,y=270)
#btn.place(x=175, y=100)    
#btn.pack()   
drop.place(x=400,y=340)
btnOpen.pack()
btnOpen.place(x=400,y=390)
space.pack()  
btnConvert.pack()
btnConvert.place(x=400,y=440)
btn1.place(x=400,y=490)


root.mainloop() 
