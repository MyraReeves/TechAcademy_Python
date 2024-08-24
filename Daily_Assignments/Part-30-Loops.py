
# Create a variable:
loopingSentence = "loves the color"

# Create a list:
colors = ['red', 'white', 'blue', 'pink', 'purple', 'black', 'green']

# Create a function to show a sentence for each color
def colorSententence_function(nameParameter):
    # Create a temporary list and leave it empty:
    tempList = []
    # Iterate thru the color list:
    for i in colors:
        # Use a variable named "message" and insert three wild cards and format those strings by plugging in the nameParameter, then the loopingSentence variable, and lastly followed by the iteration:
        message = "{} {} {}".format(nameParameter, loopingSentence, i)
        # Append each iteration's result into the end of the list to form an array:
        tempList.append(message)
    # After the entire list of colors is finished, end the loop with a "return" command to show the array of resulting sentences:
    return tempList
    

# Create a function to get the user's name and then loop it thru all the sentences:
def getName_function():
    go = True
    while go: 
        userName = input('What is your name? ')
        if userName == "": print("Please provide a name")
        elif userName == 'Myra': print("That name is not allowed. Sorry!")
        else: go = False
    resultingSentence = colorSententence_function(userName)
    for i in resultingSentence: print(i)

# Call the function
getName_function()
