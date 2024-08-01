from tkinter import *

myWindow = Tk()


# A frame is a widget whose sole purpose is to contain other widgets.  Groups of widgets, whether packed or placed in a grid, may be combined in a single Frame.  Frames may then be packed with other widgets and frames.  This feature lets devs create just about any kind of layout.
myFrame = Frame(myWindow)

button1 = Button(myFrame, text="One", fg = "green")
button2 = Button(myFrame, text="Two", fg = "darkred")
button3 = Button(myFrame, text="Three", fg = "blue")

myLabel = Label(myWindow, text="This label will end up positioned above all the buttons")   # Notice the difference of "myWindow" instead of "myFrame"


button1.pack(side=LEFT, padx = 10, pady = 5)
button2.pack(side=LEFT, padx = 10, pady = 5)
button3.pack(side=LEFT, padx = 10, pady = 5)
myLabel.pack()
myFrame.pack()
