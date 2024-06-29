# It is possible to tell Python that an object's real values will be assigned later when an object of the class gets created.
# Object initialization is the act of assigning an object's value before the object is created.  It is done using the __init__() method.

class name:
    def __init__(self, firstName, lastName) -> None:
        #Initializing values for future objects created from this class
        self.firstName=firstName
        self.lastName=lastName
    def printName(self):
        print("Hello, I am {} {}".format(self.firstName, self.lastName))

# Passing in the actual object values:
person = name('Dustin', 'Smith')

# Calling on the function:
person.printName()