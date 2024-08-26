# STEP 305 = Complete these actions:

# STEP 1: Create a database table in RAM named Roster that includes the fields ‘Name’, ‘Species’ and ‘IQ.’

# Imports the SQL module:
import sqlite3

# Storing a token of the connection to a database named "Roster" within a variable named "connection" will automatically create a blank database named "Roster":
connection = sqlite3.connect('Part80_Roster.db')

# Until the session is closed, while the connection token is open...
with connection :

    # Invokes a cursor variable to operate on the database when we want to execute commands:
    cursor = connection.cursor()
    
    # Passes in a multi-line SQL string statement into an execute function to create a table named "Roster" within the database, and adds the requested column names: 
    cursor.execute("CREATE TABLE IF NOT EXISTS Roster( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    Name TEXT, \
                    Species TEXT, \
                    IQ INTEGER )")
                    # The backslashes allow the code instructions to go down a line for better ease of readability
                    
    # Commit these changes to the database
    connection.commit()

# Now that all desired actions are finished, close the database connection:
connection.close()


# ---------------------------------------------------------------------------------------------------
# STEP 2: Populate your new table with the following values:
# 1 Jean-Baptiste, Zorg, Human, 122
# 2 Korben Dallas, Meat Popsicle, 100
# 3 Ak'not, Mangalore, -5

# To add information to the table, establish a connection to the database...
connection = sqlite3.connect('Part80_Roster.db')

# While the connection to the database is open...
with connection:

    # Invokes a cursor variable to operate on the database when we want to execute commands:
    cursor = connection.cursor()

    # Uses the INSERT INTO SQL statement to insert new records in a table:
    cursor.execute("INSERT INTO Roster(Name, Species, IQ) VALUES ('Jean-Baptiste Zorg', 'Human', '122')")
    cursor.execute("INSERT INTO Roster(Name, Species, IQ) VALUES ('Korben Dallas', 'Meat Popsicle', '100')")
    cursor.execute("INSERT INTO Roster(Name, Species, IQ) VALUES ('Ak''not', 'Mangalore', '-5')")

    # Commit these changes to the database:
    connection.commit()

# Now that all desired actions are finished, close the database connection:
connection.close()

# ---------------------------------------------------------------------------------------------------
# STEP 3: Update the Species of Korben Dallas to be Human.


# STEP 4: Display the names and IQs of everyone in the table who is classified as Human.


# HELPFUL LINK:  https://www.sqlitetutorial.net/sqlite-python/creating-database/