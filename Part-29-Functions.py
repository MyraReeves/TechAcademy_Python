
# Create a variable:
mySentence = "I like the color"

# Create a list:
colorList = ['red', 'white', 'blue', 'pink', 'purple', 'black', 'green']

# Create a function to show a sentence for each color
def color_function():
    # Iterate thru the color list:
    for i in colorList:
        # Insert two wild cards and format those strings by plugging in the mySentence variable followed by the iteration:
        print("{} {}".format(mySentence, i))
    

# Call the function
color_function()
