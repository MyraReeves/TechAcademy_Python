from tkinter import *

window = Tk()

# Text content and styling (such as button background color) is declared at the time of button creation.
# The same is also true for label widgets, which place text directly into the window.
textLabel = Label(window, text="Here are some buttons:", font=("Courier", 16), fg = "purple")

button1 = Button(window, text="One", bg = "lightgreen", font=("Helvetica", 14))
button2 = Button(window, text="Two", bg = "white")
button3 = Button(window, text="Three", bg = "lightblue", font=("Roman", 18))
button4 = Button(window, text="Four", bg="pink", font=("Terminal", 12))


# The above would create a blank window without further instruction.  Use "pack" to tell the widget to pack itself into its parent (which is "window").  The window will then automatically shrink to fit only the size of the button(s).  The default positioning for them will be to TOP stack them vertically in the order in which they were packed in.
# Use "side = LEFT" to position them a horizontal row from left to right.
# Use "padx" to add padding to the left/right, and "pady" to add padding to the top/bottom.
textLabel.pack(side=TOP, padx = 10, pady = 10)

button1.pack(side=LEFT, padx = 10, pady = 10)
button2.pack(side=LEFT, padx = 10, pady = 10)
button3.pack(side=LEFT, padx = 10, pady = 10)
button4.pack(side=LEFT, padx = 10, pady = 10)

# If "side = RIGHT" was used, then that would arrange them in a horizontal row from right to left.
# If "side = BOTTOM" was used, then that would arrange them in a vertical stack from the bottom up.




# Note:  In addition to pack() and grid(), there is place() method which is available for all standard widgets, which is the simplest of the three general geometry managers in Tkinter and allows you explicitly set the position and size of a window (either in absolute terms, or relative to another window), but it is usually not a good idea to use place() for ordinary window and dialog layouts.