# Creating the same class, called "User" to act as a blueprint for future objects created from it, as in the previous example, this time we will also pass in all the values for the attributes at the time the object is created.  This is called initialization and requires using the dunder method __init__ to attach the arguments for creating the object to the attributes of that object.

class User:
    # Define the attributes of the class, and assign variables names to each. As part of the definition, it is necessary to give default values to each.  The values can change so long as you provide methods to do so.
    name = "No name provided"
    email = " "
    password = "1234abcd"
    account = 0

    # As in the previous example, here is the definitions of the methods of the class:
    def login(self):
        entry_email = input("Please enter your email address:  ")
        entry_password = input("Enter your passowrd here:  ")
        if (entry_email == self.email and entry_password == self.password): print("Welcome back, {}!".format(self.name))
        else:
            print("Email and password do not match.  Access denied!")
        # Note: For simplicity of the lesson, no security method was used to encrypt the password.  This is NOT how passwords would be handled in a real world use scenario!

    # Then add the following dunder method to the definition of the class:
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account



# Now a new object can be created with a single line of code!  For example:
Newest_user = User("John Doe", "jdoe@example.com", "p@55w0rd", 56428101)
