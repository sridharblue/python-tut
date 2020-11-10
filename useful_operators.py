'''
There are a few built-in functions and "operators" in Python that don't fit well into any category, so we will go over them in this file, let's begin!
'''
#range
#The range function allows you to quickly generate a list of integers

print(range(0, 11))
#Note that this is a generator function, so to actually get a list out of it, we need to cast it to a list with list()

#What is a generator? Its a special type of function that will generate information and not need to save it to memory. 
# Notice how 11 is not included, up to but not including 11, just like slice notation!
print(list(range(0,11)))

# Third parameter is step size!
# step size just means how big of a jump/leap/step you 
# take from the starting number to get to the next number.
print(list(range(0,11,2)))
print(list(range(0,101,10)))

#enumerate
#enumerate is a very useful function to use with for loops.
index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1

# Notice the tuple unpacking!
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))


#zip
#You can use the zip() function to quickly create a list of tuples by "zipping" up together two lists.
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

# This one is also a generator! 
print(zip(mylist1,mylist2))
#let's transform it to a list
print(list(zip(mylist1,mylist2)))

for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))

#in operator
print('x' in ['x','y','z'])
print('x' in [1,2,3])

#not in
print('x' not in ['x','y','z'])
print('x' not in [1,2,3])

#min and max
#Quickly check the minimum or maximum of a list with these functions.
mylist = [10,20,30,40,100]
print(min(mylist))
print(max(mylist))

#random
#Python comes with a built in random library. 
from random import shuffle
# This shuffles the list "in-place" meaning it won't return
# anything, instead it will effect the list passed
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,100))


#input
input('Enter Something into this box: ')


