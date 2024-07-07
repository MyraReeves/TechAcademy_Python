
import sqlite3
connection = sqlite3.connect(test.db)
with connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS more_people(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                   fName TEXT)")
    connection.commit()

connection = sqlite3.connect('test.db')

# Tuple of names:
persons_tuple = ('Kelly', 'Sally', 'Kevin', 'Adam')

# To add only the names that end with "y" to the database...
# Create a For loop that analyzes the tuple of names and finds only those that end with "y", then splits the names we want into one-element tuples:

for x
