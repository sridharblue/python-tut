'''
List Comprehensions
In addition to sequence operations and list methods, Python includes a more advanced operation called a list comprehension.
List comprehensions allow us to build out lists using a different notation. You can think of it as essentially a one line for loop built inside of brackets. For a simple example:
'''
#Example 1
lst = [x for x in 'word']
print(lst)

# Square numbers in range and turn into list
lst = [x**2 for x in range(0,11)]
print(lst)

mylist1 = [10,20,30,40,100]
mylist2 = []
mylist2 = [i for i in mylist1]
print(mylist2)

celcius = [0,25.5,36,40]
fahrenheit = [((9/5)*temp+32) for temp in celcius]
print(fahrenheit)

num = [x**2 for x in range(0,11) if x%2 ==0]
print(num)

#Example 2
mylis = []

for x in [2,6,8]:
    for y in [1,10,100]:
        mylis.append(x*y)
print(mylis)

mylis11 = [x*y for x in [2,6,8] for y in [1,10,100]]
print(mylis11)


