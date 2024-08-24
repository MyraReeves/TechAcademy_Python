# ABSTRACTION ASSIGNMENT

from abc import ABC, abstractmethod

# Create a class that utilizes the concept of abstraction.  Your class should contain at least one abstract method and one regular method.
class Animal(ABC):
    def identifying(self):
        print("\nI am an animal....")

    def movement(self):
        pass


# Create a child class that defines the implementation of its parents abstract method.
class Dog(Animal):
    def movement(self):
        print("...who can walk and run.")


class Snake(Animal):
    def movement(self):
        print("...and I can only crawl on my belly!")



# Create an object that utilizes both the parent and child methods.
Object1 = Snake()
Object1.identifying()
Object1.movement()

Object2 = Dog()
Object2.identifying()
Object2.movement()
