
# User capitalization unpredictability can be compensated for by normalizing the data using the lower() method to change all the inputted characters into lowercase, or by using the upper() method to change them all to uppercase letters:

def getName():
    First_name = input("Please type your first name without any capitalization. \n>>>>>").lower()
    print ("Thank you {}!  Welcome back!".format(First_name))
    Last_name = input("What is your last name? \n>>>>>>").upper()
    print ("{} is a great last name to have!".format(Last_name))

getName()

#  Note:  The casefold() method is an even stronger, more aggressive means of converting all characters into lowercase.  It will find more matches when comparing two strings when both are converted using the casefold() method.



# For names, it is also helpful to convert only the first letter to uppercase.  Use the capitalize() method to do so.
def capitalizeFirstLetterOnly():
    First = input("What is your first name? \n>>>>").capitalize()
    Last = input("What is your last name, {}? \n>>>>".format(First)).capitalize()
    print ("Hello there, {} {}!  Pleased to meet you!".format(First, Last))

capitalizeFirstLetterOnly()