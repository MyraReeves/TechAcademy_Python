# Encapsulation is implemented by creating a protected (non-public) or private method or property.  The purpose is to restrict access from functions and variables from being directly changed or modified by accident within a Class.

# Protected is denoted with a single underscore prefix.  It doesn't change anything; instead, it acts more as a warning to other developers, basically stating that it is protected and shouldn't be used outside of its Class.
class Protected1:
    def __init__(self):
        self._protectedVar = 0

protected_object = Protected1()
protected_object._protectedVar = 34
print(protected_object._protectedVar)


# Private is denoted with a double underscore prefix.  It's harder to access, but it can still be done.  It takes a bit more coding, but this ensures that private can not be changed unless it is on purpose.
class Protected2:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivte(self, private):
        self.__privateVar = private

obj = Protected2()
obj.getPrivate()
obj.setPrivte(23)
obj.getPrivate()