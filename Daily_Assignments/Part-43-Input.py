
# When asking for input, it looks more clean to have the request start on a new line
fName = input("What is your first name? \n")

# To also help the user see the waiting prompt, you can insert a few leading characters, such as >>>>>
lName = input("What is your last name? \n >>>>>")

# Since the values are now stored in variables, they can be used
print("Hello there, {} {}!  Welcome to the program!".format(fName, lName))
