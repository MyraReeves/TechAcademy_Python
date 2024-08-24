
x = "Good-bye"
y = 45
z = 105

# 1. Run a condition in an if statement:
if z > y: print("The value of z is larger than the value of y")
else: print("The value of z is not greater than y")


# 2. Use the bool() function to evaluate values:
print(bool("Hello"))
print(bool(15))
print(bool(x))
print(bool(y))
# Note: Almost any value evaluates to "True" so long as it has some sort of content. Any string is True, unless empty. Any number is True except for zero.  Any list, tuple, set, or dictionary is True, unless empty.


# 3. Use the isinstance() function to check whether a number is an integer:
w = isinstance(52, int)
print(w)
# Note:  The isinstance() function will return True if the specified object is of the specified type.
# Also, if the type parameter is a tuple, then the function will return True so long as the object is one of the types in the tuple:
v = isinstance("Hello", (str, float, int, str, list, dict))
print(v)
