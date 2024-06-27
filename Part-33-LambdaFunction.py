def multiply(i):
    return i * i;

print(multiply(3))


# The lambda keyword is used as an anonymous function.  That is a single-line function that has no name and can have any number of arguments but only one expression.  It is used for a shorter amount of time than a regular function, and is used when you want to pass another function in as an argument.
y = lambda x: x * x * x

print(y(20))
