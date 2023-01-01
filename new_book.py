from tkinter import *
# from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

from CRUDOperations import *

mainheadingfont = ("Footlight MT Light", 20)


def opennewbookmenu():
    global newbookmenu, book_name, book_author, book_isbn, book_genre

    # configuring new window
    newbookmenu = Toplevel()
    newbookmenu.title("New Book Entry")
    newbookmenu.configure(bg="black")
    newbookmenu.geometry("700x500")

    # new window elements
    newbookframe = LabelFrame(newbookmenu, text = "New Book Entry Menu", padx = 50, pady=25, bg = "black", fg="white")
    newbookframe.pack(pady=(75, 0))
    nbheadinglabel = Label(newbookframe, text = "      New Book Entry     ", font=mainheadingfont, bg="black", fg="white")
    nbheadinglabel.grid(row = 0, column = 0, columnspan = 3)

    # input fields 
    nbfps1 = Label(newbookframe, bg="black").grid(row = 1, column = 1)
    label1 = Label(newbookframe, text = "Enter Book Name:", bg = "black", fg = "white").grid(row = 2, column = 0)
    book_name = Entry(newbookframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    book_name.grid(row = 2, column = 1)

    nbfps2 = Label(newbookframe, bg="black").grid(row = 3, column = 1)
    label2 = Label(newbookframe, text = "Enter Book Author:", bg = "black", fg = "white").grid(row = 4, column = 0)
    book_author = Entry(newbookframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    book_author.grid(row = 4, column = 1)

    nbfps4 = Label(newbookframe, bg="black").grid(row = 5, column = 1)
    label3 = Label(newbookframe, text = "Enter Book ISBN:", bg = "black", fg = "white").grid(row = 6, column = 0)
    book_isbn = Entry(newbookframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    book_isbn.grid(row = 6, column = 1)

    nbfps5 = Label(newbookframe, bg="black").grid(row = 7, column = 1)
    label3 = Label(newbookframe, text = "Enter Book Genre:", bg = "black", fg = "white").grid(row = 8, column = 0)
    book_genre = Entry(newbookframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    book_genre.grid(row = 8, column = 1)

    # submit button code
    nbfps6 = Label(newbookframe, bg="black").grid(row = 9, column = 1)
    nbfps7 = Label(newbookframe, bg="black").grid(row = 10, column = 1)
    submit_button = Button(newbookframe, text="Submit", bg = "black", fg = "white", command = submitnewbook).grid(row = 11, column = 2)

    # go back button
    back_button = Button(newbookframe, text="Back", bg = "black", fg = "white", command = newbookmenu.destroy).grid(row = 11, column = 0)

    # buttons hover binding
    submit_button.bind("<Enter>", button_enterhover)
    submit_button.bind("<Leave>", button_leavehover)
    back_button.bind("<Enter>", button_enterhover)
    back_button.bind("<Leave>", button_leavehover)

# what to do after user has submitted data
def submitnewbook():
    # these variables return the data user has entered
    fbookname = book_name.get()
    fbookauthor = book_author.get()
    fbookisbn = book_isbn.get()
    fbookgenre = book_genre.get()
    fbookgenre = fbookgenre.lower()
    response = messagebox.showinfo("Information", "Book entry was successfull")

    write_new_record(fbookgenre, fbookname, fbookisbn, fbookauthor)

    #clear the input fields

    book_name.delete(0, END)
    book_author.delete(0, END)
    book_isbn.delete(0, END)
    book_genre.delete(0, END)






