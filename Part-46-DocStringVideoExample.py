"""Multi-line notes can be written
using triple quotation marks, such as
this example here!"""

## Using Alt3 inside of Idle will also comment a line.  It works like hitting control+/ in this VSCode.  The cursor can be anywhere within the line for it to work.
## Inside of Idle, you can UNcomment a line by pressing Alt4



def printMe():
    """This is a docstring. Its purpose is to leave notes for other users of a code to see. For example, if a user needs help understanding your function.
    """
    print("Example of another command inside of the function.  This one is the action the function performs.  It's what will show if you call the function.")


# The docstring comment won't show unless you tell the program specifically to print any docstrings inside of a function using:
print(printMe.__doc__)

# The contents of a docstring can also be revealed when running a Python program by typing the name of the function inside of a help parentheses:
help(printMe)
