# A placeholder doesn't need to be blank inside of the {}.  Instead, they can be identified using word or numbered indexes.

# A 2 decimal format for listing prices can be created using .2f

# Challenge = Execute a format() method to show a price:
salesText = "Buy now for only {price:.2f} dollars!"
print(salesText.format(price = 49))

personIntroduction = "Hello!  My name is {firstname}, and I am {age} years old".format(firstname="Johnny", age=36)
print(personIntroduction)
