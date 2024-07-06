# To create an SQL table database of persons, with their first names, last names, and email addresses...

# Import the SQL module:
import sqlite3

# To view all of the methods that can be used within the sqlite3 module:
print(dir(sqlite3))



# Store a token of the connection to the database within a variable named "connection"
connection = sqlite3.connect('test.db')     # Note: doing this automatically creates a blank database named "test"!


# Until the session is closed, while the connection token is open...
with connection :
    # Invoke a cursor variable to operate on the database when we want to execute commands:
    cursor = connection.cursor()
    # Pass in a multi-line SQL string statement into an execute function to create a table: 
    cursor.execute("CREATE TABLE IF NOT EXISTS table_persons( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    column_firstName TEXT, \
                    column_lastName TEXT, \
                    column_email TEXT )")
                    # The backslashes allow the code instructions to go down a line for better ease of readability
    # Commit these changes to the database
    connection.commit()


# Now that all desired actions are finished, close the database connection:
connection.close()


# __________________________________________________________________________________________________


# To add information to the persons table, establish a connection to the database...

connection = sqlite3.connect('test.db')

# While the connection to the database is open...
with connection:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO table_persons(column_firstName, column_lastName, column_email) VALUES (?, ?, ?)", \
                   ('Bob', 'Smith', 'bobsmith@example.com'))
    cursor.execute("INSERT INTO table_persons(column_firstName, column_lastName, column_email) VALUES (?, ?, ?)", \
                   ('Sarah', 'Jones', 'sarahjones@example.com'))
    cursor.execute("INSERT INTO table_persons(column_firstName, column_lastName, column_email) VALUES (?, ?, ?)", \
                   ('Sally', 'May', 'sallymay@example.com'))
    cursor.execute("INSERT INTO table_persons(column_firstName, column_lastName, column_email) VALUES (?, ?, ?)", \
                   ('Kevin', 'Bacon', 'kevinbacon@example.com'))
    # The ? is a wild card

    # Commit these changes to the database:
    connection.commit()

# Now that all desired actions are finished, close the database connection:
connection.close()


# Note: Ideally, this should have been contained within a function that you can call on


# ___________________________________________________________________________________________________


# To query information from the database table to send it back to us (print to screen) upon request...

connection = sqlite3.connect('test.db')

# While the connection to the database is open...
with connection:
    cursor = connection.cursor()
    cursor.execute("SELECT column_firstName, column_lastName, column_email FROM table_persons WHERE column_firstName = 'Sarah' ")
    
    # Store the info in a variable, that way it won't be lost.  Use fetchall since it is multiple pieces of data in the fixed tuple list
    variablePerson = cursor.fetchall()
    
    # Iterate each piece of information out using a For loop:
    for item in variablePerson:
        displayedInfo = "First Name: {} \nLast Name: {} \nEmail Address: {}".format(item[0], item[1], item[2])
    
    print(displayedInfo)

# Note: Ideally, this should have been contained within a function that you can call on
