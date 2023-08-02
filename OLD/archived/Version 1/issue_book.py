from tkinter import *
#from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

mainheadingfont = ("Footlight MT Light", 20)
 
def issuebook():
    global issuebookname

    # configuring new window
    issuemenu = Toplevel()
    issuemenu.title("Book Issue")
    issuemenu.configure(bg="black")
    issuemenu.geometry("700x500")

    # new window elements
    issueframe = LabelFrame(issuemenu, text = "Book Issue Menu", padx = 50, pady=25, bg = "black", fg="white")
    issueframe.pack(pady=(125, 0))

    issuelabel = Label(issueframe, text = "        Issue Book       ", font=mainheadingfont, bg="black", fg="white")
    issuelabel.grid(row = 0, column = 0, columnspan = 3)

    # input fields 
    nbfps1 = Label(issueframe, bg="black").grid(row = 1, column = 1)
    label1 = Label(issueframe, text = "Enter Book Name:", bg = "black", fg = "white").grid(row = 2, column = 0)
    issuebookname = Entry(issueframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    issuebookname.grid(row = 2, column = 1)

    nbfps2 = Label(issueframe, bg="black").grid(row = 3, column = 1)
    label2 = Label(issueframe, text = "Enter Name Of Borrower:", bg = "black", fg = "white").grid(row = 4, column = 0)
    borrower_name = Entry(issueframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    borrower_name.grid(row = 4, column = 1)

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

    # issue button code
    nbfps6 = Label(issueframe, bg="black").grid(row = 9, column = 1)
    nbfps7 = Label(issueframe, bg="black").grid(row = 10, column = 1)
    issue_button = Button(issueframe, text="Issue Book", bg = "black", fg = "white", command = issuethebook).grid(row = 11, column = 2)

    # go back button
    goback_button = Button(issueframe, text="Back", bg = "black", fg = "white", command = issuemenu.destroy).grid(row = 11, column = 0)


def issuethebook():
    global status
    # these variables return the data user has entered
    fbookissue = issuebookname.get()
    response = messagebox.showinfo("Information", "Book has been successfully issued!") 

    """
    change this part for the status of the book
    """
    status = "not-in-shelf"

    #clear the input fields
    issuebookname.delete(0, END)
