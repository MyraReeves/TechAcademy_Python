# Create a class that uses encapsulation. Requirements include:
# 1. This class should make use of a private attribute or function.
# 2. This class should make use of a protected attribute or function.

class BankAccount:
    def __init__(self, account_holder, intitial_balance=0):
        self.account_holder = account_holder

        # Private attribute "balance":
        self.__balance = intitial_balance


    def depositMoney(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"\nSuccessfully deposited ${amount} into your account. \nNew account balance: ${self.__balance}")
        else:
            print("ERROR: Invalid amount!  Can not deposit negative dollars!")


    def withdrawMoney(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"\nWithdrew ${amount} successfully. \nNew account balance: ${self.__balance}")
        else:
            print("ERROR: Insufficient funds!")


    def transferMoney(self, amount, other_account):
        if 0 < amount <= self.__balance:
            self.withdrawMoney(amount)
            other_account.__update_balance(amount)
            print(f"Transfer complete!  Moved the ${amount} to {other_account.account_holder}.")
        else:
            print("ERROR:  Insufficient funds or invalid dollar amount.")
        
    
    # Protected method "Update_balance":
    def __update_balance(self, amount):
        self.__balance += amount



# 3. Create an object that makes use of protected and private.
account1 = BankAccount("Billy Bob Grey", 1000)
account2 = BankAccount("Juliet Grey", 500)


# Using the available functions:
account1.depositMoney(200)
account1.withdrawMoney(500)
account1.transferMoney(300, account2)