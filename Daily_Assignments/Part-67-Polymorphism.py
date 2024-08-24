# Polymorphism allows child classes to keep the same function names as their parents, but modify their functionality.  Essentially, a child class overrides the behavior of its parent class.  Here is an example of a child class that performs the same function as the parent but in a different way...


# Parent Class = User
class User:
    name = "Unknown"
    email = " "
    password = "password"

    def getLoginInformation(self):
        entry_name = input("Please enter your name:  ")
        entry_email = input("Enter the email address associated with your account:  ")
        entry_password = input("Enter password here:  ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else: print("Password or email is incorrect. Access denied!")


# Child Class = Employee
class Employee(User):
    base_pay = 17.00
    department = " "
    pin_number = "00000"

    # The following method uses the same name as in the parent class, however instead of using an entry_password it uses the employee's pin number:
    def getLoginInformation(self):
        entry_name = input("Please enter your name:  ")
        entry_email = input("Enter the email address associated with your employee id:  ")
        entry_pin = input("Enter your employee pin number:  ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("Log-in information incorrect!  Access denied!")



# To instantiate objects and invoke the methods inside each class for a User parent object and a Employee child object:
customer1 = User()
customer1.getLoginInformation()

manager1 = Employee()
manager1.getLoginInformation()