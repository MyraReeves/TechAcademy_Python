
def getInfo():
    variable1 = input("Please provide the first numeric value: ")
    variable2 = input("What is the numeric value you wish to add to it? ")
    compute(variable1, variable2)

def compute(variable1, variable2):
    go = True
    while go:
        getInfo()

        # Add a try/catch block in case of errors
        try:
            variable3 = int(variable1) + int(variable2)
            print("{} + {} = {}".format(variable1, variable2, variable3))

        except ValueError as e:
            print("{}: \nYou did not provide a numeric value! Make sure you are entering a number".format(e))
        except:
            print("Invalid input.  The program will close now.")
        finally:
            print("Moving on...")


if __name__ == "__main__":
    getInfo()