
def getInfo():
    variable1 = input("\nPlease provide the first numeric value: ")
    variable2 = input("\nWhat is the numeric value you wish to add to it? ")
    return(variable1, variable2)

def compute():
    go = True
    while go:
        variable1, variable2 = getInfo()

        # Add a try/catch block in case of errors
        try:
            variable3 = int(variable1) + int(variable2)
            go = False

        except ValueError as e:
            print("\n{}: \nYou did not provide a numeric value! Make sure you are entering a number".format(e))
            print("\n\nLet's try again...")
        except:
            print("Invalid input.  The program will close now.")


    print("{} + {} = {}".format(variable1, variable2, variable3))

if __name__ == "__main__":
    compute()