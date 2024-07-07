
# Parent class with default values:
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    DNA = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    # Create a method for this class, passing in the keyword "self" in order to access the attributes:
    def information(self):
        message = "\nName: {} \nSpecies: {} \nNumber of legs: {} \nDNA sequence: {} \nOrigin: {} \nCarbon based? {}".format(self.name, self.species, self.legs, self.DNA, self.origin, self.carbon_based)
        return message
    

# Now we can create a child class instance: