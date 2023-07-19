from tkinter import *

#This is the main screen
main_menu = Tk()

myLabel1 = Label(main_menu, text = "Hello World")
myLabel2 = Label(main_menu, text = "This is a test")

''''
#Shoving the label onto the screen. Doesn't give us a whole lot of control on where to put stuff. 
myLabel.pack()
'''

#Grids, on the other hand, allow us to control the position using rows and columns, like in excel
myLabel1.grid(row = 0, column=0)
myLabel2.grid(row = 1, column=5) #this just goes to column 2. It cant just go straight to 5.

#this is the main program loop that keeps updating stuff until the program ends
main_menu.mainloop()