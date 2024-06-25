 # A set is a collection of unordered and unindexed objects encapsulated in curly brackets

exampleSet = {"baseball", "basketball", "football"}

print(exampleSet)

# After creating a set, you cannot change or edit an item.  However, you CAN still add or remove items without having to turn the set into a list first.
# Becasue they are unindexed, you have to explicitly tell the interpreter which item to remove. There is no index for any item.

exampleSet.remove("basketball")

print(exampleSet)