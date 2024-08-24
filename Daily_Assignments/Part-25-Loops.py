
#################
##  For Loop ##
#################

# Initialize i to be zero:
i = 0
# A For Loop will cycle thru the block of code a defined number of times.
# Set that number of times to 10:
for i in range(10):
    # print the wild card value of which iteration it is (which starts at zero) and then remember to set the format of what the wild card is
    print("{} iteration through the loop.".format(i))
    # In shorthand, write i = i + 1, to tell it to add one to it each cycle.
    i += 1





#################
##  While Loop ##
#################

# Initialize i to be zero:
i = 0
# A While Loop will cycle thru the block of code indefinitely until a set parameter has been reached.
# Set that parameter to have a value of 10:
while i < 10:
    # print the wild card value of which iteration it is (which starts at zero) and then remember to set the format of what the wild card is
    print("{} iteration through the loop.".format(i))
    # IMPORTANT:  In order to reach a "False" eventually of i being equal to 10, instruct the code to add one to the value of i each iteration.
    # Use shorthand, write i = i + 1:
    i += 1
# Caution:  While loops have a much greater potential to glitch into becoming an infinite loop!
