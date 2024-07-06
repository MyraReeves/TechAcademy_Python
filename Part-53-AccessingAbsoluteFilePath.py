# Leveraging OS Interfacing Modules
# to be able to give an absolute path in Python...


# Import the OS module:
import os
# Information about what methods can be done within this module is at docs.python.org


# Give the desired file name as a string, and store it in a variable:
fName = "Demo_NewFile.txt"


# Give the file path to that file, as a string, and store it in a variable:
fPath = 'C:\\Users\\4myra\\OneDrive\\Desktop\\Projects\\DevelopmentArea\\python_projects\\'
# Remember that the \ is an escape character. Therefore, an extra one is needed in front of each in order for the software to read it as the \ symbol


# To concatenate the file name to the file path to produce an absolute file path, invoke the path.join() method from the os module:
absolutePath = os.path.join(fPath, fName)
# It is saved in a variable so that it can be called on below


# View the absolute file path:
print(absolutePath)
