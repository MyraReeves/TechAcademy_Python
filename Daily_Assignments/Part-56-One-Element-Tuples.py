# A tuple (immutable sequence of objects) can contain a single object, making it a one-element tuple.  A trailing comma is needed, however, to indicate to Python that it should be treated as a tuple.  Otherwise, if the trailing comma is missing, Python will ignore the parentheses and consider it to be merely a string data type.  The parentheses define a multiple-element tuple, whereas the comma defines a one-element tuple.

oneElementTuple = ('one',)
multiTuple = ('two', 'three', 'four')
addition = oneElementTuple + multiTuple
print(addition)

# Without the trailing comma inside of oneElementTuple, the above would return an error because Python can't concatenate a string with a tuple.