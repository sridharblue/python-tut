""" *args and **kwargs 
     *args accepts n number of arguments, parameters, values

"""
##usage 1
def sum(*args):
    s=0
    for i in args:
        s=s+i
    print("result is",s)

sum(11,22,33,44)   
 
##usage 2
def var(*a):
    print(*a)

args=[11,22,33]
var(*args)

""" *kwargs used to pass key,value arguments"""
def keyval(**kwargs):
    print(kwargs)

s={'name':'sri','color':'blue','game':'mlbb'}
keyval(**s)

def keyval(**kwargs):
    for i,j in kwargs.items():
        print(i, ":", j)

s={'name':'sri','color':'blue','game':'mlbb'}
keyval(**s)

#*args
#When a function parameter starts with an asterisk, it allows for an arbitrary number of arguments, and the function takes them in as a tuple of values. Rewriting the above function:

def myfunc(*args):
    return sum(args)*.05

myfunc(40,60,20)

#It is worth noting that the word "args" is itself arbitrary - any word will do so long as it's preceded by an asterisk. To demonstrate this:
def myfunc(*spam):
    return sum(spam)*.05

myfunc(40,60,20)

#**kwargs
#Similarly, Python offers a way to handle arbitrary numbers of keyworded arguments. Instead of creating a tuple of values, **kwargs builds a dictionary of key/value pairs. For example:
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
    else:
        print("I don't like fruit")
        
myfunc(fruit='pineapple')

#*args and **kwargs combined
#You can pass *args and **kwargs into the same function, but *args have to appear before **kwargs
def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass
        
myfunc('eggs','spam',fruit='cherries',juice='orange')

