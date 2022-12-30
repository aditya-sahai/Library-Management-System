from tkinter import *

root = Tk()

# state = DISABLED will disable the button
# myButton = Button(root, text = "totally not sus", state=DISABLED)

# its pretty obvious what padx and pady do lol
# myButton = Button(root, text = "totally not sus", padx = "50", pady = "50")

'''
def onclick():
    myLabel = Label(root, text = "Hello world")
    myLabel.pack()

# The command statement is for on clicking the button, do this
myButton = Button(root, text = "totally not sus", command = onclick)
'''

# fg is the text color, bg is the background color
myButton = Button(root, text = "totally not sus", fg="blue", bg="red")



myButton.pack()

root.mainloop()