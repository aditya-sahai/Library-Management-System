from pathlib import Path
from tkinter import *
from os import getcwd
import DataManager
from tkinter import messagebox # have to do this explicitly for some reason


def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(getcwd()+"\\all_assets\\edit_user_menu_assets\\frame0")
    return ASSETS_PATH / Path(path)

#------------------------------------------------------------------------------------------
def open_edit_user_menu():
    window = Toplevel()
    window.geometry("800x600")
    window.configure(bg = "#0078D4")
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
        file=relative_to_assets("edituserbackground.png"))
    image_1 = canvas.create_image(
        400.0,
        307.0,
        image=image_image_1
    )
    #------------------------------------------------------------------------------------------
    def edit_user():
        oldphone = ogphonenoentry.get()
        newphone = newphonenoentry.get()
        newfname = newfirstnameentry.get()
        newlname = newlastnameentry.get()
        newaddress = newaddressentry.get()

        oldphone,newphone=oldphone.strip(),newphone.strip()
        oldphonecheck = DataManager.checkphoneformat(oldphone)
        newphonecheck = DataManager.checkphoneformat(newphone)
        if oldphonecheck == "datatype":
            messagebox.showerror("Data Type Error","Old Phone number can only contain numbers!")
            ogphonenoentry.delete(0, END)       
        elif oldphonecheck == "length":
            messagebox.showerror("Length Error","Please ensure old phone number is 10 digits long!") 
            ogphonenoentry.delete(0, END)
        elif newphonecheck == "datatype":
            messagebox.showerror("Data Type Error","New Phone number can only contain numbers!")
            newphonenoentry.delete(0, END)
        elif newphonecheck == "length":
            messagebox.showerror("Length Error","Please ensure new phone number is 10 digits long!")  
            newphonenoentry.delete(0, END)  
        
        elif oldphonecheck=="correctformat" and newphonecheck=="correctformat":
            result = DataManager.edit_user(oldphone,newfname,newlname,newphone)
            if result == "id":
                messagebox.showerror("Not Found","Entered user ID not found!")
            elif result == "done":
                messagebox.showinfo("Success","User data has been successfully edited!")
                ogphonenoentry.delete(0, END)
                newphonenoentry.delete(0, END)
                newfirstnameentry.delete(0, END)
                newlastnameentry.delete(0, END)
                newaddressentry.delete(0, END)
    #------------------------------------------------------------------------------------------
    canvas.create_rectangle(
        185.0,
        23.0,
        616.0,
        578.0,
        fill="#D9D9D9",
        outline="")
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
        file=relative_to_assets("ogphonenoentry.png"))
    entry_bg_1 = canvas.create_image(
        492.5,
        245.0,
        image=entry_image_1
    )
    ogphonenoentry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    ogphonenoentry.place(
        x=386.0,
        y=235.0,
        width=213.0,
        height=18.0
    )
    #------------------------------------------------------------------------------------------
    image_image_2 = PhotoImage(
        file=relative_to_assets("heading.png"))
    image_2 = canvas.create_image(
        400.0,
        95.0,
        image=image_image_2
    )
    #------------------------------------------------------------------------------------------
    entry_image_2 = PhotoImage(
        file=relative_to_assets("newphonenoentry.png"))
    entry_bg_2 = canvas.create_image(
        493.0,
        281.0,
        image=entry_image_2
    )
    newphonenoentry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    newphonenoentry.place(
        x=386.0,
        y=271.0,
        width=214.0,
        height=18.0
    )
    #------------------------------------------------------------------------------------------
    entry_image_3 = PhotoImage(
        file=relative_to_assets("newfirstnameentry.png"))
    entry_bg_3 = canvas.create_image(
        492.5,
        317.0,
        image=entry_image_3
    )
    newfirstnameentry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    newfirstnameentry.place(
        x=386.0,
        y=307.0,
        width=213.0,
        height=18.0
    )
    #------------------------------------------------------------------------------------------
    entry_image_4 = PhotoImage(
        file=relative_to_assets("newlastnameentry.png"))
    entry_bg_4 = canvas.create_image(
        493.0,
        353.0,
        image=entry_image_4
    )
    newlastnameentry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    newlastnameentry.place(
        x=386.0,
        y=343.0,
        width=214.0,
        height=18.0
    )
    #------------------------------------------------------------------------------------------
    entry_image_5 = PhotoImage(
        file=relative_to_assets("newaddressentry.png"))
    entry_bg_5 = canvas.create_image(
        493.0,
        389.0,
        image=entry_image_5
    )
    newaddressentry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    newaddressentry.place(
        x=386.0,
        y=379.0,
        width=214.0,
        height=18.0
    )
    #------------------------------------------------------------------------------------------
    button_image_2 = PhotoImage(
        file=relative_to_assets("submitbutton.png"))
    submitbutton = Button(
        canvas,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=edit_user,
        relief="flat"
    )
    submitbutton.place(
        x=267.0,
        y=430.0,
        width=267.0,
        height=50.0
    )
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
        y=496.0,
        width=267.0,
        height=50.0
    )
    #------------------------------------------------------------------------------------------
    image_image_3 = PhotoImage(
        file=relative_to_assets("subheading.png"))
    image_3 = canvas.create_image(
        400.0,
        195.0,
        image=image_image_3
    )
    #------------------------------------------------------------------------------------------
    image_image_4 = PhotoImage(
        file=relative_to_assets("labels.png"))
    image_4 = canvas.create_image(
        287.0,
        317.0,
        image=image_image_4
    )
    #------------------------------------------------------------------------------------------
    window.resizable(False, False)
    window.mainloop()
