from pathlib import Path
from tkinter import *
from tkinter import messagebox #have to do this explicitly for some reason
from os import getcwd
import DataManager

def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(getcwd()+"\\all_assets\\new_user_menu_assets\\frame0")
    return ASSETS_PATH / Path(path)
def open_new_user_menu():
    #------------------------------------------------------------------------------------------
    window = Toplevel()
    window.geometry("800x600")
    window.configure(bg = "#0078D4")
    #------------------------------------------------------------------------------------------
    def add_new_user():
        ffirstusername = (firstnameentry.get()).strip()
        flastusername = (lnameentry.get()).strip()
        fphoneno = (phonenoentry.get()).strip()
        faddress = (addressentry.get()).strip()

        result = DataManager.add_new_user(ffirstusername,flastusername,fphoneno)
        if DataManager.checkphoneformat2(fphoneno)=="datatype":
            messagebox.showerror("Data Type Error","Phone number can only contain numbers!")
        elif DataManager.checkphoneformat2(fphoneno)=="length":
            messagebox.showerror("Length Error","Please ensure phone number is 10 digits long!")

        # if result == "phone":
        #     messagebox.showerror("Duplicate Phone No.","User with this phone number already exists!")
        #     phonenoentry.delete(0, END)
        if type(result)==tuple:
            tempstr = "User has been successfully added with a default membership duration of 30 days. User ID: "+str(result[1])
            messagebox.showinfo("Success",tempstr)
            firstnameentry.delete(0, END)
            lnameentry.delete(0, END)
            phonenoentry.delete(0, END)
            addressentry.delete(0, END)
        else:
            messagebox.showerror("ERROR","If you're seeing this, something did not go the way it was supposed to. Please contact the developers.")
        
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
        file=relative_to_assets("newusermenubg.png"))
    newusermenubg = canvas.create_image(
        400.0,
        304.0,
        image=image_image_1
    )
    #------------------------------------------------------------------------------------------
    # Main rectangle
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
        file=relative_to_assets("fnameentry.png"))
    entry_bg_1 = canvas.create_image(
        476.0,
        248.5,
        image=entry_image_1
    )
    firstnameentry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    firstnameentry.place(
        x=353.0,
        y=235.0,
        width=246.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    entry_image_2 = PhotoImage(
        file=relative_to_assets("lnameentry.png"))
    entry_bg_2 = canvas.create_image(
        476.0,
        290.5,
        image=entry_image_2
    )
    lnameentry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    lnameentry.place(
        x=353.0,
        y=277.0,
        width=246.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    entry_image_3 = PhotoImage(
        file=relative_to_assets("phonenoentry.png"))
    entry_bg_3 = canvas.create_image(
        476.0,
        332.5,
        image=entry_image_3
    )
    phonenoentry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    phonenoentry.place(
        x=353.0,
        y=319.0,
        width=246.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    entry_image_4 = PhotoImage(
        file=relative_to_assets("addressentry.png"))
    entry_bg_4 = canvas.create_image(
        476.0,
        374.5,
        image=entry_image_4
    )
    addressentry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    addressentry.place(
        x=353.0,
        y=361.0,
        width=246.0,
        height=25.0
    )
    addressentry.insert(0, "Optional")
    #------------------------------------------------------------------------------------------
    button_image_2 = PhotoImage(
        file=relative_to_assets("submitbutton.png"))
    submitbutton = Button(
        canvas,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=add_new_user,
        relief="flat"
    )
    submitbutton.place(
        x=267.0,
        y=425.0,
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
        400.0,
        199.0,
        image=image_image_3
    )
    #------------------------------------------------------------------------------------------
    image_image_4 = PhotoImage(
        file=relative_to_assets("labeltext.png"))
    labeltext = canvas.create_image(
        267.0,
        304.0,
        image=image_image_4
    )
    #------------------------------------------------------------------------------------------
    window.resizable(False, False)
    window.mainloop()
    #------------------------------------------------------------------------------------------