# Assignment:  Create a child (derived) class that inherits functionality from a parent (base) class:

class SchoolRoster:
    def __init__(instance, firstName, lastName):
        instance.first = firstName
        instance.last = lastName

    def printName(instance):
        print("\n", instance.first, instance.last)


# The child class Teacher doesn't have any extra properties or methods beyond the ones already in the parent class.  Therefore, it uses the "pass" keyword
class Teacher(SchoolRoster):
    pass


# The child class Student, however, DOES have extra methods
class Student(SchoolRoster):
    def studyingFencing(instance):
        print("-- Fencing student")
    def studyingArt(instance):
        print("-- Art student")
    def studyingSurvival(instance):
        print("-- Outdoor survival skills student")
    def studyingCooking(instance):
        print("-- Culinary student")
    def bardic(instance):
        print("-- Poetry student")


# Creating an object of the Teacher class:
Roster10021 = Teacher("Darren", "Jones")

# Creating an object of the Student class:
Roster31107 = Student("Felicia", "Smith")


# Calling on Roster10021 to show their name:
Roster10021.printName()

# Calling on Roster31107 to show their name:
Roster31107.printName()
# And their areas of study:
Roster31107.studyingFencing()
Roster31107.studyingCooking()