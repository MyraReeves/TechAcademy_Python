# Note: Python doesn't have built-in support for anything called "Arrays."  Lists need to be used instead.

# 1. Create an array:
recyclables = ['glass', 'cardboard', 'paper', 'aluminum', 'steel']

# 2. Loop through all the elements of the array using a for loop:
for r in recyclables: print(r)

# 3. Use the count() method on the array:
number = len(recyclables)
print(number)

# 4. Use the sort() method on the array:
recyclables.sort()
for alphabetized in recyclables: print(alphabetized)

# Reverse alphabetical order:
recyclables.sort(reverse=True)
for reverseOrder in recyclables: print(reverseOrder)
