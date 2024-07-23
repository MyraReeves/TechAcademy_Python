# Import the Tkinter module:
import tkinter

# Import ALL of its widgets:
from tkinter import *


# Create a Tkinter window:
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        # Make it so that the Tkinter window can't be resized
        self.master.resizable(width=False, height=False)
        # Set the width of the window to 700px and the height to 400px:
        self.master.geometry('{}x{}'.format(700, 400))
        # Give the window the title of "Learning Tkinter":
        self.master.title('Learning Tkinter')
        # Make the window have a dark red background color:
        self.master.config(bg='darkred')


        # Add widgets into the Tkinter window...

        # Create variables to use later.  Options for types include BooleanVar, DoubleVar, IntVar, and StringVar.
        self.variableFirstName = StringVar()
        self.variableLastName = StringVar()

        # Assign values to those variables:
        self.variableFirstName.set('Bob')
        self.variableLastName.set('Smith')

        # Use the console and the get() to make sure that the above went correctly.  The user won't see this:
        print(self.variableFirstName.get())
        print(self.variableLastName.get())

        # Setup instructions to build a textbox by instantiating the single line Entry() class widget and then configuring it by telling it to be placed on self master, setting the text content, setting the font tuple of style and size, setting the foreground font color, and setting the background color of the textbox.
        self.textBox_FirstName = Entry(self.master, text=self.variableFirstName, font=("Helvetica", 16), fg="black", bg="lightblue")
        # Paint the geometry object onto the form/window by referencing its name and using the unspecific pack() geometry manager
        self.textBox_FirstName.pack()

        # Repeat for the last name variable:
        self.textBox_LastName = Entry(self.master, text=self.variableLastName, font=("Helvetica", 16), fg="yellow", bg="black")
        self.textBox_LastName.pack()




# When we launch this...
if __name__ == "__main__":
    # Instantiate the Tkinter,
    root = Tk()
    # pass it over to the class program,
    App = ParentWindow(root)
    # and create a main loop for that to run so that the Tkinter window stays open
    root.mainloop()
