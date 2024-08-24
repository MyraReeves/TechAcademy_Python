# 1. Create a set:
painkillers = {"Acetaminophen", "Ibuprofen", "Naproxen", "Diclofenac topical", "Aspirin"}
# Note that the items will appear in random order when printed, since they are unordered:
print(painkillers)

# 2. Add an item to the set using the add() method:
painkillers.add("Demerol")
print(painkillers)

# 3. Use the remove() method to take an item out of the set:
painkillers.remove("Demerol")
print(painkillers)

# 4. Use the difference() method on two sets to show only the items that exist in the first set and NOT in the second set:
heartattackRisk = {"Ibuprofen", "Diclofenac topical", "Naproxen"}

safestAdultPainkillers = painkillers.difference(heartattackRisk)
print(safestAdultPainkillers)
