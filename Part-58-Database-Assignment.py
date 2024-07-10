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



with connection:
    # Cursor object:
    cursor = connection.cursor()

    # Create a "text file name" table, if one doesn't already exist:
    cursor.execute("CREATE TABLE IF NOT EXISTS text_file_name(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                   fileName TEXT)")
    
    connection.commit()




# Provided tuple of file names:
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Creating a For loop that analyzes that tuple of file names and finds only those that end with ".txt", then splits those names we want into being one-element tuples:
for x in fileList:
    if x.endswith('.txt'):
        with connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO more_people (fName) VALUES (?)", (x,))
            print(x)
        # The values for each row will be one name out of the tuple.  Therefore (x,) will denote a one element tuple for each name ending with y.



# Closing the connection:
connection.close()