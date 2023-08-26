#importing necessery libraries
from tkinter import *#importing all classes, functions and variables from "tkinter" to create GUI
from tkinter import filedialog#importing filedialog to work with dialog boxes to work with file related operations
import tkinter as tk
from PIL import Image, ImageTk#importing Image and ImageTk to improve capabilities of image work
import os
from stegano import lsb

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="Select Image File",
                                        filetypes=(("PNG File", "*.png"),
                                                  ("JPG File", "*.jpg"),
                                                  ("All File", "*.*")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250, height=250)
    lbl.image=img

def message_to_bin(message):
    """Convert a string message to binary."""
    #for i in message->iterating through the message
    #ord(i)->returns the unicode character of the letter
    #08b->ocnverting the unicode into the binary format in 8bits
    #join-> joining all binary representations of characters into one string
    binary_message = ''.join(format(ord(i), '08b') for i in message)
    return binary_message

def bin_to_message(binary_message):
    """Convert a binary string to its ASCII representation."""
    #for loop ->iterating through the binary message at increments of 8
    #binary_message[i:i+8]-> for each value of i we slice the 8-bit segment from "binary message"
    #(int(binary_message[i:i+8], 2) -> onverting 8-bit segment to integer."2" indicates input string is in base 2(binary)
    #chr->converts the integer into its ASCII character
    #join-> joins all the characters into a single string
    ascii_string = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    return ascii_string

def hide_message(image_path, message):
    """Hide the message in the image."""
    img = Image.open(image_path)#opening the image
    binary_message = message_to_bin(message) + '1111111111111110' #converting the user's message to binary and appending terminator to indicate end of message
    pixels = list(img.getdata())#getting the pixels data of the image and storing in a list
    new_pixels = []#creating new list to store modified pixels with hidden message
    
    message_index = 0#initializing current message index to 0 to track binary message processing
    for pixel in pixels:#iterating through each tuple(pixel) in the pixels list
        if message_index < len(binary_message):#checking if there are bits of messages left to be hidden
            new_pixel = (pixel[0] & ~1 | int(binary_message[message_index]),) + pixel[1:]
            #pixel[0] & ~1 ->retrieving value of red channel and inverting the binary value of 1
            #int(binary_message[message_index] ->getting the current bit of the message that needs to be hidden
            #pixel[0] & ~1 | int(binary_message[message_index]) ->effectively replacing the LSB or the red channel to current message bit
            new_pixels.append(new_pixel)#appending the modified pixel to the new_pixels list
            message_index += 1#incrementing message index to iterate the loop
        else:
            new_pixels.append(pixel)#if allbits of binary message have been embedded into the image, the code appends the rest of the pixels
            
    img.putdata(new_pixels)##putting the modified data into the image
    img.save('hidden.png')#saving the image as a separate file
    return img

def show_message(image_path):
    """Reveal the message from the image."""
    img = Image.open(image_path)#opening the image
    pixels = list(img.getdata())#getting the image data and storing it into a list
    
    binary_message = ''
    for pixel in pixels:
        binary_message += str(pixel[0] & 1)
        
    terminator = binary_message.find('1111111111111110')
    if terminator != -1:
        binary_message = binary_message[:terminator]
        
    message = bin_to_message(binary_message)
    return message



def hide():
    global filename
    message = text1.get(1.0, END)
    hide_message(filename, message)


def show():
    revealed_message = show_message('hidden.png')
    text1.delete(1.0, END)
    text1.insert(END, revealed_message)



def save():
    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if filepath:
        img = Image.open("hidden.png")
        img.save(filepath)

#SETTING UP THE GUI
root=Tk()#creating main window for application
root.title("Steganography- Hide your data")#setting title of main window
root.geometry("700x500+150+180")#setting width, height, and position of window
root.resizable(False, False)#making sure that the window is not resizable by user
root.configure(bg="#2f4155")#setting background color of window


#icon of the window
image_icon=PhotoImage(file="logo_main.png")#loading an image using photoimage library
root.iconphoto(False, image_icon)#setting the window icon to the image loaded above

#logo of the window
logo=PhotoImage(file="logo.png")#loading an image for the application logo
Label(root, image=logo, bg="#2f4155").place(x=10,y=0)#creating label in main window and displaying the logo at (10,0) coordinates

#setting up the heading of the window
Label(root, text="CYBERSECURITY", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

#first frame
f=Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)#setting up the left side framespecified with border, bg color, dimensions and groove styled border
f.place(x=10, y=80)#placing it at the coordinates(10,80)
lbl=Label(f,bg="black")#setting up a label inside and settingbg color to black
lbl.place(x=40,y=10)#placing the label at (40,10) coordinates in the frame

#second Frame
frame2=Frame(root, bd=3, width=340, height=280,bg="white", relief=GROOVE)#creating the right side frame much like the left(bg is WHITE)
frame2.place(x=350, y=80)#placing it at (350, 80) coordinates
text1=Text(frame2, font="robote 20", bg="white", fg="black", relief=GROOVE)#creating text widget for multi-line input
text1.place(x=0, y=0, width=320, height=295)#placing the text widget in the right side frame

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third Frame
frame3=Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)#creating third frame simliar to the above 2 but with diff. dimensions
frame3.place(x=10,y=370)#placing it at (10, 370) coordinates

Button(frame3, text="Open Image", width=10, height=2, font="ariel 14 bold",command=showimage).place(x=20, y=30)#making a button in the third frame to open the image
Button(frame3, text="Save Image", width=10, height=2, font="ariel 14 bold",command=save).place(x=180, y=30)#making another button to save the image
Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)#creating label above the two buttons to suggest user on input format

#fourth Frame
frame4=Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4, text="Encode Data", width=10, height=2, font="ariel 14 bold",command=hide).place(x=20, y=30)#creating button in the fourth frame to encode data in image
Button(frame4, text="Decode Data", width=10, height=2, font="ariel 14 bold",command=show).place(x=180, y=30)#creating another button to decode data in the image
Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)
root.mainloop()#starting main loop of window to keep it running