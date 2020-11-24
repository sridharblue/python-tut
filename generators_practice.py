def gen(n):
    for i in range(n):
        yield i

for num in gen(5):
    print(num)

#Create a generator that generates the squares of numbers up to some number N
def gensquares(N):
    
    for i in range(N): 
        yield i**2

for x in gensquares(10):
    print(x)

#Create a generator that yields "n" random numbers between a low and high number (that are inputs).
import random
def rand_num(low,high,n):

    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)

#Use the iter() function to convert the string below into an iterator
s = 'hello'
for i in s:
    print(i)
s = iter(s)
next(s)

#Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.
'''
If the output has the potential of taking up a large amount of memory and you only intend to iterate through it, you would want to use a generator.
'''



