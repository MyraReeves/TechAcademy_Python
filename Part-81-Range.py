# PYTHON RANGE() FUNCTION

# The Python range( ) function generates a list of numbers, which is generally used to iterate over with for loops. In other words, using it creates the list of index numbers that you can then use in a for loop.  The range( ) function has two different sets of parameters that can be used as follows:

# range(stop)
# stop: The number of integers to generate, starting from zero.

# range([start], stop[, step])
# Notice how the optional parameters are enclosed in [ ]
# start: The starting number of the sequence.
# stop: The number specifying where the sequence will stop. This is not inclusive (meaning, it doesn't include the number specified).
# step: The difference between each number in the sequence. This is basically the ‘count by’ number.

# Note that:
# All parameters must be integers.
# All parameters can be positive or negative.
# The stop parameter is not the number the function will stop on. It specifies that it will stop before the sequence reaches this number.

# EXAMPLE:
myList = ['one', 'two', 'three', 'four', 'five']

myList_length = len(myList)
# MyList_length = 5

for i in range(0, myList_length):
    # The range above goes from index 0 thru index 4 of the five item long list

    print(myList[i])
    # Therefore, the above will print the values of index 0 thru index 4 (because that is the range).