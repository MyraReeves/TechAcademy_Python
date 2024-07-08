# Assignment = create two classes that inherit from another class

# The parent should have at least one method function

# Each child should have at least two of their own attributes.

# Both child classes should utilize polymorphism on the parent class method

# ____________________________________________________________________________________________________________________

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

# Calling on the move method they all have:
for x in (Speedracer, MiamiVice, Decommissioned):
    x.move()
