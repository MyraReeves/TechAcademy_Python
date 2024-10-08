# 1. Assign a string to a variable:
string1 = "Hi there!"
print(string1)



# 2. Assign a multiline string to a variable:
string2 = """Ryan1 says: And then after this guy takes down the henchman,
I'll bust in, do a back flip, snap the bad guy's neck and save the day!

Ryan2: So wait, let me get this straight,
You want us to go thru all that trouble
...go thru all of that...
on the slight chance that it might work?

Ryan1:  That's it.  That's the plan.

Ryan2:  Alright.  I'm in.

Ryan1:  You son of a gun.
"""
print(string2)




# 3. Return a range of characters by using the slice syntax:
print("""
__________________________________
Four examples of using the slice method:
__________________________________""")
# First, it can be done by specifying the start index and the end index, separated by a colon. Note that the first character has an index of zero:
print(string2[340:347]) 

# Second, by leaving out the start index. This way, the range will start at the first character and end wherever you specify:
print(string1[:2])

# Third, if you leave out the ending index, then the range will go all the way to the end:
print(string2[330:]) 

# The fourth way would be using negative indexes to start counting the slice from the end of the string:
print(string2[-18:-1])




# 4. Use the len() function:
print("""
      
__________________________________________________________
The total number of characters in the string2 variable is:
__________________________________________________________""")
print(len(string2))




# 5. Use the strip() method to return a trimmed version of a string.
print("""
      
__________________________________
Two examples of using the strip method:
__________________________________""")
Ryan4 = "     Well if he's in, I'm in.                 "
stripped = Ryan4.strip( )
print('Ryan3: "I\'m in, too."  Ryan4: "' + stripped + '"')
# Note that leaving it blank only works for leading/trailing white space, NOT for white space that's in the middle of a string

# Leading/trailing letters can be specified, however:
exampleStripped = ".,,,...jkkkjbanana...jjj"
strippedExample = exampleStripped.strip(",.jk")
print(exampleStripped + " gets stripped down to become " + strippedExample)




# 6. Use the upper() method to convert a string into all uppercase letters:
Ryan5 = '"If he\'s in, I\'m out!"'
print("""
      
__________________________________
Example of using the upper method:
__________________________________""")
allCaps = Ryan5.upper()
print(allCaps)




# 7. Use the "in" or "not" in keyword to check whether or not a particular phrase or character is present in a string:
print("""
      
___________________________________________________________________
Checking whether the word 'henchman' is within the string2 variable:
___________________________________________________________________""")

print("henchman" in string2)

# ----------------------------------

print("""
      
___________________________________________________________________
Print confirmation only if the word 'henchman' is within the string2 variable:
___________________________________________________________________""")

if "henchman" in string2: print("Yes, Ryan mentioned a henchman when describing the plan")

# ----------------------------------

print("""
      
_______________________________________________________________
Check whether the word 'out' is NOT within the string2 variable:
_______________________________________________________________""")

print("out" not in string2)

# ----------------------------------

print("""
      
____________________________________________________________________________
Print confirmation only if the word 'out' is NOT within the string2 variable:
____________________________________________________________________________""")

if "out" not in string2: print("At the beginning, all of the Ryans said they were in. In the string2 variable, none said that they were out.")




# 8. Concatenate a string:
print("""
      
_____________________
Concatenating strings:
_____________________""")
string3 = "Hello!"
print(string1 + " " + string3)
RyanGreeting = '"' + string1 + ' '  + string3 +'"'
print(RyanGreeting)




# 9. Use an escape character:
print("""
      
________________________
About escape characters:
________________________""")
print("✅ See lines 66 and 78 of the code for this page to see examples of using the \ escape character")
