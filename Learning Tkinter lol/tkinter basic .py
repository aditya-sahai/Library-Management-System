from tkinter import *

#This is the main screen
main_menu = Tk()

myLabel = Label(main_menu, text = "Hello World") #Label is used to specify a container where we place stuff

#Shoving the label onto the screen. Doesn't give us a whole lot of control on where to put stuff. 
myLabel.pack()

#this is the main program loop that keeps updating stuff until the program ends
main_menu.mainloop()