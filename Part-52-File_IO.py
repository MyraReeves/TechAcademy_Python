
# To see all of the methods associated with the string class:
print(dir(str))

# To open up the built-in help module associated with strings, to see the correct syntax and an explanation of what a method does:
print(help(str))






# ###################################
#           OS Module               #
# ###################################

import os

print(dir(os))

print(help(os))


# To return a unicode string showing the current working directory, use getcwd()
print(os.getcwd())


print(help(open))
# To open a file to read-only it use open() within a with loop, creating a named instance
# In the example below, the instance is called f, and we created a new variable called "data" that read the contents of the file.  The contents were stored inside of the "data" variable.  Hence, we printed the "data" variable to be able to view it.  Then to prevent any memory leaks, we close the file.
with open('C:\Users\4myra\OneDrive\Desktop\Projects\DevelopmentArea\python_projects\SchoolExample.txt', 'r') as f:
    data = f.read()
    print(data)
    f.close()


# To add content to a file, use "append" instead of "write", because "w" would overwrite/truncate the existing file!
data = '\nHello there!'
with open('README.md', 'a') as f:
    f.write(data)
    f.close()


# Those commands can be saved within functions:
def openFile():
    with open('README.md', 'r') as f:
        data = f.read()
        print(data)
        f.close()

def writeData():
    data = '\nHello there!'
    with open('README.md', 'a') as f:
        f.write(data)
        f.close()

if __name__ == "__main__":
    writeData()
    openFile()
