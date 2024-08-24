from tkinter import *

popupWindow = Tk()

# A listbox is created using the Listbox() method.  The "height" parameter limits how many liens will show.
myListbox = Listbox(popupWindow, height = 3, width = 50)
myListbox.pack()

# Items can be inserted into the listbox at the END...
myListbox.insert(END, "First entry")
myListbox.insert(END, "Here is a second entry in the box")
myListbox.insert(END, "🗹 The third entry is this one")
myListbox.insert(END, "This fourth entry won't show because the listbox is set to be only be three lines tall!")

# ...Or (for example, if needed later on) items can also be inserted at the beginning of the list using an index of zero...
myListbox.insert(0, "New first entry overriding the initial one!")

# ...Or items can be inserted into the middle of the listbox by using whatever index is desired for the new item:
myListbox.insert(2, "Here is a brand new third entry!")


# To create a scrollbar for the listbox (to see the fourth thru sixth lines that don't fit in the box), first create the scrollbar:
myScrollbar = Scrollbar(popupWindow, orient=VERTICAL)

# And set its position and height inside of the window:
myScrollbar.pack(side = LEFT, fill = Y)

# And then link it to the listbox.  Two calls are needed, one each to link each to the other.
myScrollbar.configure(command=myListbox.yview)
myListbox.configure(yscrollcommand=myScrollbar.set)



# A tuple of the indexes of selected items can be returned in the console window by using the curselection() command.
# For example, if a dev selects the third visible line ("Here is a brand new third entry!") and then in the console window types 
#       myListbox.curselection()
# it will return a one item tuple of
#       (2,)




# Items in the listbox can also be deleted, by specifying the starting index to delete thru the desired ending index to delete.  Therefore, to clear an entire listbox, use:
myListbox.delete(0, END)
# Note that the scrollbar still shows, since that is a separate element outside of the listbox.