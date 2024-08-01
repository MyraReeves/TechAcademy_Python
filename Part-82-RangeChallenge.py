# Step: 307 = RANGE CHALLENGE

# Complete these actions:

#1. Start IDLE and use the Python range( ) function with one parameter to display the following:
# 0
# 1
# 2
# 3

# This doesn't need to use backwardsList variable because you can simply ask for a range that is a number one beyond the last number you want and Python will start counting at zero.
x = range(4)

for n in x:
  print(n)


# The same would also be true for a different range.  For example, 3 thru 5:
y = range(3, 6)

for n in y:
  print(n)

# ----------------------------------------------------------------------------------


#2. Use the Python range() function with 3 parameters to display the following:
# 3 2 1 0

# One way to accomplish this challenges would be to have the list be backwards.  However, that only uses two parameters and requires a lot of typing:
backwardsList = ['8', '7', '6', '5', '4', '3', '2', '1', '0']

for index in range(5, len(backwardsList)):
  print(backwardsList[index])


# Therefore, to use 3 parameters, use a list that is in the normal default order and specify the need to count by negative one:
QuestionTwo = range(3, -1, -1)          # Note: The range starts counting at 3, ends at the integer just before -1 (which is zero), and counts by -1

for backwards in QuestionTwo:
  print(backwards)


# As another example, for better clarity, if we wanted it to count backwards from 5 and end at the number 1, that would be:
AnotherExample = range(5, 0, -1)
for backwards in AnotherExample:
  print(backwards)


# -------------------------------------------------------------------------------


# Use the Python range( ) function with 3 parameters to display the following:
# 8 6 4 2

# The same basic solution as above can be used -- normal default order and specify the need to count by negative TWO until the number just before the end:

QuestionThree = range(8, 1, -2)
for backwardsByTwo in QuestionThree:
  print(backwardsByTwo)




# HELPFUL LINK:  https://www.w3schools.com/python/ref_func_range.asp

