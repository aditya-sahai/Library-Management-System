from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title()
# Changing the tiny icon on the top left of the window:
# root.iconbitmap("File path")

myimg = ImageTk.PhotoImage(Image.open("tree.jpg"))
mylabel = Label(image = myimg)
mylabel.pack()



root.mainloop()