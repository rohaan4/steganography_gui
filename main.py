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

root.mainloop()#starting main loop of window to keep it running