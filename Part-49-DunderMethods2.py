import Part_49_DunderMethods1

def printApp_Part2():
    name = (__name__)
    return name


if __name__ == "__main__":
    # Call code from within this script file:
    print("First, I am running code from {}".format( printApp_Part2() ) )

    # Call code from the imported module:
    print("And now, instead, I am running code from {}".format( Part_49_DunderMethods1.printApp() ) )
