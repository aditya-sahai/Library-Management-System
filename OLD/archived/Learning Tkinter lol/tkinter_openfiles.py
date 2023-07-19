from tkinter import *
from PIL import ImageTk, Image
# NOTICE THIS THING YOU HAVE TO IMPORT 
from tkinter import filedialog

root = Tk()
root.title("MAIN WINDOW")

# THIS LINE IS VERY IMPORTANT!
root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\Anu Ghorse\Documents\_library management project\Learning Tkinter lol", title = "select a file", filetypes = (("png files", "*.png"), ("all files", "*.*"), ("text files", "*.txt")))

# mylabel = Label(root, text=root.filename).pack() # this line will only return file path. 
myimage = ImageTk.PhotoImage(Image.open(root.filename))
image_label = Label(root, image=myimage).pack()


root.mainloop()