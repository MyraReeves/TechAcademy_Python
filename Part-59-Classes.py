
# In this example, we are creating a class called "User" which will act as a blueprint for future objects created from it.

class User:
    # Define the attributes of the class, and assign variables names to each. As part of the definition, it is necessary to give default values to each.  The values can change so long as you provide methods to do so.
    name = "No name provided"
    email = ""
    password = "1234abcd"
    account = 0

    # Define the methods of the class.  This is done like any other function, but they will belong only to this class.  Since the methods will need the elements of the class to operate, use the "self" keyword to pass them into the function.  The "self" keyword represents an isntance of the class (an object of the class), its attributes, and functions.  Call the elements using self.element.
    def login(self):
        entry_email = input("Please enter your email address:  ")
        entry_password = input("Enter your passowrd here:  ")
        if (entry_email == self.email and entry_password == self.password): print("Welcome back, {}!".format(self.name))
        else:
            print("Email and password do not match.  Access denied!")

# Note: For simplicity of the lesson, no security method was used to encrypt the password.  This is NOT how passwords would be handled in a real world use scenario!


# _____________________________________________________________________________________

# Here is the creation of an instance of the User class:
new_user = User()

# The log-in method can be called using the new object that was created:
new_user.login()