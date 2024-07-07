
#  In this example, we are creating two children (Employee and Customer) from the class User.  That way both children can inherit tracking of basic attributes like name, email, contact phone, and password, but each child can have attributes and methods unique to itself.  This makes the code as concise as possible.  By avoiding having to retype the things the two children have in common, it saves memory, time, and space in the code.

class User:
    name = 'No name was provided'
    email = ' '
    contact = '555-555-5555'
    password = '12345abcde'

class Employee(User):
    base_pay = 17.00
    department = ' '

class Customer(User):
    account_number = 0
    address = ' '
    mailing_list = True
