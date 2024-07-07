# Note that the "self" parameter can be called whatever you want.  It is a reference to the current instance of a class.  It has to be the first parameter of any function in the class.  It is used to access variables that belong to the class.

class Person:
    def __init__(anObjectOfClassPersons, name, age):
        anObjectOfClassPersons.personName = name
        anObjectOfClassPersons.currentAge = age

    def methodFunction(abc):
        print("\nHello there!  My name is " + abc.personName)


# An object of class Person:
person1 = Person("John", 36)

# The object calling on the method inside of the class:
person1.methodFunction()