def gen(n):
    for i in range(n):
        yield i

for num in gen(5):
    print(num)


def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in genfibon(10):
    print(num)

def fibon(n):
    a = 1
    b = 1
    output = []
    
    for i in range(n):
        output.append(a)
        a,b = b,a+b
        
    return output

fibon(10)
#if we call some huge value of n (like 100000) the second function will have to keep track of every single result, when in our case we actually only care about the previous result to generate the next one!


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



