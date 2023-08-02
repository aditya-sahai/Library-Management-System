from pathlib import Path
from tkinter import *
from os import getcwd



def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(getcwd()+"\\all_assets\\book_status_menu_assets\\frame0")
    return ASSETS_PATH / Path(path)
def open_book_status_menu():
    #------------------------------------------------------------------------------------------
    window = Toplevel()
    window.geometry("800x600")
    window.configure(bg = "#0078D4")
    #------------------------------------------------------------------------------------------
    def statusbutton():
        fbookname = book_name_entry.get()
        fphoneno = phone_no_entry.get()
        fbookisbn = book_isbn_entry.get()
        print(fbookname, fphoneno, fbookisbn)

        book_name_entry.delete(0, END)
        phone_no_entry.delete(0, END)
        book_isbn_entry.delete(0, END)
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
    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        400.0,
        299.0,
        image=image_image_1
    )
    #------------------------------------------------------------------------------------------
    # main rectangke
    canvas.create_rectangle(
        185.0,
        23.0,
        616.0,
        578.0,
        fill="#D9D9D9",
        outline="")
    #------------------------------------------------------------------------------------------
    # Line rectangle
    canvas.create_rectangle(
        216.0,
        170.0,
        582.0121459960938,
        171.0,
        fill="#B0855D",
        outline="")
    #------------------------------------------------------------------------------------------
    button_image_1 = PhotoImage(
        file=relative_to_assets("check_status_button.png"))
    check_status_button = Button(
        canvas,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=statusbutton,
        relief="flat"
    )
    check_status_button.place(
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
        399.0,
        205.0,
        image=image_image_3
    )
    #------------------------------------------------------------------------------------------
    entry_image_1 = PhotoImage(
        file=relative_to_assets("book_name_entry.png"))
    entry_bg_1 = canvas.create_image(
        494.0,
        271.5,
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
        x=383.0,
        y=258.0,
        width=222.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    entry_image_2 = PhotoImage(
        file=relative_to_assets("phone_no_entry.png"))
    entry_bg_2 = canvas.create_image(
        494.0,
        311.5,
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
        x=383.0,
        y=298.0,
        width=222.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    entry_image_3 = PhotoImage(
        file=relative_to_assets("book_isbn_entry.png"))
    entry_bg_3 = canvas.create_image(
        494.0,
        351.5,
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
        x=383.0,
        y=338.0,
        width=222.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        275.0,
        313.0,
        image=image_image_4
    )
    #------------------------------------------------------------------------------------------
    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        263.0,
        353.0,
        image=image_image_5
    )
    #------------------------------------------------------------------------------------------
    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        263.0,
        312.0,
        image=image_image_6
    )
    #------------------------------------------------------------------------------------------
    window.resizable(False, False)
    window.mainloop()
    #------------------------------------------------------------------------------------------