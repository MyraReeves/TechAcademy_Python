from tkinter import *

window = Tk()

# Text content and styling (such as button background color) is declared at the time of button creation.
# The same is also true for label widgets, which place text directly into the window.
textLabel = Label(window, text="This is button number 2:", font=("Courier", 16), fg = "purple")

button1 = Button(window, text="One", bg = "lightgreen", font=("Helvetica", 14))
button2 = Button(window, text="Two", bg = "white")
button3 = Button(window, text="Three", bg = "lightblue", font=("Roman", 18))
button4 = Button(window, text="Four", bg="pink", font=("Terminal", 12))



# Using "grid" instead places the above widgets (the label and buttons) into a table or grid positioning where the parent ("window") is divided into rows and columns and each widget is placed in a cell.
# The grid manager keeps track of how many rows and columns are needed and will fill out the window accordingly.  It will keep track of how wide and tall each column and row must be respectively to accommodate the largest widget in that row/column.  Rows do not all have to be the same height and columns do not have to all be the same width.
textLabel.grid(row=1, column=0)

button1.grid(row=0, column=0)
button2.grid(row=1, column=1)
button3.grid(row=2, column=0, sticky=W)       # By default, the widgets will be centered inside their cells. Therefore, "sticky" and a compass position (north, east, south, or west) is used to position the widget inside of a cell.  In this case, it positions the "three" button to the left side of its cell instead of it being centered.
button4.grid(row=3, column=1)

