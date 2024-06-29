# This file is a module for only saving functions inside of it.  Not calling them.  Call them within a second file.


# Dunder (double underline) methods are built in to Python and will perform special actions when used.

def printApp():
    # Get the name of this file and store it in the variable "name" using the __name__ dunder method:
    name = (__name__)
    return name
