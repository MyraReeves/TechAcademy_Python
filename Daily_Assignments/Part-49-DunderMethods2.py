# "Dunder" is short for "double under(line)".  Double underline methods (also called "magic methods") don't need to be called directly.  Instead, Python calls them when it needs to know how you want something handled - like object initialization. The name comes from the fact that they have two underscore lines on either side, as both a prefix and a suffix.


#  The dunder __name__ is a built-in method that is the name of the REMOTE file you are calling on from an outside file, as a string.


# Declare a new function that assigns the name of THIS (Part-49-...2) file being typed in to a variable called "name" and then returns it to be seen when the function is called.
def printApp_Part2():
    name = (__name__)
    return name
# When called on REMOTELY, this Part2 function will return a value of "Part-49-DunderMethods2.py"



# Import the other file, the one containing a printApp() function that, when called, will return a variable with a value of "Part_49_DunderMethods1.py"
import Part_49_DunderMethods1



# __main__ is the module script being ran (i.e this file that is being written in) instead of any imported module



if __name__ == "__main__":
    # Call the function that was created above inside this script file:
    print("First, I am running code from {}".format( printApp_Part2() ) )
    # Since we're calling this function from inside the same file it was created in instead of remotely, instead of showing the name of this file being currently typed in this will show "__main__" because it is the very module being run!

    # Call the code from the imported module file (i.e. tell it to go to the module file name and then the desired function inside it):
    print("And now, instead, I am running code from {}".format( Part_49_DunderMethods1.printApp() ) )
    # Since this module is saved in a different, remote file, when we call on it the __name__ dunder will show that other file name
