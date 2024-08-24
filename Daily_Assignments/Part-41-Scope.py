# Scope can be global or local


name = "Python"     # Global scope (useable anywhere, inside or outside of functions)


def getName():
    name = "C#"     # Local scope (after this function is done running, the "name" variable will go back to having a value of "Python")
    print("I am coding with {}".format(name))


getName()