
# Create a function to collect information from the user:
def getInfo():
    variable1 = input("\nPlease provide a numeric value: ")
    variable2 = input("\nWhat is the second numeric value you wish to add to that? ")
    return(variable1, variable2)
# Note that the program automatically accepts all input as strings, not as integers


# Create a function to compute the information given. Be sure to call on the above function within it:
def compute():
    # Create a while loop to keep asking for the two numbers until we tell the loop to turn off/exit
    go = True
    while go:
        variable1, variable2 = getInfo()

        # Add a try/exception block in case of errors. Make sure to convert the string values entered into integers
        try:
            variable3 = int(variable1) + int(variable2)
            go = False            # Turns off the loop!


        # The except parts below will display a message if the user made a mistake that causes a fatal exception

        # We know from what is returned by the program that if the user doesn't enter a numeric value that the default error has a label of "ValueError".  That default message would read "ValueError: invalid literal for int() with base 10"  Therefore, we can create a better worded exception error message that addresses that most likely scenario 
        except ValueError as e:                         # e being the default message the code would state on its own
            print("\n{}: \nYou did not provide a numeric value! Make sure you are entering a number".format(e))
            print("\n\nLet's try again...")

        # The following is a catch-all that will only run if the fatal error is caused by something unknown that we didn't predict
        except:
            print("Invalid input.  The program will close now.")


    print("{} + {} = {}".format(variable1, variable2, variable3))



# Control the program flow
if __name__ == "__main__":
    # Call on the compute function
    compute()



# If used, a "finally:"" line within the try/except block would have run no matter what happens.  For example, to move on to the next step.