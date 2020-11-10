x = set()
# We add to sets with the add() method
x.add(1)
print(x)
'''
Note the curly brackets. This does not indicate a dictionary! Although you can draw analogies as a set being a dictionary with only keys.
We know that a set has only unique entries. So what happens when we try to add something that is already in a set?
'''
# Add a different element
x.add(2)
print(x)
# Try to add the same element
x.add(1)
print(x)

'''
Notice how it won't place another 1 there. That's because a set is only concerned with unique elements! We can cast a list with multiple repeat elements to a set to get the unique elements. For example:
'''
# Create a list with repeats
list1 = [1,1,2,2,3,4,5,6,1,1]
# Cast as set to get unique values
print(set(list1))
