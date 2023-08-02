from tkinter import *

root = Tk()

def onclick():
    myLabel = Label(root, text = input_field.get())
    myLabel.pack()
    ''' 
    you can also do something like this:
    inputted_thing = input_field.get()
    myLabel = Label(root, text = inputted_thing)
    myLabel.pack()
    '''

# Creating an input field
input_field = Entry(root, width = "10", bg = "gray", fg = "white", borderwidth=10)
input_field.pack()

input_field.get() # this will get whatever is put into the box
input_field.insert(0, "Enter ur data") # this is for some default text already in the program. 0 is the 0th button.



# The command statement is for on clicking the button, do this
myButton = Button(root, text = "totally not sus", command = onclick)


myButton.pack()

root.mainloop()