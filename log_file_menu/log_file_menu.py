from tkinter import *
from tkinter import ttk
import csv 
    #------------------------------------------------------------------------------------------
def open_browse_logs_menu():
    root = Toplevel()
    root.title("Browse Log Files")
    root.geometry("1280x720")
    treeframe = Frame(root)
    treeframe.place(relx=0.03, rely=0.02, width=1200, height=600)
    #------------------------------------------------------------------------------------------
    style = ttk.Style()
    style.theme_use("clam")
    #------------------------------------------------------------------------------------------
    tree_scroll = Scrollbar(treeframe)
    tree_scroll.pack(side=RIGHT, fill=Y)
    #------------------------------------------------------------------------------------------
    mytree = ttk.Treeview(treeframe,show="headings",yscrollcommand=tree_scroll.set,selectmode="browse") #show=headings is what hides the ghost column, it is very important.
    mytree.place(relx=-0.008, rely=0.02, width=1200, height=600)
    tree_scroll.config(command=mytree.yview)
    #------------------------------------------------------------------------------------------
    #Defining columns
    mytree["columns"] = ("User ID","User Name","Phone","Book Name","ISBN","Issue Date","Expected Return Date","Actual Return Date")

    #formatting columns
    mytree.column("#0",width=0)
    # alternatively, to hide the ghost column, you could not do the show=headings and do:
    # mytree.column("#0",width=0,stretch=NO)
    mytree.column("User ID", anchor=CENTER,width=50)
    mytree.column("User Name",anchor=CENTER,width=50)
    mytree.column("Phone",anchor=CENTER,width=50)
    mytree.column("Book Name",anchor=CENTER,width=50)
    mytree.column("ISBN", anchor=CENTER,width=50)
    mytree.column("Issue Date", anchor=CENTER,width=50)
    mytree.column("Expected Return Date", anchor=CENTER,width=50)
    mytree.column("Actual Return Date", anchor=CENTER,width=50)
    #------------------------------------------------------------------------------------------

    # Creating headings (that the user sees)

    mytree.heading("#0",text="GHOST COLUMN")
    mytree.heading("User ID", text="User ID", anchor=CENTER)
    mytree.heading("User Name", text="User Name", anchor=CENTER)
    mytree.heading("Phone", text="Phone", anchor=CENTER)
    mytree.heading("Book Name", text="Book Name", anchor=CENTER)
    mytree.heading("ISBN",text="ISBN", anchor=CENTER)
    mytree.heading("Issue Date",text="Issue Data", anchor=CENTER)
    mytree.heading("Expected Return Date",text="Expected Return", anchor=CENTER)
    mytree.heading("Actual Return Date",text="Actual Return", anchor=CENTER)

    #------------------------------------------------------------------------------------------

    myfile = open("log.csv","r")
    reader = csv.reader(myfile)
    counter = 1
    for x in reader:
        if reader.line_num==1:
            continue
        mytree.insert(parent="",index="end",iid=counter,text="THIS ISNT SUPPOSED TO SHOW UP",values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
        counter+=1

    # mytree.place(relx=0.03, rely=0.02, width=1200, height=600)
    #------------------------------------------------------------------------------------------
    root.mainloop()