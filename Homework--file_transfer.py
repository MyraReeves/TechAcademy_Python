import tkinter as tk
from tkinter import *

class ParentWindow (Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("Move Files")

        # "Select Source" Button:
        self.sourceDirectoryButton = Button(text="Select Source", width=20)
        self.sourceDirectoryButton.grid(row=0, column=0, padx=(20, 10), pady=(30,0))

        # Entry area for the source:
        self.sourceDirectory = Entry(width=75)
        self.sourceDirectory.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))   # padx and pady are the same as the button to ensure they will line up.

        # "Select Destination" Button:
        self.destinationDirectoryButton = Button(text="Select Destination", width=20)
        self.destinationDirectoryButton.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        # Entry area for the destination:
        self.destinationDirectory = Entry(width=75)
        self.destinationDirectory.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10)) # padx and pady are the same as the button to ensure they will line up.



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop