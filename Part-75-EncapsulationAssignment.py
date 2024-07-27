# Create a class that uses encapsulation. Requirements include:

# 1. This class should make use of a private attribute or function:

# Creating a class for student
class Student:
    name = "April Glass"
    __id = 1234567

    # Method for printing the private attribute:
    def printId(self):
        print(f"The id # of this student is: {self.__id}")

Glass = Student()
print(f"The name of this student is: {Glass.name}")

# Accessing the private attribute using getter method:
Glass.printId()

# This class should make use of a protected attribute or function.

# Create an object that makes use of protected and private.

# Add comments throughout your Python explaining your code.

# Upload your code to GitHub.
