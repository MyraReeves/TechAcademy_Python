# 1. Create a list:
plumTrees = ["satsuma", "santa rosa", "black beauty", "friar"]
print(plumTrees)

# 2. Loop through the list using a "for" loop:
for x in plumTrees: print(x)

# 3. Use the append() method:
plumTrees.append("victoria")
print(plumTrees)

# 4. Make a copy of the list.  For example, use the List method copy():
secondCopy = plumTrees.copy()
print(secondCopy)

# 5. Concatenate two lists:
appleTrees = ["anna", "braeburn", "cortland", "fuji"]

fruitTrees = plumTrees + appleTrees
print(fruitTrees)

# 6.  Use the reverse() method on a list:
appleTrees.reverse()
print(appleTrees)