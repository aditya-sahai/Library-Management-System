from pathlib import Path
from tkinter import *
from tkinter import messagebox
from os import getcwd

import DataManager

#------------------------------------------------------------------------------------------
def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(getcwd()+"\\all_assets\\issue_book_menu_assets\\frame0")
    return ASSETS_PATH / Path(path)
#------------------------------------------------------------------------------------------
def open_issue_book_menu():
    window = Toplevel()
    window.geometry("800x600")
    window.configure(bg = "#0078D4")

    canvas = Canvas(
        window,
        bg = "#0078D4",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)
    #------------------------------------------------------------------------------------------
    def issuenewbook():
        fbookisbn = book_isbn_entry.get()
        fissuephone = phone_no_entry.get()

        try:
            fissuephone = int(fissuephone)
        except:
            messagebox.showerror("Type Error", "Please enter valid data types!")
        if len(str(fissuephone))!=10:
            messagebox.showerror("Error", "Library can only be 7 digits long!")

        if issue_duration_entry.get() == "Duration in days":
            fissueduration = 7
        else:
            try:
                fissueduration = int(issue_duration_entry.get())
            except:
                messagebox.showerror("Type Error", "Please enter valid data types!")
                phone_no_entry.delete(0, END)

        fissuephone = str(fissuephone).strip()        
        fbookisbn = str(fbookisbn).strip()
        fissuephone = str(fissuephone).strip()
        result = DataManager.issue_book(fbookisbn,fissuephone,fissueduration)
        if result == "id":
            messagebox.showerror("User Not Found", "User not found! Please check user ID.")
            phone_no_entry.delete(0, END)
        elif result == "isbn": # This case will never happen here as we're already checking for it in the bigger if block
            messagebox.showerror("ISBN Not Found", "Entered ISBN not found!")
        elif result == "expired":
            messagebox.showerror("Membership Expired", "User's membership has expired! Go back to main menu, and renew user membership to continue.")
        elif result == "not-in-shelf":
            messagebox.showerror("Not In Shelf", "Book has already been issued by someone else! To check for copies, try entering \"-01\",\"-02\" and so on.")
            book_isbn_entry.delete(0, END)            
        elif result == "done":
            messagebox.showinfo("Success", "Book issued successfully")
            book_isbn_entry.delete(0, END)
            phone_no_entry.delete(0, END)
            issue_duration_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "Book not found.")
            book_isbn_entry.delete(0, END)
            phone_no_entry.delete(0, END)
            issue_duration_entry.delete(0, END)
        
        print(fbookisbn, fissuephone, fissueduration)
    #------------------------------------------------------------------------------------------
    image_image_1 = PhotoImage(
        file=relative_to_assets("issuebookmenubg.png"))
    issuebookmenubg = canvas.create_image(
        399.0,
        299.0,
        image=image_image_1
    )
    #------------------------------------------------------------------------------------------
    # Main rectangle
    canvas.create_rectangle(
        184.0,
        23.0,
        615.0,
        578.0,
        fill="#D9D9D9",
        outline="")
    #------------------------------------------------------------------------------------------
    # this is the line!!!
    canvas.create_rectangle(
        216.0,
        170.0,
        582.0121459960938,
        171.0,
        fill="#B0855D",
        outline="")
    #------------------------------------------------------------------------------------------
    entry_image_1 = PhotoImage(
        file=relative_to_assets("book_isbn_entry.png"))
    entry_bg_1 = canvas.create_image(
        500.5,
        286.5,
        image=entry_image_1
    )
    book_isbn_entry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    book_isbn_entry.place(
        x=400.0,
        y=273.0,
        width=201.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    entry_image_2 = PhotoImage(
        file=relative_to_assets("phone_no_entry.png"))
    entry_bg_2 = canvas.create_image(
        500.5,
        328.5,
        image=entry_image_2
    )
    phone_no_entry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    phone_no_entry.place(
        x=400.0,
        y=315.0,
        width=201.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    entry_image_3 = PhotoImage(
        file=relative_to_assets("issue_duration_entry.png"))
    entry_bg_3 = canvas.create_image(
        500.5,
        370.5,
        image=entry_image_3
    )
    issue_duration_entry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    issue_duration_entry.place(
        x=400.0,
        y=357.0,
        width=201.0,
        height=25.0
    )
    issue_duration_entry.insert(0, "Duration in days")
    #------------------------------------------------------------------------------------------
    button_image_2 = PhotoImage(
        file=relative_to_assets("issuebutton.png"))
    issuebutton = Button(
        canvas,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=issuenewbook,
        relief="flat"
    )
    issuebutton.place(
        x=267.0,
        y=425.0,
        width=267.0,
        height=50.0
    )
    '''
    alternate code for centering the text box in the image
    issue_duration_entry.place(
        x=407.0,
        y=361.0,
        width=190.0,
        height=20.0
    )
    '''
    #------------------------------------------------------------------------------------------
    button_image_3 = PhotoImage(
        file=relative_to_assets("backbutton.png"))
    backbutton = Button(
        canvas,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=window.destroy,
        relief="flat"
    )
    backbutton.place(
        x=267.0,
        y=499.0,
        width=267.0,
        height=50.0
    )
    #------------------------------------------------------------------------------------------
    image_image_2 = PhotoImage(
        file=relative_to_assets("heading.png"))
    heading = canvas.create_image(
        400.0,
        95.0,
        image=image_image_2
    )
    #------------------------------------------------------------------------------------------
    image_image_3 = PhotoImage(
        file=relative_to_assets("subheading.png"))
    subheading = canvas.create_image(
        410.0,
        206.0,
        image=image_image_3
    )
    #------------------------------------------------------------------------------------------
    image_image_4 = PhotoImage(
        file=relative_to_assets("entrytext.png"))
    entrytext = canvas.create_image(
        295.0,
        329.0,
        image=image_image_4
    )
    #------------------------------------------------------------------------------------------
    window.resizable(False, False)
    window.mainloop()
    #------------------------------------------------------------------------------------------

