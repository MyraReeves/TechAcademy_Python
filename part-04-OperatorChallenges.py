x = 5
y = 3


# 1. Use an arithmetic operator:
print("What is x times y?")
print(x*y)


# 2. Use two assignment operators:
print("If we add 3 to x what is the sum?")
x += 3
print(x)

print("If we multiply 3 times y what is product?")
y *= 3
print(y)


print("The values of x and y have now changed to those answers!")

# 3. Use four comparison operators:
print("Is x equal to y?")
print(x == y)

print("Is x NOT equal to y?")
print(x != y)

print("Is the new value of x greater than the new value of y?")
print(x > y)

print("Is x less than or equal to y?")
print(x <= y)


# 4. Use a logical operator:
x = 5
print("Is 5 greater than 3 AND less than 10?")
print(x > 3 and x < 10)


# 5. Use an identity operator:
print("Are x and y the same?")
print(x is y)


# 6. Use a membership operator:
z = ["apple", "grapes", "banana", "cherry"]
print("Does z contain 'banana' within its array?")
print("banana" in z)


# 7. Use two bitwise operators to compare binary numbers:
print("Set each bit to 1 if BOTH bits are 1:")
print(6 & 3)

print("Set each bit to 1 if one of the two bits is 1. Otherwise set it to 0:")
print(6 | 3)
