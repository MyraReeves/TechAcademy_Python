# Data abstraction hides the complex details of items while only revealing te essential or relevant data.  It hides the complex functionality through the use of creating abstract methods.  They are defined, but most of the time do not really contain any implementation.

# When a class contains more than one abstract method, it is called an abstract class.  The implementation of the abstract class is defined by a subclass like a child class or a third party plug in.  Abstraction is useful for working on much larger projects when child classes may need to utilize implementation of methods differently from their parent class and other child classes that inherit from the same parent.


# Import the Abstract Base Class (ABC) from the abc module, as well as the abstractmethod:
from abc import ABC, abstractmethod

class card(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
    # Pass in an argument of unspecified data in an unspecified way
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(card):
    # This defines how to implement the payment function from its parent paySlip class.
    def payment(self, amount):
        print("Your purchase amount of {} exceeded your $100 limit ".format(amount))


obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")

# You have one parent class of payment.  Child classes need to run different payment options separately from each other, such as Debit, Credit, Gift card, etc.  They all take a payment from the customer, but each process needs to be different according to how the banks process them.