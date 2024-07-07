
# Parent class with default values:
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    DNA = "Sequence A"
    origin_planet = "Unknown"
    carbon_based = True

    # Create a method for this class, passing in the keyword "self" in order to access the attributes:
    def information(self):
        message = "\nName: {} \nSpecies: {} \nNumber of legs: {} \nDNA sequence: {} \nOrigin planet: {} \nCarbon based life-form? {}".format(self.name, self.species, self.legs, self.DNA, self.origin_planet, self.carbon_based)
        return message
    


# _______________________________________________________________________________________________________________
# Now we can create child classes as instances of the parent class.  Here are 3:


class Human(Organism):
    # Attributes can override the defaults:
    name = "MacGyver"
    species = "Homo sapiens"
    legs = 2
    origin_planet = "Earth"
    # this human will inherit both its DNA and carbon_based values from the parent

    def ingenuity(self):
        message = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape. \n"
        return message
    


class Dog(Organism):
    # Attributes overriding the defaults:
    name = "Spot"
    species = "Canis familiaris"
    legs = 4
    DNA = "Sequence B"
    origin_planet = "Earth"
    # This dog will only inherit its carbon_based value from the parent class

    def biteAttack(self):
        message = "\nEmits a loud, menacing growl and bites down ferociously on its target. \n"
        return message
    


class Bacterium(Organism):
    name = "X"
    species ="Vibriodonkus marsis"
    legs = 0
    DNA = "Sequence C"
    origin_planet = "Mars"
    # This bacterium will only inherit its carbon_based value from the parent class

    def replication(self):
        message = "\nThe cells begin to glow, then divide and multiply into two separate organisms. \n"
        return message


# _______________________________________________________________________________________________________________
# Instantiate the child classes to turn them into named objects, calling on all their methods in the process:

if __name__ == "__main__":
    Angus = Human()
    print(Angus.information())
    print(Angus.ingenuity())

    sidekick = Dog()
    print(sidekick.information())
    print(sidekick.biteAttack())

    nemesis = Bacterium()
    print(nemesis.information())
    print(nemesis.replication())
