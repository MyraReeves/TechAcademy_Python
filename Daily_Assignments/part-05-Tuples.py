# Tuples use parentheses and are immutable objects that cannot be changed
animal = ('zebra', 'alligator', 'giraffe', 'goat', 'ox')
print(animal)

# Lists, however, CAN be changed
listOfAnimals = list(animal)
print(listOfAnimals)
listOfAnimals.append("honey badger")
print(listOfAnimals)

# Strings are also considered immutable objects that cannot be changed
myString = "Hello!  Pleased to meet you!"

# Therefore, attempting to create a list with one would create an array where every character and empty space is its own element!
newString = list(myString)
print(newString)

# So, to split the array apart into separate words, use the split method and pass in an empty space as the condition
corrected_New_String = myString.split(" ")
print(corrected_New_String)