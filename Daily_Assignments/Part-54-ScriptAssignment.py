# Leveraging OS Interfacing Modules
# to check a specific folder on the hard drive, verify whether any files inside it end with a specific file extension (Example: .txt), and if they do then print those qualifying file names and their corresponding modified time-stamps to the console...


# Import the OS module
import os


# Save the file path to the desired directory within a variable.  Remember to use double \ to communicate a single \
desiredDirectory = 'C:\\Users\\4myra\\OneDrive\\Desktop\\Projects\\DevelopmentArea\\python_projects'


# Use the listdir() method from the OS module to iterate through all files within the directory:
directoryContents = os.listdir(desiredDirectory)


# Viewing that list of all the files to ensure that worked:
print("\n All the files currently inside of the python_projects directory are:")
print(directoryContents)


# Setting up the console message for the next step:
print("\nIn specific, the absolute file paths to all of the TEXT files in the directory are:")

fileName = []

# To narrow it down to only .txt files use a For loop:
textDocuments = []

for file in os.listdir(desiredDirectory):
    if file.endswith(".txt"):
        fileName += [file]
        textDocuments += [os.path.join(desiredDirectory, file)]
        # Use the path.join() method from the OS module to concatenate the file name to its file path, forming an absolute path:
        print(os.path.join(desiredDirectory, file))


# Use the getmtime() method from the OS module to find the latest date that each text file was created or modified:
import time

modification_time = os.path.getmtime(textDocuments[0])
# convert the time in seconds since epoch into local time
local_time = time.ctime(modification_time)
print("\nThe last modification (in your local time) of", fileName[0], "occured at", local_time)

# Shortening it to one line:
local_time2 = time.ctime(os.path.getmtime(textDocuments[1]))
print("\nThe last modification of", fileName[1], "occured at", local_time2, "\n")

# To print to the console a list of each file ending with a ".txt" file extension and its corresponding mtime, use a For loop:
timeStamp = []
# for modifiedTime in os.listdir(desiredDirectory):
#     timeStamp += [time.ctime(os.path.getmtime(directoryContents))]

for x in fileName: print(x, timeStamp)
