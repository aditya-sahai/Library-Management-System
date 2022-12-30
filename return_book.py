from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

mainheadingfont = ("Footlight MT Light", 20)
 
def returnbook():
    global returnbookname

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

    '''
    nbfps2 = Label(returnframe, bg="black").grid(row = 3, column = 1)
    label2 = Label(returnframe, text = "Enter Name Of Borrower:", bg = "black", fg = "white").grid(row = 4, column = 0)
    borrower_name = Entry(returnframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    borrower_name.grid(row = 4, column = 1)

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
    issue_button = Button(returnframe, text="Return Book", bg = "black", fg = "white", command = returnthebook).grid(row = 11, column = 2)

    # go back button
    goback_button = Button(returnframe, text="Back", bg = "black", fg = "white", command = returnmenu.destroy).grid(row = 11, column = 0)


def returnthebook():
    global status
    # these variables return the data user has entered
    fbookreturn = returnbookname.get()
    response = messagebox.showinfo("Information", "Book has been successfully returned!") 

    """
    change this part for the status of the book
    """
    status = "in-shelf"
    
    #clear the input fields
    returnbookname.delete(0, END)
