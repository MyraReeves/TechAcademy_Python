iteration = 1
brokenLoop = 1
skipFive = 0
elseCounting = 1


# 1. Execute a While loop:
while iteration < 11:
    print(iteration)
    iteration += 1


print("--------------------------")
# 2. Use the "break" statement within a while loop to stop it running despite the while condition still being true:
while brokenLoop < 11:
    print(brokenLoop)
    if brokenLoop == 3: break
    brokenLoop += 1


print("--------------------------")
# 3. Use the "continue" statement within a while loop to skip over an iteration:
while skipFive < 10:
    skipFive += 1
    if skipFive == 5: continue
    print(skipFive)


print("--------------------------")
# 4. Use the "else" statement within a while loop:
while elseCounting < 11:
    print(elseCounting)
    elseCounting += 1
else:
    print("...We have reached the number 10. Counting is done.")
