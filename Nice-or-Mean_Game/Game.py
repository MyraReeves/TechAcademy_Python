#
# Python version: 3.12.2
#
# Authors: Daniel A. Christie, with modifications made by Myra Reeves
#
# Purpose:


# Start the game with all parameters equaling zero as the defaults:
def startGame(nice=0, mean=0, userName=""):
    # Get the user's name from the introduction function and store it in the "userName" variable:
    userName = introduction(userName)
    # Pass in the values of nice, mean, and userName into the "nice_mean" function and store them in their variables
    nice, mean, userName = nice_mean(nice, mean, userName)



def introduction(userName):
    # Check whether it's a new game.  If so, then userName will be a blank string (as per the startGame function) and we need to ask the user to provide their name.
    # If it's not a new game, then we will already have their name saved in the "userName" variable and we can thank them for playing again, and then continue on.
    if userName !="":
        print("\nThank you for playing again, {}!".format(userName))
    else:
        stop = True
        # Create a while loop
        while stop == True:
            if userName == "":
                # Ask the user for their name. Capitalize the first letter of the name they provide:
                userName = input("\nWhat is your name? \n>>>").capitalize()
                if userName != "":
                    print("\nWelcome to the game, {}!".format(userName))
                    print("In this game, you will be greeted by several different people. \nYou can choose to be nice or mean to each of them.")
                    print("Just remember that your fate will be sealed by your choices!")
                    stop = False
                else:
                    userName = input('You didn\'t type anything! Press the "Enter" key to go back and try again...').capitalize()
    return userName



def nice_mean(nice, mean, userName):
    stop = True
    while stop:
        show_score(nice, mean, userName)
        pick = input("\nA stranger approaches you for a \nconversation. Will you greet them nicely\nor be mean? (N or M?) \n>>>:").lower()
        if pick == "n":
            print("\nYou and the stranger have a lovely conversation, and they walk away smiling.")
            nice = (nice+1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \n menacingly and storms off!")
            mean = (mean+1)
            stop = False
    score(nice, mean, userName) # pass the 3 


def score(nice, mean, userName):
    # This score function is being passed the values stored within those 3 variables
    if nice > 2:
        win(nice, mean, userName)
    if mean > 2:
        lose(nice, mean, userName)
    else:
        nice_mean(nice, mean, userName)

def win(nice, mean, userName):
    print("\nGreat job being a good person, {}!")

def again(nice, mean, userName):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (yes)")


if __name__ == "__main__":
    startGame()