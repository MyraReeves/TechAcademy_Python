# As of Python version 3.7, dictionaries are ordered.  However, previously (in Python 3.6 and earlier) dictionaries were unordered.


# 1. Create a dictionary:
pickupTruck = {
    "make":"Ford",
    "model":"Ranger",
    "year":1991,
    "color":"white"
}

# Viewable using:
print(pickupTruck)


# 2. use the get() method on the dictionary to return the value of an item with a specified key:
model = pickupTruck.get("model")
print(model)


# 3. Change a value within the dictionary by referring to its key name:
pickupTruck["color"] = "blue"
print(pickupTruck)


# 4. Add an item to the dictionary by using a new index key and assigning a value to it:
pickupTruck["transmission"] = "manual"
print(pickupTruck)


# 5. Create a nested dictionary:
BlueyFamily = {
    "Mum": {
        "name":"Chilli",
        "breed":"red heeler",
        "voiced by":"Melanie Zanetti"
    },
    "Dad": {
        "name":"Bandit",
        "breed":"blue heeler",
        "voiced by":"Dave McCormack"
    },
    "eldest": {
        "name":"Bluey Christine",
        "breed":"Blue Heeler",
        "age":6
    },
    "youngest":{
        "name":"Bingo",
        "breed":"Red Heeler",
        "age":4
    }
}


print(BlueyFamily)


# 6. Use the fromkeys() method to create a dictionary with the specified keys and one specified value:
x = ("color1", "color2", "color3")
y = "red"

combinedDictionary = dict.fromkeys(x,y)

print(combinedDictionary)