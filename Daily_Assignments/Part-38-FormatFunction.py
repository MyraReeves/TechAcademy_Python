# The format() function can do more than just format strings!  It can also convert a value into a specific data type format.  Plus, it can also format values into binary or into floats.

# To do so, the format() function takes 2 parameters -- the values that need to be formatted and the format specification


# To format a number into binary:
binaryExample = format(8, 'b')
print(binaryExample)

# To format a number into hexadecimal:
hexadecimalExample = format(4, 'x')
print(hexadecimalExample)

# To format a number into percentage:
percentageExample = format(1, '%')
print(percentageExample)

# Formatting a value into different data types, written out in string format concatenation:
print("Here is the number 3 written as... binary: {0:b}, hexadecimal: {0:x}, percentage: {0:%}".format(3))