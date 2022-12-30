from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title()

# myimg = ImageTk.PhotoImage(Image.open(r"C:\Users\Anu Ghorse\Documents\_library management project\Learning Tkinter lol\tree.jpg"))

# frames are little boxesthat are used to keep your GUI organized
# padx and paady here will pad INSIDE THE GRAME
frame = LabelFrame(root, text = "My frame", padx = 50, pady = 50)

# padx and pady here will pad OUTSIDE THE FRAME
frame.pack(padx = 10, pady = 10)

# notice how instead of root, we put frame as we want the button inside the frame
b = Button(frame, text = "DONT CLICK HERE")
b.pack()
# you can also use grid system within a frame, but still use .pack() on the frame itself




root.mainloop()