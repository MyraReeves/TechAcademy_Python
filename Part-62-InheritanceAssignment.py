print("\n")
# Create two classes that inherit from another class.  Ensure each child has at least two of their own attributes.

class CannedDrinks:
    def __init__(self, brand, flavor):
        self.brand = brand
        self.flavor = flavor

    def label(self):
        print(self.brand, self.flavor)

class SparklingWater(CannedDrinks):
    def __init__(self, brand, flavor, additive):
        super().__init__(brand, flavor)
        self.sweetener = additive

    def diet(self):
        print("If you are watching your calories, then try a nice, refreshing can of", self.brand, self.flavor, "water, sweetened using", self.sweetener)

# Creating an object from the sparkling water child class
diabetic = SparklingWater("Bonsa", "Blackberry Lime", "aspartame")


# Calling on methods from the objects:
diabetic.diet()