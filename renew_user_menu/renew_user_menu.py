from pathlib import Path
from tkinter import *
from os import getcwd
from tkinter import messagebox # have to do this explicitly for some reason
import DataManager

def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(getcwd()+"\\all_assets\\renew_user_menu_assets\\frame0")
    return ASSETS_PATH / Path(path)

def open_renew_user_menu():
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
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        400.0,
        299.0,
        image=image_image_1
    )
    #------------------------------------------------------------------------------------------
    def renew_user():
        fphone = phonenoentry.get().strip()
        fduration = durationentry.get().strip()

        formatcheck = DataManager.checkphoneformat(fphone)
        if formatcheck == "datatype":
            messagebox.showerror("Data Type Error","Library ID can only contain numbers!")
            phonenoentry.delete(0, END)
        elif formatcheck == "length":
            messagebox.showerror("Length Error","Please ensure library ID is 7 digits long!")
            phonenoentry.delete(0, END)

        elif str(fduration).isnumeric() == False:
            messagebox.showerror("Data Type Error","Renew duration can only contain numbers!")

        elif formatcheck == "correctformat" and str(fduration).isnumeric()==True:
            fduration = int(fduration)
            result = DataManager.renew_user(fphone,fduration)
            if result == "id":
                messagebox.showerror("Not Found","Entered library ID not found, please try again.")
                phonenoentry.delete(0, END)
            elif result == "done":
                messagebox.showinfo("Success","User's membership has been successfully renewed")
                phonenoentry.delete(0, END)
                durationentry.delete(0, END)
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
        file=relative_to_assets("image_2.png"))
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
        file=relative_to_assets("entry_1.png"))
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
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        490.0,
        335.5,
        image=entry_image_2
    )
    durationentry = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    durationentry.place(
        x=379.0,
        y=322.0,
        width=222.0,
        height=25.0
    )
    #------------------------------------------------------------------------------------------
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        canvas,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=renew_user,
        relief="flat"
    )
    button_2.place(
        x=267.0,
        y=425.0,
        width=267.0,
        height=50.0
    )
    #------------------------------------------------------------------------------------------
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        canvas,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=window.destroy,
        relief="flat"
    )
    button_3.place(
        x=267.0,
        y=499.0,
        width=267.0,
        height=50.0
    )
    #------------------------------------------------------------------------------------------
    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        409.0,
        207.0,
        image=image_image_3
    )
    #------------------------------------------------------------------------------------------
    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        286.0,
        288.0,
        image=image_image_4
    )
    #------------------------------------------------------------------------------------------
    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        286.0,
        337.0,
        image=image_image_5
    )
    window.resizable(False, False)
    window.mainloop()
    #------------------------------------------------------------------------------------------
