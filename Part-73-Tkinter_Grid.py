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

        # Insert labels onto the form/window...
        # Instantiate the single line Label() class widget and then configure it by telling it to be: placed on the main window self master, setting the text content, setting the font tuple of style and size, setting the foreground font color, and setting the background color of the textbox:
        self.labelFirstName = Label(self.master, text='First Name:', font=("Courier", 16), fg="lightblue", bg="black")
        # Paint the geometry object onto a very specific location in the form/window by referencing its variable name and using the grid() geometry manager. Set the margins around the label using pad() for the x-axis and y-axis:
        self.labelFirstName.grid(row=0, column=0, padx=(20,0), pady=(50,0))

        # Repeat for the next label:
        self.labelLastName = Label(self.master, text='Last Name:', font=("Courier", 16), fg="lightyellow", bg="black")
        self.labelLastName.grid(row=1, column=0, padx=(33,0), pady=(20,0))


        # Instructions to build a textbox by instantiating the single line Entry() class widget and then configuring it by telling it to be placed on self master, setting the text content, setting the font tuple of style and size, setting the foreground font color, and setting the background color of the textbox.
        self.textBox_FirstName = Entry(self.master, text=self.variableFirstName, font=("Helvetica", 16), fg="black", bg="lightblue")
        # Paint the geometry object onto a very specific location of the form/window. Remember to set the margins around the text box using pad() for the x-axis and y-axis:
        self.textBox_FirstName.grid(row=0, column=1, padx=(0,0), pady=(50,0))

        # Repeat for the last name variable:
        self.textBox_LastName = Entry(self.master, text=self.variableLastName, font=("Helvetica", 16), fg="black", bg="lightyellow")
        self.textBox_LastName.grid(row=1, column=1, padx=(0,0), pady=(20,0))

        # Note: To make an entry span two columns of space, add in ", colspan=2" after "column".  Leaving it blank automatically tells the program that the column span is the size of only one column.


        # Add a submit button to the page. Place it on the main window self master. On the face of the button have it say "Submit"
        self.buttonSubmit = Button(self.master, text="Submit", width=10, font=("Courier", 16), fg="green", bg="lightgreen")
        # Place the button onto the page using the grid.  Have it stick to the upper right of its cell using NorthEast
        self.buttonSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        # Add a CANCEL button to the page. Place it on the main window self master. On the face of the button have it say "Submit"
        self.buttonCancel = Button(self.master, text="CANCEL", width=10, font=("Courier", 16), fg="red", bg="pink")
        # Place the button onto the page using the grid.  Have it stick to the upper right of its cell using NorthEast
        self.buttonCancel.grid(row=2, column=0, padx=(20,0), pady=(30,0), sticky=NE)





# When we launch this...
if __name__ == "__main__":
    # Instantiate the Tkinter,
    root = Tk()
    # pass it over to the class program,
    App = ParentWindow(root)
    # and create a main loop for that to run so that the Tkinter window stays open
    root.mainloop()
