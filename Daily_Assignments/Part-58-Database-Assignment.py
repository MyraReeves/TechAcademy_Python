# Using Python and the SQLite3 module, write a script that creates a database and adds new data into that database

# Requirements = 
# Include in the database 2 fields - an autoincrement primary integer field and a "string" field
# Read from the supplied list of files names and determine only the names that end in a "txt" file extension
# The provided folder and files do NOT need to be saved on your computer
# The script should add the found txt file names to the database
# The list of qualifying text file names should be printed to the console
# --------------------------------------------------------------------------------------------------


# Connecting to sqlite:
import sqlite3



# Creates a blank database named "Step223_Assignment" by storing a token of the connection to the database within a variable named "connection":
connection = sqlite3.connect('Step223_Assignment.db')



# Until the session is closed, while the connection token is open...
with connection:

    #  # Invoke a cursor variable to operate on the database when we want to execute commands:
    cursor = connection.cursor()

    # Create a "text file name" table, if one doesn't already exist:
    cursor.execute("CREATE TABLE IF NOT EXISTS text_file_name(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    column_fileName TEXT)")
    
    # Commit these changes to the database
    connection.commit()



# Provided tuple of file names:
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Creating a For loop that analyzes that tuple of file names and finds only those that end with ".txt", then splits those names we want into being one-element tuples:
for x in fileList:
    if x.endswith('txt'):
        with connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO text_file_name (column_fileName) VALUES (?)", (x,))
                    # The values for each row will be one file name out of the tuple.  Therefore (x,) will denote a one element tuple for each file name ending with .txt
            print(x)



# Closing the connection:
connection.close()
