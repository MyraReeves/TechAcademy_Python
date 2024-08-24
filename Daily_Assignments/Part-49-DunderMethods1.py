# This file is a module for only saving functions (block of codes that can be reused) inside of it.  Not for calling them.  Call on them within a second file.  This type of file is called a module.

# Dunder (double underline) methods are built in to Python and will perform special actions when used.



# Define a function named "printApp" using () and :
def printApp():
    # Use this function to get the name of this file and store it in a variable called "name" using the __name__ Python dunder method:
    name = (__name__)
    # Return back the name of this file whenever anyone calls on this printApp function:
    return name

# When called on in a separate file, the above function should return a value of "Part_49_DunderMethods1.py"