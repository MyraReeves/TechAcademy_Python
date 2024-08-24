# SEPARATION OF CONCERNS is splitting a project into sections for usability or where a user would be concerned.  The idea is to focus on how a single piece should function or what kind of data it should contain.  You might see code files that contain a single block of code or just a few lines, and their file names would be relevant to what that code is used for.

# REUSABILITY means that you can reuse code without having to rewrite it.  Like saving a user input function in one file and then referencing it later anytime you need user input.



# EXAMPLE OF PYTHON WINDOW CREATION FROM STEP 284 QUIZ:
import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500, 300)
        self.master.maxsize(700, 500)
        self.master.title("My Program")
        self.lbl_fName = tk.Label(self.master, text="Hello User!")
        self.lbl_fName.grid(row=0, column=0, padx=(27, 0), pady=(10,0), sticky=N+W)

        self.closeButton = Button(self.master, text="Close", width=5, height=2)
        self.closeButton.grid(row=1, column=0, padx=(27,0), pady=(10,0), sticky=E+W)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
