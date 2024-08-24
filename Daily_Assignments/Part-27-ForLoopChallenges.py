sequence = ["fox", "coyote", "wolf"]
brokenSequence = ["cup", "saucer", "plate", "fork", "spoon", "knife", "table", "chair"]
skipBanana = ["peach", "papaya", "banana", "plum", "pear"]

# A for loop doesn't need an indexing variable to be set beforehand


# 1. Execute a For loop:
for x in sequence: print(x)

# Iterating thru the characters of a word:
for x in "Gourmet": print(x)


# 2. Use the "break" statement within a for loop to stop it before it loops thru all of the items:
for x in brokenSequence:
    print(x)
    if x == "knife": break


# 3. Use the "continue" statement within a for loop to skip over a specified element:
for x in skipBanana:
    if x == "banana": continue
    print(x)


# 4. Use the range() function within a for loop to return a sequence of numbers, starting at zero and ending at a specified number:
for x in range(20): print(x)    # It will count 20 times, meaning that the displayed numbers will stop at 19.
print("____________________")
# To count between a certain range of numbers, specify which integer to start at followed by which one to stop just before:
for x in range(10, 21): print(x)
print("____________________")
# To count using a different incremental value, specify it as the third parameter:
for x in range(3, 31, 3): print(x)



print("____________________")



# 5. Use the "else" keyword within a for loop to print something once the loop has ended:
for x in range(11): print(x)
else: print("We have now finished counting to 10")
