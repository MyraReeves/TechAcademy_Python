print("\n")

# Assignment:

# 1. Create a class:
class PizzaToppings:
    meat1 = "pepperoni"
    meat2 = "sausage"
    meat3 = "Canadian bacon"
    meat4 = "chicken"
    veggies1 = "artichoke"
    veggies2 = "mushrooms"
    nuts1 = "pine nuts"

# 2. Create an object from that class:
myToppings = PizzaToppings()
print(myToppings.meat4, myToppings.veggies1, myToppings.nuts1)


print("\n")


# 3. Create a new class and assign values to object properties created from that class, using the built-in __init__() function:
class Arachnid:
    def __init__(self, taxonomicOrder, commonName):
        self.order = taxonomicOrder
        self.common = commonName

Emperor = Arachnid("Scorpiones", "emperor scorpion")
print(Emperor.common)
print(Emperor.order)



# 4. Create a method inside a class to be a function that belongs to an object:
class Arachnid:
    def __init__(self, taxonomicOrder, commonName):
        self.order = taxonomicOrder
        self.common = commonName

    def methodFunction(self):
        print("\nA " + self.common + " belongs to the taxonomic Order " + self.order)

# Creation of an object of the Arachnid class:
Harvestman = Arachnid("Opiliones", "daddy longlegs")

# Using that object to call on the method inside of Arachnid:
Harvestman.methodFunction()
