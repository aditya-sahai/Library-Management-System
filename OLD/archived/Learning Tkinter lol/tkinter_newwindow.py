from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("MAIN WINDOW")

def open():
    new_window = Toplevel()
    new_window.title("TOP WINDOW")
    # Notice how it is placed inside new_window and not root
    window_label = Label(new_window, text = "This is on the upper window").pack()  
    #button for closing the new window 
    btn2 = Button(new_window, text="Close New Window", command = new_window.destroy).pack()
btn1 = Button(root, text="New Window Open", command = open).pack()


'''
new_window = Toplevel()
new_window.title("TOP WINDOW")
# Notice how it is placed inside new_window and not root
window_label = Label(new_window, text = "This is on the upper window").pack()
'''

root.mainloop()