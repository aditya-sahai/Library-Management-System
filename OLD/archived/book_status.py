from tkinter import *
# from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import random

from CRUDOperations import *

mainheadingfont = ("Footlight MT Light", 20)
 
def bookstatus():
    global statusbookname, statusbookgenre

    # list having all the genres for the genre dropdown menu 
    genre_options = ["Fiction", "Fantasy", "Adventure", "Non-Fiction", "Educational"]

    # configuring new window
    statusmenu = Toplevel()
    statusmenu.title("Book Status")
    statusmenu.configure(bg="black")
    statusmenu.geometry("700x500")

    # new window elements
    statusframe = LabelFrame(statusmenu, text = "Book Status Menu", padx = 50, pady=25, bg = "black", fg="white")
    statusframe.pack(pady=(125, 0))

    returnlabel = Label(statusframe, text = "    Check Book Status    ", font=mainheadingfont, bg="black", fg="white")
    returnlabel.grid(row = 0, column = 0, columnspan = 3)

    # input fields 
    nbfps1 = Label(statusframe, bg="black").grid(row = 1, column = 1)
    label1 = Label(statusframe, text = "Enter Book Name:", bg = "black", fg = "white").grid(row = 2, column = 0)
    statusbookname = Entry(statusframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    statusbookname.grid(row = 2, column =1)

    
    nbfps2 = Label(statusframe, bg="black").grid(row = 3, column = 1)
    label2 = Label(statusframe, text = "Enter Book Genre:", bg = "black", fg = "white").grid(row = 4, column = 0)
    statusbookgenre = StringVar()
    statusbookgenre.set(genre_options[random.randint(0,4)])
    genredropdown = OptionMenu(statusframe, statusbookgenre, *genre_options)
    genredropdown.config(width=19, bg="black", fg="white", activebackground="#1a1a1a", activeforeground="white", highlightthickness=0)
    genredropdown.grid(row = 4, column = 1)

    # statusbookgenre = Entry(statusframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    # statusbookgenre.grid(row = 4, column = 1)

    '''
    nbfps4 = Label(issueframe, bg="black").grid(row = 5, column = 1)
    label3 = Label(issueframe, text = "Enter Book ISBN:", bg = "black", fg = "white").grid(row = 6, column = 0)
    book_isbn = Entry(issueframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    book_isbn.grid(row = 6, column = 1)

    nbfps5 = Label(issueframe, bg="black").grid(row = 7, column = 1)
    label3 = Label(issueframe, text = "Enter Book Genre:", bg = "black", fg = "white").grid(row = 8, column = 0)
    book_genre = Entry(issueframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    book_genre.grid(row = 8, column = 1)
    '''

    # status button code
    nbfps6 = Label(statusframe, bg="black").grid(row = 9, column = 1)
    nbfps7 = Label(statusframe, bg="black").grid(row = 10, column = 1)
    status_button = Button(statusframe, text="Check Book Status", bg = "black", fg = "white", command = checkbookstatus).grid(row = 11, column = 2)

    # go back button
    goback_button = Button(statusframe, text="Back", bg = "black", fg = "white", command = statusmenu.destroy).grid(row = 11, column = 0)

    '''
    Changing the color of the buttons is not working here for some reason

    status_button.bind("<Enter>", button_enterhover)
    status_button.bind("<Leave>", button_leavehover)
    goback_button.bind("<Enter>", button_enterhover)
    goback_button.bind("<Leave>", button_leavehover)
    '''

def checkbookstatus():

    fstatusbookname = statusbookname.get()
    fstatusbookgenre = statusbookgenre.get()
    fstatusbookgenre = fstatusbookgenre.lower()

    bookstatus = get_book_record(fstatusbookgenre, fstatusbookname)

    line = ""
    for data in bookstatus:
        if data == "Status":
            if bookstatus["Status"]:
                status = "In shelf"
            else:
                status = "Not in shelf"
            line += f"Status - {status}\n"
        else:
            line += f"{data} - {bookstatus[data]}\n"

    if bookstatus:
        response = messagebox.showinfo("Information", line)
    else:
        response = messagebox.showerror("Error", "Book doesn't exist. Please enter a valid book name or check your data!")

    #clear the input fields
    statusbookname.delete(0, END)
