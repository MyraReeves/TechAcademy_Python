#
# Python:  version #
#
# Author:  your name and/or the entire team of authors
#
# Purpose: What was the intention of this software.  What is it supposed to do for us.  What are we supposed to get from it.



# Create a function called "start"
def start():
    # call on the "get_number" function and print the result on the screen:
    print(get_number())


# Create a function called "get_number" 
def get_number():
    # Save the integer value 12 inside of a variable called "number":
    number = 12
    # Return whatever value is saved inside of the "name" variable to whatever function (in this case, the "start" function) had called on this get_number function:
    return number





# Tell Python we are running this as a script
if __name__ == "__main__":
    # and which functions to call, in order
    start()


# Reminders:  
# functionName(variable) means that we pass in the variable.
# return variable means that we are returning the variable back to the calling function.  