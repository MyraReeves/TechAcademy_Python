#  The following is all that is needed to demonstrate opening a file, writing something new in it, reading the file contents, and then closing it:

import os

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
