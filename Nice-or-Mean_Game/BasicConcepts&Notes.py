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


# ----------------------- Second half of lecture video is below ------------------------

# Create a function that calls on a "get_name" function and prints the result on the screen
def start2():
    print(get_name())


# Create the get_name function
def get_name():
    # Have it inquire from the user what their name is:
    name = input("What is your name?  ")
    # Return to whatever function calls this get_name function whatever that value was that the user entered
    return name


# ------ Alteration to the above:  Format the calling function using wild cards:
def start3():
    print("Hi there, {}!".format(get_name()))



# ----------------------- Third example of basic concepts ------------------------
def terminator():
    first_name = "Sarah"
    last_name = "Connor"
    age = "20"
    occupation = "waitress"
    employer = "Big Jeff's"
    gender = "female"
    # Call on the acquire_target function and pass in the above variables
    acquire_target(first_name, last_name, age, gender, occupation, employer)


# Create the acquire_target function and specify which variables it will need in order to work
def acquire_target(first_name, last_name, age, gender, occupation, employer):
    # Have this function print something to the page:
    print ("Instructions: Assassinate {} {}. Target is a {} year old {} {} at {} diner.".format(first_name, last_name, age, gender, occupation, employer))




# ---------------------- Lastly, for all sections of this video, call the function created in that part of the video ------------------

# Tell Python we are running this as a script
if __name__ == "__main__":
    # and which functions to call, in order
    start()
    start2()
    start3()
    terminator()



# Reminders:  
# "functionName(variable)"" means that we pass in the variable.
# "return variable" means that we are returning the variable back to the calling function.  