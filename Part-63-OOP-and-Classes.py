# Everything inside of python is considered an object.  Hence it is object oriented programming!


class Game:
    # Add attributes and variables involved in all Game objects:
    variable1 = "Hello"
    variable2 = "there!"





if __name__ == "__main__":
    x = Game()
    print(x.variable1)

    a = Game()
    print("{} {}".format(x.variable1, x.variable2))
