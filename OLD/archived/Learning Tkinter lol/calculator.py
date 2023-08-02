from tkinter import *

root = Tk()
root.title("Calculator")

def equal():
    second_number = input.get()
    input.delete(0, END)
    input.insert(0, f_num + int(second_number))

def add():
    first_number = input.get()
    global f_num # creates a global variable that can be used even outside here, like in equal function
    f_num = int(first_number)
    input.delete(0, END)

def button_click(number):
    current = input.get() #Used to show which number you just pressed, but BEFORE what you just put
    input.delete(0, END) #Used to clear the input field
    input.insert(0, str(current)+str(number)) #To fix that, we used a current variable.

def clear():
    input.delete(0, END)


input = Entry(root, width = 50, borderwidth = 5)
# Notice the columnspan
input.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)



# Putting Lambda allows us to take arguements it the () in the command parameter
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))

button_add = Button(root, text = "+", padx = 39, pady = 20, command = add)
button_equal = Button(root, text = "=", padx = 91, pady = 20, command = equal)
button_clear = Button(root, text = "Clear", padx = 79, pady = 20, command = clear)



# Putting buttons on the screen
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)

button_add.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan=2)
button_clear.grid(row = 4, column = 1, columnspan=2)



root.mainloop()