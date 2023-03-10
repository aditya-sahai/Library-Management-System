from tkinter import *
# from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import random

from CRUDOperations import *

mainheadingfont = ("Footlight MT Light", 20)
 
def issuebook():
    global issuebookname, borrower_name, issuebookgenre

    # list having all the genres for the genre dropdown menu 
    genre_options = ["Fiction", "Fantasy", "Adventure", "Non-Fiction", "Educational"]

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
    label2 = Label(issueframe, text = "Enter Book Genre:", bg = "black", fg = "white").grid(row = 4, column = 0)
    issuebookgenre = StringVar()
    issuebookgenre.set(genre_options[random.randint(0,4)])
    genredropdown = OptionMenu(issueframe, issuebookgenre, *genre_options)
    genredropdown.config(width=19, bg="black", fg="white", activebackground="#1a1a1a", activeforeground="white", highlightthickness=0)
    genredropdown.grid(row = 4, column = 1)

    # issuebookgenre = Entry(issueframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    # issuebookgenre.grid(row = 4, column = 1)

    
    nbfps4 = Label(issueframe, bg="black").grid(row = 5, column = 1)
    label3 = Label(issueframe, text = "Enter Borrower Name:", bg = "black", fg = "white").grid(row = 6, column = 0)
    borrower_name = Entry(issueframe, width = "25", bg = "black", fg = "white", borderwidth=1, insertbackground = "white")
    borrower_name.grid(row = 6, column = 1)
    
    '''
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

    '''
    Changing the color of the buttons is not working here for some reason
    
    issue_button.bind("<Enter>", button_enterhover)
    issue_button.bind("<Leave>", button_leavehover)
    goback_button.bind("<Enter>", button_enterhover)
    goback_button.bind("<Leave>", button_leavehover)
    '''

def issuethebook():
    # these variables return the data user has entered
    fborrower_name = borrower_name.get()
    fbookissuename = issuebookname.get()

    # returning proper genres as chosen from the dropdown menu
    fissuebookgenre = issuebookgenre.get()
    fissuebookgenre = fissuebookgenre.lower()

    # handling various cases of the book

    # for when the borrower name is not entered 
    record_found = get_book_record(fissuebookgenre, fbookissuename)
    if not fborrower_name:
        fborrower_name = ""

    if record_found:
        if edit_existing_record(fissuebookgenre, fbookissuename, fborrower_name):
            response_success = messagebox.showinfo("Information", "Book has been successfully issued!")
        else:
            respose_failure = messagebox.showwarning("Information", "Book is issued by someone else. Try again later.")  # feature: show who issued it, etc
    else:
        reponse_doesntexist = messagebox.showerror("Information", "Book doesn't exist! Please enter a valid book and check your data.")  

    # add feature for permission denied to edit file because it is open

    #clear the input fields
    issuebookname.delete(0, END)
    borrower_name.delete(0, END)
