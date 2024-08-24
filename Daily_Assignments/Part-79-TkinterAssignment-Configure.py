from tkinter import *

myWindow = Tk()

myFrame = Frame(myWindow)

button1 = Button(myFrame, text="One", fg = "green")
button2 = Button(myFrame, text="Two", fg = "darkred")
button3 = Button(myFrame, text="Three", fg = "blue")
myLabel = Label(myWindow, text="This label will end up positioned above all the buttons")

button1.pack(side=LEFT, padx = 10, pady = 5)
button2.pack(side=LEFT, padx = 10, pady = 5)
button3.pack(side=LEFT, padx = 10, pady = 5)
myLabel.pack()
myFrame.pack()


# The configure() method can use any keyword argument to affect a widget.  For example, the following will override the above styling/text for the first button and instead cause it to say "Uno" in pink letters on a black background:
button1.configure(text="Uno!", fg="pink", bg="black")

# Buttons are tied to callback functions using the parameter "command".  This is typically done when the button is created, but can also be done using "configure".  For example, we can create a function that prints a message to the console...
def button1Message():
    print("The first button has been pressed successfully!  Huzzah!")
    
# ...and then use the "configure" method with "command" to add functionality to the first button:
button1.configure(command=button1Message)
# That button will now print the message to the console whenever pressed.