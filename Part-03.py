num1 = "one"
num2 = 2.1

# print(num1 + num2)
# Will result in an error saying that you can't concatenate a string to a floating point number

num1 = "1"
print( int(num1) + num2 )
# Will work to produce 3.1 because we converted num1 from a string into an integer
