from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import filedialog

from new_book import *
from issue_book import *
from return_book import *
from book_status import *
from CRUDOperations import button_enterhover, button_leavehover

'''
from new_book import *
here_newbookmenu = new_book.newbookmenu

def disable_button():
    global enternewbook
    enternewbook.config(state="disabled")
def on_closing():
    enternewbook.config(state="normal")

here_newbookmenu.protocol("WM_DELETE_WINDOW", on_closing)
'''

root = Tk()
root.title("Library Management System")
#root.iconbitmap()
root.geometry("800x600")
root.configure(bg="black")

# Creating main container frame
mainscreenframe = LabelFrame(root, text = "Main menu", padx = 50, pady=25, bg = "black", fg="white")
mainscreenframe.pack(pady=(125, 0))

mainheadingfont = ("Footlight MT Light", 20)

# main heading code
mainheadinglabel = Label(mainscreenframe, text = "Library management system", font=mainheadingfont, bg="black", fg="white")
mainheadinglabel.grid(row = 0, column = 0, columnspan = 3)

# buttons code
mainmenuplaceholder1 = Label(mainscreenframe, bg="black")
mainmenuplaceholder1.grid(row=1, column=1)
enternewbook = Button(mainscreenframe, text="[1] Enter New book", bg = "black", fg = "white", command = opennewbookmenu)
enternewbook.grid(row = 2, column = 1)

mainmenuplaceholder2 = Label(mainscreenframe, bg="black")
mainmenuplaceholder2.grid(row=3, column=1)
issuebookmain = Button(mainscreenframe, text="[2] Issue Book", bg = "black", fg = "white", command = issuebook)
issuebookmain.grid(row = 4, column = 1)

mainmenuplaceholder3 = Label(mainscreenframe, bg="black")
mainmenuplaceholder3.grid(row=5, column=1)
returnbookmain = Button(mainscreenframe, text="[3] Return Book", bg = "black", fg = "white", command = returnbook)
returnbookmain.grid(row = 6, column = 1)

mainmenuplaceholder4 = Label(mainscreenframe, bg="black")
mainmenuplaceholder4.grid(row=7, column=1)
checkbookstatusmain = Button(mainscreenframe, text="[4] Check Book Status", bg = "black", fg = "white", command = bookstatus)
checkbookstatusmain.grid(row = 8, column = 1)

# Buttons hover event binding
enternewbook.bind("<Enter>", button_enterhover)
enternewbook.bind("<Leave>", button_leavehover)
issuebookmain.bind("<Enter>", button_enterhover)
issuebookmain.bind("<Leave>", button_leavehover)
returnbookmain.bind("<Enter>", button_enterhover)
returnbookmain.bind("<Leave>", button_leavehover)
checkbookstatusmain.bind("<Enter>", button_enterhover)
checkbookstatusmain.bind("<Leave>", button_leavehover)

root.mainloop()