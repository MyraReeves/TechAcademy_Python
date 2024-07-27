# Create a class that uses encapsulation. Requirements include:

# 1. This class should make use of a private attribute or function.
# 2. This class should make use of a protected attribute or function.

class BankAccount:
    def __init__(self, account_holder, intitial_balance=0):
        self.account_holder = account_holder

        # Private attribute:
        self.__balance = intitial_balance


    def depositMoney(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited ${amount} into your account. \nNew account balance: ${self.__balance}")
        else:
            print("ERROR: Invalid amount!  Can not deposit negative dollars!")


    def withdrawMoney(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Please collect your withdrawl of ${amount} cash below. \nNew account balance: ${self.__balance}")
        else:
            print("ERROR: Insufficient funds!")

    
    # Private method:
    def __update_balance(self, amount):
        self.__balance += amount



# 3. Create an object that makes use of protected and private.
