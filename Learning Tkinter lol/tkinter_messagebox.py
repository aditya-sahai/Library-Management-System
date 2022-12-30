from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Message boxes xd")

def popup():
    # this is one type of message box, an information box

    # messagebox.showerror("This is my Title", "This is my message") 
    '''
    other message boxes are:
    showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    ok returns 1, cancel returns 0
    askyesno returns 1 for yes and 0 for no
    however, askquestion returns "yes" for yes and "no" for no
    showerror returns ok, showwarning also returns ok, also showinfo
    '''
    response = messagebox.askyesno("Title", "Yes or No?") 
    Label(root, text=response).pack()


b = Button(root, text = "popup", command=popup)
b.pack()

root.mainloop()
