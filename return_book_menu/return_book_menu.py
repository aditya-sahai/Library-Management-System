from pathlib import Path
from tkinter import *
from tkinter import messagebox
from os import getcwd
import DataManager

#------------------------------------------------------------------------------------------
def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(getcwd()+"\\all_assets\\return_book_menu_assets\\frame0")
    return ASSETS_PATH / Path(path)
#------------------------------------------------------------------------------------------

def open_return_book_menu():
    window = Toplevel()
    window.geometry("800x600")
    window.configure(bg = "#0078D4")
    #------------------------------------------------------------------------------------------
    # return button code
    def returnbook():
        fbookname = book_name_entry.get()
        fphoneno = phone_no_entry.get()
        fbookisbn = book_isbn_entry.get()

        if not fbookisbn.isnumeric():
            messagebox.showerror("Error", "ISBN can only have numbers!")    

        if "-" not in str(fbookisbn) and len(str(fbookisbn))!=13:
            messagebox.showerror("Error", "ISBN can only be 13 digits long!")
            book_isbn_entry.delete(0, END)
        elif "-" in str(fbookisbn) and len(str(fbookisbn))!=16:
            messagebox.showinfo("Format", "For storing copies, please use the format \"ISBN-Copy Number\". Copy Number can only be double digit number (01, 03, 32, etc).")
            book_isbn_entry.delete(0, END)        
            
        fbookisbn = str(fbookisbn).strip()
        result = DataManager.return_book(fbookisbn)
        print(result)
        if result == "done-1":
            messagebox.showinfo("Late Return","Returned late. 1 day subtracted from user membership.")            
        elif result == "done":
            messagebox.showinfo("Success","Book returned successfully")
        elif result == "not-found":
            messagebox.showerror("Error","Book has not been issued. For checking stored copies, please use the format \"ISBN-Copy Number\". Copy Number can only be double digit number (01, 03, 32, etc). ")
            book_isbn_entry.delete(0, END)
        print(fbookname, fphoneno, fbookisbn)
    #------------------------------------------------------------------------------------------
    canvas = Canvas(
        window,
        bg = "#0078D4",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    #------------------------------------------------------------------------------------------
    # bg image
    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("returnbookmenubg.png"))
    returnbookmenubg = canvas.create_image(
        399.0,
        299.0,
        image=image_image_1
    )
    #------------------------------------------------------------------------------------------
    # main rectangle
    canvas.create_rectangle(
        185.0,
        23.0,
        616.0,
        578.0,
        fill="#D9D9D9",
        outline="")
    #------------------------------------------------------------------------------------------
    # line rectangle
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
        490.0,
        286.5,
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
        x=379.0,
        y=273.0,
        width=222.0,
        height=25.0
    )
    book_name_entry.insert(0, "Optional")
    #------------------------------------------------------------------------------------------
    entry_image_2 = PhotoImage(
        file=relative_to_assets("phone_no_entry.png"))
    entry_bg_2 = canvas.create_image(
        490.0,
        326.5,
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
        x=379.0,
        y=313.0,
        width=222.0,
        height=25.0
    )
    phone_no_entry.insert(0, "Optional")
    #------------------------------------------------------------------------------------------
    button_image_1 = PhotoImage(
        file=relative_to_assets("return_button.png"))
    return_button = Button(
        canvas,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=returnbook,
        relief="flat"
    )
    return_button.place(
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
        395.0,
        207.0,
        image=image_image_3
    )
    #------------------------------------------------------------------------------------------
    entry_image_3 = PhotoImage(
        file=relative_to_assets("book_isbn_entry.png"))
    entry_bg_3 = canvas.create_image(
        490.0,
        366.5,
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
        x=379.0,
        y=353.0,
        width=222.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    image_image_4 = PhotoImage(
        file=relative_to_assets("booknametext.png"))
    booknametext = canvas.create_image(
        271.0,
        328.0,
        image=image_image_4
    )
    #------------------------------------------------------------------------------------------
    # image_image_5 = PhotoImage(
    #     file=relative_to_assets("bookisbntext.png"))
    # bookisbntext = canvas.create_image(
    #     259.0,
    #     366.0,
    #     image=image_image_5
    # )
    #------------------------------------------------------------------------------------------
    # image_image_6 = PhotoImage(
    #     file=relative_to_assets("phonenotext.png"))
    # phonenotext = canvas.create_image(
    #     259.0,
    #     325.0,
    #     image=image_image_6
    # )
    #------------------------------------------------------------------------------------------
    window.resizable(False, False)
    window.mainloop()
    #------------------------------------------------------------------------------------------