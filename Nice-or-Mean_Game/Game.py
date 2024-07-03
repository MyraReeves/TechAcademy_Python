#
# Python version: 3.12.2
#
# Authors: Daniel A. Christie, with modifications made by Myra Reeves
#
# Purpose:  School assignment to demonstrate passign variables from function to function, while coding a functional game.



# Start the game with all parameters equaling zero as the defaults:
def startGame(nice = 0, mean = 0, userName=""):
    # Get the user's name from the introduction function and store it in the "userName" variable:
    userName = introduction(userName)
    # Pass in the values of nice, mean, and userName into the "nice_mean" function and store them in their variables
    nice, mean, userName = nice_mean(nice, mean, userName)



def introduction(userName):
    # Check whether it's a new game.  If so, then userName will be a blank string (as per the startGame function) and we need to ask the user to provide their name.
    # If it's not a new game, then we will already have their name saved in the "userName" variable and we can thank them for playing again, and then continue on.
    if userName !="":
        print("\nAll set!  Thank you for playing again, {}!".format(userName))
    else:
        stop = True
        # Create a while loop
        while stop == True:
            if userName == "":
                # Ask the user for their name. Capitalize the first letter of the name they provide:
                userName = input("\nWhat is your name? \n>>> ").capitalize()
                if userName != "":
                    print("\nWelcome to the game, {}!".format(userName))
                    print("In this game, you will be greeted by several different people. \nYou can choose to be nice or mean to each of them.")
                    print("Just remember that your fate will be sealed by your choices!")
                    stop = False
                else:
                    userName = input('You didn\'t type anything! Press the "Enter" key to go back and try again...').capitalize()
    return userName


# Obtain the values of nice, mean, and userName from the startGame function and pass them into this function:
def nice_mean(nice, mean, userName):
    stop = True
    while stop:
        # Call the show_score function and pass into it the current values of nice, mean, and userName
        show_score(nice, mean, userName)
        # Now change that score by asking the user to make a choice:
        pick = input("\nA stranger approaches you for a conversation. \nWill you treat them nicely or be mean to them? \n(To choose, type either the word 'Nice' or the word 'Mean') \n>>>").lower()
        if pick == "nice":
            print("\n😇 You and the stranger have a lovely conversation, and they walk away smiling.")
            nice = (nice+1)
            stop = False
        if pick == "mean":
            print ("\nThe stranger glares at you menacingly and storms off! 👿")
            mean = (mean+1)
            stop = False
    score(nice, mean, userName) # pass the values of nice, mean, and the userName into the score function


# Obtain the values of nice, mean, and userName and pass them into this function
def show_score(nice, mean, userName):
    print("\nYour current score is: \n {} beauty points, {} ugliness points".format(nice, mean))



# Obtain the values of nice, mean, and userName from the nice_mean function and pass them into this function
def score(nice, mean, userName):

    if mean > 3:
        # Call the lose function and pass in the 3 variables:
        lose(nice, mean, userName)
    
    if nice > 3:
        # Call the win function and pass in the 3 variables:
        win(nice, mean, userName)
    
    else:
        # Continue asking the user to make new choices so that the score changes, being sure to pass in the current values:
        nice_mean(nice, mean, userName)


# Receive the current values of nice, mean, and userName
def lose(nice, mean, userName):
    print("Oh no, {}! 🫣 \nYour mean-spirited choices have left you jobless, wretched, and alone! The game ends as you cry yourself to sleep on a dirty piece of cardboard, homeless down by the river. 😞".format(userName))
    # Ask whether the user wants to play the game again.  Be sure to pass off the current variable values.
    playAgain(nice, mean, userName)


# Receive the current values of nice, mean, and userName
def win(nice, mean, userName):
    print("\n🎉 Great job being a good person, {}! 🎉 \nThe game has ended after you've made so many new friends that you win the local popularity contest! \n🏆".format(userName))
    # Ask whether the user wants to play the game again.  Be sure to pass off the current variable values.
    playAgain(nice, mean, userName)


def playAgain(nice, mean, userName):
    stop = True
    while stop == True:
        choice = input('\nDo you want to play again? (Answer with either "Yes" or "No"): \n>>> ').lower()
        if choice == "yes":
            print("\n✔️ \tHuzzah! I'll zero out your scores and start the game from fresh for you!")
            stop = False
            # Call on the reset function, passing into it the values of the 3 variables
            reset(nice, mean, userName)
        if choice == "no":
            print("\n❌ \t So sad to see you go. Bye, {} 👋".format(userName))
            stop = False
            quit()
        else:
            print("Please answer with either the word YES or the word NO")


# This reset function only needs to reset the score values, since the user has remained the same
def reset(nice, mean, userName):
    nice = 0
    mean = 0
    # Call on the startGame function, passing into it these three existing values:
    startGame(nice, mean, userName)


if __name__ == "__main__":
    startGame()