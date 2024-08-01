from tkinter import *

myExampleWindow = Tk()

instructions = Label(myExampleWindow, text = "Enter text below:")

# To communicate with an entry widget, use a StringVar to hold a string of text.  This will allow us to set its contents and read it using get(), below:
userText = StringVar()

# To input text from a user, use an Entry() widget:
e = Entry(myExampleWindow, textvariable = userText)


e.pack(padx = 30, pady = 5, side = BOTTOM)
instructions.pack(pady = 5, side = TOP)


# To read what the user wrote, use the following get() method in the console:
#       userText.get()


# To have something already written inside the entry widget, use the set() method:
userText.set("This is example text written by the dev and can be deleted or edited by the user")
