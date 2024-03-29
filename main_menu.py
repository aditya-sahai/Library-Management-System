from tkinter import messagebox # have to do this explicitly for some reason
from pathlib import Path
from tkinter import *
from os import getcwd
from subprocess import Popen
from sys import path
path.append(getcwd()+"\\new_book_menu")
path.append(getcwd()+"\\new_user_menu")
path.append(getcwd()+"\\return_book_menu")
path.append(getcwd()+"\\user_info_menu")
path.append(getcwd()+"\\book_status_menu")
path.append(getcwd()+"\\edit_user_menu")
path.append(getcwd()+"\\issue_book_menu")
path.append(getcwd()+"\\renew_user_menu")
path.append(getcwd()+"\\browse_books_menu")
path.append(getcwd()+"\\log_file_menu")

from issue_book_menu import open_issue_book_menu
from new_book_menu import open_new_book_menu
from return_book_menu import open_return_book_menu
from book_status_menu import open_book_status_menu
from new_user_menu import open_new_user_menu
from edit_user_menu import open_edit_user_menu
from user_info_menu import open_user_info_menu
from renew_user_menu import open_renew_user_menu
from browse_books_menu import open_browse_books_menu
from log_file_menu import open_browse_logs_menu

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(getcwd()+"\\all_assets\\main_menu_assets\\frame0")

def open_log_file():
    Popen("notepad log.csv")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#------------------------------------------------------------------------------------------
# Creating main window and setting properties
window = Tk()

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
#------------------------------------------------------------------------------------------
# Background image of the library
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("main_menu_bg.png"))
image_1 = canvas.create_image(
    400.0,
    300.0,
    image=image_image_1
)
#------------------------------------------------------------------------------------------
# Main, white rectangle at the back
canvas.create_rectangle(
    185.0,
    23.0,
    616.0,
    578.0,
    fill="#D9D9D9",
    outline="")
#------------------------------------------------------------------------------------------
# Library management system waali image
image_image_2 = PhotoImage(
    file=relative_to_assets("heading.png"))
image_2 = canvas.create_image(
    400.0,
    109.0,
    image=image_image_2
)
#------------------------------------------------------------------------------------------
button_image_1 = PhotoImage(
    file=relative_to_assets("book_history.png"))
book_history = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_browse_logs_menu,
    relief="flat"
)
book_history.place(
    x=414.0,
    y=431.0,
    width=189.0,
    height=37.0
)
#------------------------------------------------------------------------------------------
button_image_2 = PhotoImage(
    file=relative_to_assets("user_status.png"))
user_status = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_user_info_menu,
    relief="flat"
)
user_status.place(
    x=414.0,
    y=376.0,
    width=189.0,
    height=37.0
)
#------------------------------------------------------------------------------------------
button_image_3 = PhotoImage(
    file=relative_to_assets("edit_user.png"))
edit_user = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_edit_user_menu,
    relief="flat"
)
edit_user.place(
    x=414.0,
    y=320.0,
    width=189.0,
    height=37.0
)
#------------------------------------------------------------------------------------------
button_image_4 = PhotoImage(
    file=relative_to_assets("renew_user.png"))
renew_user = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command = open_renew_user_menu,
    relief="flat"
)
renew_user.place(
    x=414.0,
    y=265.0,
    width=189.0,
    height=37.0
)
#------------------------------------------------------------------------------------------
button_image_5 = PhotoImage(
    file=relative_to_assets("add_new_user.png"))
add_new_user = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=open_new_user_menu,
    relief="flat"
)
add_new_user.place(
    x=414.0,
    y=209.0,
    width=189.0,
    height=37.0
)
#------------------------------------------------------------------------------------------
button_image_6 = PhotoImage(
    file=relative_to_assets("browse_books.png"))
browse_books = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=open_browse_books_menu,
    relief="flat"
)
browse_books.place(
    x=200.0,
    y=432.0,
    width=189.0,
    height=37.0
)
#------------------------------------------------------------------------------------------
button_image_7 = PhotoImage(
    file=relative_to_assets("return_book.png"))
return_book = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=open_return_book_menu,
    relief="flat"
)
return_book.place(
    x=200.0,
    y=320.0,
    width=189.0,
    height=37.0
)
#------------------------------------------------------------------------------------------
button_image_8 = PhotoImage(
    file=relative_to_assets("issue_book.png"))
issue_book = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=open_issue_book_menu,
    relief="flat"
)
issue_book.place(
    x=198.0,
    y=264.0,
    width=189.0,
    height=37.0
)
#------------------------------------------------------------------------------------------
button_image_9 = PhotoImage(
    file=relative_to_assets("add_new_book.png"))
add_new_book = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=open_new_book_menu,
    # For some reason, command=open_new_book_menu() doesn't work and breaks a lot of stuff???
    relief="flat"
)
add_new_book.place(
    x=198.0,
    y=209.0,
    width=189.0,
    height=37.0
)
#------------------------------------------------------------------------------------------
button_image_10 = PhotoImage(
    file=relative_to_assets("book_status.png"))
book_status = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=open_book_status_menu,
    relief="flat"
)
book_status.place(
    x=198.0,
    y=376.0,
    width=189.0,
    height=37.0
)
#------------------------------------------------------------------------------------------
window.resizable(False, False)
window.mainloop()
#------------------------------------------------------------------------------------------
