# Leveraging OS Interfacing Modules
# to check a specific folder on the hard drive, verify whether any files inside it end with a specific file extension (Example: .txt), and if they do then print those qualifying file names and their corresponding modified time-stamps to the console...


# Import the OS module
import os


# Save the file path to the desired directory within a variable.  Remember to use double \ to communicate a single \
desiredDirectory = 'C:\\Users\\4myra\\OneDrive\\Desktop\\Projects\\DevelopmentArea\\python_projects'


# Use the listdir() method from the OS module to iterate through all files within the directory:
directoryContents = os.listdir(desiredDirectory)


# Viewing that list of all the files to ensure that worked:
print("All the files currently inside of the python_projects directory are:")
print(directoryContents)


# Setting up the console message for the next step:
print("\nIn specific, all of the text files in the directory are:")

# To narrow it down to only .txt files use a For loop:
for file in os.listdir(desiredDirectory):
    if file.endswith(".txt"):
        testing = os.path.join(desiredDirectory, file)
        # Use the path.join() method from the OS module to concatenate the file name to its file path, forming an absolute path:
        print(os.path.join(desiredDirectory, file))


# Use the getmtime() method from the OS module to find the latest date that each text file was created or modified:
import time
modification_time = os.path.getmtime(testing)
# convert the time in seconds since epoch into local time
local_time = time.ctime(modification_time)
print("Last modification time(Local time):", local_time)

# Print to the console a list of each file ending with a ".txt" file extension, and its corresponding mtime:
