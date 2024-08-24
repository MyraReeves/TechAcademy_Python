# **Kwargs is special syntax that is short for "keyword arguments" and is used to pass in an unknown number of undefined arguments into a function.  The double astrisks represent a key value pair.  This allows it to act as a dictionary, mapping out the value to its corresponding variable key.  Sometimes, devs refer to it as **args instead.

def myFunction(**kwargs):
    print("Here are the kwargs: ", kwargs)

myFunction(first = '1', second = '2', third = '3')
