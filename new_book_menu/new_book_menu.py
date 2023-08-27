from pathlib import Path
from tkinter import *
from tkinter import messagebox # have to do this explicitly for some reason
from os import getcwd

import DataManager
# books_data, users_data, book_statuses = DataManager.get_data()

#------------------------------------------------------------------------------------------
def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(getcwd()+"\\all_assets\\new_book_menu_assets\\frame0")
    return ASSETS_PATH / Path(path)
#------------------------------------------------------------------------------------------
def open_new_book_menu():
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
    # submit button code
    def submitnewbook():
        fbookname = book_name_entry.get()
        fbookgenre = book_genre_entry.get()
        fbookauthor = book_author_entry.get()
        fbookisbn = book_isbn_entry.get()
        fbookisbn = fbookisbn.strip()
        try:
            fbookisbn = int(fbookisbn)
        except:
            messagebox.showerror("Error", "ISBN can only have numbers!")
        
        fbookisbn = str(fbookisbn).strip()
        if "-" not in fbookisbn and len(fbookisbn)!=13:
            messagebox.showerror("Error", "ISBN can only be 13 digits long!")
        elif "-" in fbookisbn and len(fbookisbn)!=16:
            messagebox.showinfo("Format", "For storing copies, please use the format \"ISBN-Copy Number\". Copy Number can only be double digit number (01, 03, 32, etc).")
        else: 
            print(fbookname, fbookgenre, fbookauthor, fbookisbn)
            result = DataManager.add_new_book(fbookname,fbookgenre,fbookisbn,fbookauthor)
            if result == "name":            
                book_name_entry.delete(0, END)
                messagebox.showerror("Error", "Book with same name already exists! To store a copy, simply add \"Copy no.\" at end.")
            elif result == "isbn":
                messagebox.showerror("Error", "Duplicate ISBN Detected! For storing copies, please use the format \"ISBN-Copy Number\". Copy Number can only be double digit number (01, 03, 32, etc).")
            elif result == "done":
                messagebox.showinfo("Success","Book has been succesfully added!")
        print(result)
    #------------------------------------------------------------------------------------------
    #bg img
    image_image_1 = PhotoImage(
        file=relative_to_assets("newbookmenubg.png"))
    newbookmenubg = canvas.create_image(
        400.0,
        304.0,
        image=image_image_1
    )
    #------------------------------------------------------------------------------------------
    canvas.create_rectangle(
        185.0,
        23.0,
        616.0,
        578.0,
        fill="#D9D9D9",
        outline="")
    #------------------------------------------------------------------------------------------
    image_image_2 = PhotoImage(
        file=relative_to_assets("heading.png"))
    heading = canvas.create_image(
        400.0,
        95.0,
        image=image_image_2
    )
    #------------------------------------------------------------------------------------------
    canvas.create_rectangle(
        216.0,
        170.0,
        582.0121459960938,
        171.0,
        fill="#B0855D",
        outline="")
    #------------------------------------------------------------------------------------------
    entry_image_1 = PhotoImage(
        file=relative_to_assets("book_name_entry.png"))
    entry_bg_1 = canvas.create_image(
        476.0,
        248.5,
        image=entry_image_1
    )
    book_name_entry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    book_name_entry.place(
        x=353.0,
        y=235.0,
        width=246.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    entry_image_2 = PhotoImage(
        file=relative_to_assets("book_author_entry.png"))
    entry_bg_2 = canvas.create_image(
        476.0,
        290.5,
        image=entry_image_2
    )
    book_author_entry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    book_author_entry.place(
        x=353.0,
        y=277.0,
        width=246.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    entry_image_3 = PhotoImage(
        file=relative_to_assets("book_isbn_entry.png"))
    entry_bg_3 = canvas.create_image(
        476.0,
        332.5,
        image=entry_image_3
    )
    book_isbn_entry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    book_isbn_entry.place(
        x=353.0,
        y=319.0,
        width=246.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    entry_image_4 = PhotoImage(
        file=relative_to_assets("book_genre_entry.png"))
    entry_bg_4 = canvas.create_image(
        476.0,
        374.5,
        image=entry_image_4
    )
    book_genre_entry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    book_genre_entry.place(
        x=353.0,
        y=361.0,
        width=246.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    button_image_1 = PhotoImage(
        file=relative_to_assets("submitbutton.png"))
    submitbutton = Button(
        canvas,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: submitnewbook(),
        relief="flat"
    )
    submitbutton.place(
        x=267.0,
        y=425.0,
        width=267.0,
        height=50.0
    )
    #------------------------------------------------------------------------------------------ 
    button_image_2 = PhotoImage(
        file=relative_to_assets("backbutton.png"))
    backbutton = Button(
        canvas,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:window.destroy(),
        relief="flat"
    )
    backbutton.place(
        x=267.0,
        y=499.0,
        width=267.0,
        height=50.0
    )
    #------------------------------------------------------------------------------------------
    image_image_3 = PhotoImage(
        file=relative_to_assets("subheading.png"))
    subheading = canvas.create_image(
        400.0,
        199.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("entrytext.png"))
    entrytext = canvas.create_image(
        270.0,
        314.0,
        image=image_image_4
    )
    #------------------------------------------------------------------------------------------
    window.resizable(False, False)
    window.mainloop()
    #------------------------------------------------------------------------------------------

    