# *Args (short for "arguments") is a special syntax used to pass in an undefined number of arguments into a function.  The asterisk represents the unknown number of arguments in tuple form.  This allows a dev to add on to current parameters even if none were defined.

def exampleFunction(*args):
    for arg in args:
        print(arg)

exampleFunction('This is an example of using *args', 'another string', 'and then the integer 5', 5)

