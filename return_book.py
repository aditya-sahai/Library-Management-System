from tkinter import *
# from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import random

from CRUDOperations import *

mainheadingfont = ("Footlight MT Light", 20)
 
def returnbook():
    global returnbookname, returnbookgenre

    # list having all the genres for the genre dropdown menu 
    genre_options = ["Fiction", "Fantasy", "Adventure", "Non-Fiction", "Educational"]

    # configuring new window
    returnmenu = Toplevel()
    returnmenu.title("Book Return")
    returnmenu.configure(bg="black")
    returnmenu.geometry("700x500")

    # new window elements
    returnframe = LabelFrame(returnmenu, text = "Book Return Menu", padx = 50, pady=25, bg = "black", fg="white")
    returnframe.pack(pady=(125, 0))

    returnlabel = Label(returnframe, text = "       Return Book       ", font=mainheadingfont, bg="black", fg="white")
    returnlabel.grid(row = 0, column = 0, columnspan = 3)

    # input fields 
    nbfps1 = Label(returnframe, bg="black").grid(row = 1, column = 1)
    label1 = Label(returnframe, text = "Enter Book Name:", bg = "black", fg = "white").grid(row = 2, column = 0)
    returnbookname = Entry(returnframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    returnbookname.grid(row = 2, column = 1)

    
    nbfps2 = Label(returnframe, bg="black").grid(row = 3, column = 1)
    label2 = Label(returnframe, text = "Enter Book Genre:", bg = "black", fg = "white").grid(row = 4, column = 0)
    returnbookgenre = StringVar()
    returnbookgenre.set(genre_options[random.randint(0,4)])
    genredropdown = OptionMenu(returnframe, returnbookgenre, *genre_options)
    genredropdown.config(width=19, bg="black", fg="white", activebackground="#1a1a1a", activeforeground="white", highlightthickness=0)
    genredropdown.grid(row = 4, column = 1)
    # returnbookgenre = Entry(returnframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    # returnbookgenre.grid(row = 4, column = 1)

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

    # return button code
    nbfps6 = Label(returnframe, bg="black").grid(row = 9, column = 1)
    nbfps7 = Label(returnframe, bg="black").grid(row = 10, column = 1)
    return_button = Button(returnframe, text="Return Book", bg = "black", fg = "white", command = returnthebook).grid(row = 11, column = 2)

    # go back button
    goback_button = Button(returnframe, text="Back", bg = "black", fg = "white", command = returnmenu.destroy).grid(row = 11, column = 0)

    '''
    Changing the color of the buttons is not working here for some reason

    return_button.bind("<Enter>", button_enterhover)
    return_button.bind("<Leave>", button_leavehover)
    goback_button.bind("<Enter>", button_enterhover)
    goback_button.bind("<Leave>", button_leavehover)
    '''

def returnthebook():

    freturnbookname = returnbookname.get()
    freturnbookgenre = returnbookgenre.get()
    freturnbookgenre = freturnbookgenre.lower()

    record_found = get_book_record(freturnbookgenre, freturnbookname)

    if record_found:
        if edit_existing_record(freturnbookgenre, freturnbookname):
            response_success = messagebox.showinfo("Information", "Book has been successfully returned!")
        else:
            respose_failure = messagebox.showwarning("Information", "Book is issued by someone else. Try again later.")  # feature: show who issued it, etc
    else:
        reponse_doesntexist = messagebox.showerror("Information", "Book doesn't exist! Please enter a valid book and check your data.")  

    
    #clear the input fields
    returnbookname.delete(0, END)