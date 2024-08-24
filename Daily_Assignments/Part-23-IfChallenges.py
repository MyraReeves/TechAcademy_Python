a = 50
b = 100

x = 35

# 1. Execute an If statement:
if b > a: print(str(b) + " is a larger number than " + str(a) + "!")

# 2. Use the Elif keyword within the if statement:
elif b == a: print("The two numbers are equal")

# 3. Use the Else keyword within the if statement:
else: print(str(a) + " is a larger number than " + str(b))

# 4. Execute a nested If statement:
if x > 10:
    print("The mystery number is larger than 10, ")
    if x > 20:
        print("and it is larger than 20 as well")
    else:
        print("but less than 21")