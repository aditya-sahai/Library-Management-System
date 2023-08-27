from pathlib import Path
from tkinter import *
from tkinter import messagebox # have to do this explicitly for some reason
from os import getcwd
import DataManager

#------------------------------------------------------------------------------------------
def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(getcwd()+"\\all_assets\\user_info_menu_assets\\frame0")
    return ASSETS_PATH / Path(path)
#------------------------------------------------------------------------------------------
def open_user_info_menu():

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
        file=relative_to_assets("backgrounnd.png"))
    image_1 = canvas.create_image(
        400.0,
        299.0,
        image=image_image_1
    )
    #------------------------------------------------------------------------------------------
    def get_info():
        tphone = phonenoentry.get()
        fphone = str(tphone)
        print(tphone)
        print(fphone)
        result = DataManager.user_status(fphone)
        print(result)
        tempstring = "Registration Date: "+result[0]+", Expiry Date: "+result[1]+", Expired: "+result[2]
        if result == "id":
            messagebox.showerror("Not Found","User not found!")
        else:
            messagebox.showinfo("User Found",tempstring)

    #------------------------------------------------------------------------------------------
    canvas.create_rectangle(
        185.0,
        22.0,
        616.0,
        577.0,
        fill="#D9D9D9",
        outline="")
    #------------------------------------------------------------------------------------------
    image_image_2 = PhotoImage(
        file=relative_to_assets("heading.png"))
    image_2 = canvas.create_image(
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
        file=relative_to_assets("phonenoentry.png"))
    entry_bg_1 = canvas.create_image(
        490.0,
        286.5,
        image=entry_image_1
    )
    phonenoentry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    phonenoentry.place(
        x=379.0,
        y=273.0,
        width=222.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    button_image_2 = PhotoImage(
        file=relative_to_assets("getinfobutton.png"))
    getinfobutton = Button(
        canvas,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=get_info,
        relief="flat"
    )
    getinfobutton.place(
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
        command=lambda: print("backbutton clicked"),
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
    image_3 = canvas.create_image(
        407.0,
        206.0,
        image=image_image_3
    )
    #------------------------------------------------------------------------------------------
    image_image_4 = PhotoImage(
        file=relative_to_assets("labels.png"))
    image_4 = canvas.create_image(
        286.0,
        288.0,
        image=image_image_4
    )
    #------------------------------------------------------------------------------------------
    window.resizable(False, False)
    window.mainloop()

