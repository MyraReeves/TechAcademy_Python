# Dictionaries are a specialized type of list.
# The first item is a key; the second item is its value. dictionary={"key":"value"}  Together they form a key-value pair. A dictionary is an UNordered collection of key-value pairs.

myDictionary = {'index1':1, 'index2':2, 'index3':355}
print(myDictionary)

# To get only the value associated with one key:
print(myDictionary['index3'])



# You can nest a dictionary inside of another dictionary!
dictionaryUsers = {"employee1234":{"fName":"Bob", "lName":"Barker", "phone":"123-456-7890"}, "employee12345":{"fName":"Mary", "lName":"McKraken", "phone":"987-654-3210"}, "employee123456":{"fName":"Sam", "lName":"Smith", "phone":"555-111-2222"}  }

# To call on the second item in the dictionary:
print(dictionaryUsers["employee12345"])

# To pull out only one element, such as the phone number of the desired employee:
print(dictionaryUsers["employee12345"]["phone"])

# Use {} wild cards for the first and last names, 
# then use the \n to go down one line, 
# then use a {} wild card for the phone number,
# then use the format() method with the necessary variables listed:
print( "User: {} {} \nPhone: {}".format(dictionaryUsers["employee12345"]["fName"], dictionaryUsers["employee12345"]["lName"], dictionaryUsers["employee12345"]["phone"]) )
