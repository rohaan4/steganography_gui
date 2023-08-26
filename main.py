#importing necessery libraries
from tkinter import *#importing all classes, functions and variables from "tkinter" to create GUI
from tkinter import filedialog#importing filedialog to work with dialog boxes to work with file related operations
import tkinter as tk
from PIL import Image, ImageTk#importing Image and ImageTk to improve capabilities of image work
import os
from stegano import lsb
#SETTING UP THE GUI
root=Tk()#creating main window for application
root.title("Steganography- Hide your data")#setting title of main window
root.geometry("700x500+150+180")#setting width, height, and position of window
root.resizable(False, False)#making sure that the window is not resizable by user
root.configure(bg="#2f4155")#setting background color of window


#icon of the window
image_icon=PhotoImage(file="logo_main.png")
root.iconphoto(False, image_icon)

#logo of the window
logo=PhotoImage(file="logo.png")
Label(root, image=logo, bg="#2f4155").place(x=10,y=0)

#setting up the heading of the window
Label(root, text="CYBERSECURITY", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

#first frame
f=Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)
lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

#second Frame
frame2=Frame(root, bd=3, width=340, height=280,bg="white", relief=GROOVE)
frame2.place(x=350, y=80)
text1=Text(frame2, font="robote 20", bg="white", fg="black", relief=GROOVE)
text1.place(x=0, y=0, width=320, height=295)

root.mainloop()#starting main loop of window to keep it running