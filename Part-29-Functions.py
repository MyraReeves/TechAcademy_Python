
# Create a variable:
mySentence = "loves the color"

# Create a list:
colorList = ['red', 'white', 'blue', 'pink', 'purple', 'black', 'green']

# Create a function to show a sentence for each color
def color_function(nameParameter):
    # Create a temporary list and leave it empty:
    tempList = []
    # Iterate thru the color list:
    for i in colorList:
        # Use a variable named "message" and insert three wild cards and format those strings by plugging in the nameParameter, then the mySentence variable, and lastly followed by the iteration:
        message = "{} {} {}".format(nameParameter, mySentence, i)
        # Append each iteration's result into the end of the list to form an array:
        tempList.append(message)
    # After the entire list of colors is finished, end the loop with a "return" command to show the array of resulting sentences:
    return tempList
    

# Call the function with the desired argument name and save the result inside a variable
colorSentences = color_function("Sally")

# Loop thru the array of sentences to print each to the screen. This step is needed so that the result doesn't look like an array.  It is needed so that instead we see only the resulting sentences each one after another.
for i in colorSentences:
    print(i)
