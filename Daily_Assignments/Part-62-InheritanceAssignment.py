print("\n")
# Create two classes that inherit from another class.  Ensure each child has their own attributes.

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
        print("If you are watching your calories, then try a nice, refreshing can of", self.brand, self.flavor, "water, sweetened using", self.sweetener, "\n")

class SportsDrink(CannedDrinks):
    def __init__(self, brand, flavor, electrolyte, artificialColoring):
        super().__init__(brand, flavor)
        self.primaryElectrolyte = electrolyte
        self.coloring = artificialColoring

    def replenish(self):
        print("After vomiting, intense heat exposure, or prolonged professional athletics, you should replenish your body's minerals with a bottle of", self.brand, self.flavor + ", full of", self.primaryElectrolyte, "and colored a cheerful shade using", self.coloring, "\n")


# Creating an object from the sparkling water child class
diabetic = SparklingWater("Bonsa", "Blackberry Lime", "aspartame")

# Creating an object from the sports drink child class:
athlete = SportsDrink("Gatorade", "Fruit Punch", "salt", "red dye # 40")

# Calling on methods from the objects:
athlete.replenish()
diabetic.diet()