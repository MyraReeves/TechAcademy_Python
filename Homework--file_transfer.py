import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil


class ParentWindow (Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("Transfer All Files To New Folder")

        # "Select Source" button:
        self.sourceDirectoryButton = Button(text="Source Folder", width=20, bg="papayawhip", command=self.sourceDir)
        self.sourceDirectoryButton.grid(row=0, column=0, padx=(20, 10), pady=(30,0))

        # Display area for the chosen source:
        self.sourceDirectoryEntry = Entry(width=75, bg="papayawhip")
        self.sourceDirectoryEntry.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))   # padx and pady are the same as the button to ensure they will line up.

        # "Select Destination" button:
        self.destinationDirectoryButton = Button(text="Destination Folder", width=20, bg="lavender", command=self.destiDir)
        self.destinationDirectoryButton.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        # Display area for the chosen destination:
        self.destinationDirectoryEntry = Entry(width=75, bg="lavender")
        self.destinationDirectoryEntry.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10)) # padx and pady are the same as the button to ensure they will line up.

        # File Transfer button:
        self.transferButton = Button(text="Transfer All Files", width = 30, fg="darkgreen", bg="palegreen", command=self.transferFiles)
        self.transferButton.grid(row=2, column=0, padx=(200, 0), pady=(0, 15))



    # Function to select the source directory:
    def sourceDir(self):
        selectSourceDirectory = tkinter.filedialog.askdirectory()

        # Clear contents of the source Entry widget (from index zero thru the end) to allow the newly selected path to be inserted:
        self.sourceDirectoryEntry.delete(0, END)

        # Insert the file path of the folder that the user clicks on into the source Entry widget:
        self.sourceDirectoryEntry.insert(0, selectSourceDirectory)


    # Function to select the destination directory:
    def destiDir(self):
        selectDestinationDirectory = tkinter.filedialog.askdirectory()

        # Clear contents of destination Entry widget to allow the newly selected file path to be inserted:
        self.destinationDirectoryEntry.delete(0, END)

        # Insert into the destination Entry widget the file path of the folder the user clicks on:
        self.destinationDirectoryEntry.insert(0, selectDestinationDirectory)


    # Function to transfer files:
    def transferFiles (self):
        source = self.sourceDirectoryEntry.get()
        destination = self.destinationDirectoryEntry.get()

        # Get the list of files currently inside the source folder:
        source_files = os.listdir(source)

        # Move each file from the source to the destination folder:
        for iteration in source_files:
            shutil.move(source + '/' + iteration, destination)
            # Confirm file transfer in console:
            print('\n ✔️ ' + iteration + ' successfully transferred to \n' + destination)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop