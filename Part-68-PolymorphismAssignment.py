print("\n")
# Assignment = create two classes that inherit from another class

# The parent should have at least one method function
class Vehicle:
    def __init__(self, brandName, modelName):
        self.brand = brandName
        self.model = modelName

    def movement(self):
        print("Race!")

# Each child should have at least two of their own attributes. The child classes should utilize polymorphism on the parent class method.
class Sportscar(Vehicle):
    pass


class Speedboat(Vehicle):
    Year = " "
    TelevisionShow = " "
    def movement(self):
        print("Accelerate across the water!")


class Fighterjet(Vehicle):
    Flown_by = "Unknown"
    MovieTitle = " "
    def movement(self):
        print("Negative, ghostrider. The pattern is full.")


# A sportcar object:
Richard_Petty = Sportscar("Plymouth", "Superbird")
# A speedboat object:
Undercover = Speedboat("Wellcraft", "Scarab")
# A fighter jet object:
Maverick = Fighterjet("F-14", "Tomcat")


# Using a For loop to call on each of the objects:
for x in (Richard_Petty, Undercover, Maverick):
    print(x.brand, x.model)
    x.movement()


# ____________________________________________________________________________________________________________________
print("\n")


# Example of polymorphism WITHOUT inheritance:
class Car:
    def __init__(self, brandName, modelName):
        self.brand = brandName
        self.model = modelName

    def move(self):
        print("Yeehaw!  Drive on, cowboy!")

class Boat:
    def __init__(self, brandName, modelName):
        self.brand = brandName
        self.model = modelName

    def move(self):
        print("Sail away... Sail, sail away!")

class Airplane:
    def __init__(self, brandName, modelName):
        self.brand = brandName
        self.model = modelName

    def move(self):
        print("Cleared for take-off.  Fly, you fools!")

# Creation of a Car object:
Speedracer = Car("Ford", "Mustang")
# Creation of a Boat object:
MiamiVice = Boat("Ibiza", "Touring 20")
# Creation of a Plane object:
Decommissioned = Airplane("Boeing", "747")

# Uses a For loop to call on the "move" method they all have:
for x in (Speedracer, MiamiVice, Decommissioned):
    x.move()
