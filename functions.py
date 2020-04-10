def fun1(start,end):
    if(start>end):
        print("start is greater than end")
        return 

    results=0
    for i in range(start,end+1):
        results=results+i
    return results

a=fun1(11,55)
print(a)

""" global and local variable """

var=10
def fun():
    ##var=100
    global var
    var=20
    print(var)

fun()
print(var)

""" arguments with default values """

def fun(x,y=100):
    print(x,y)

fun(10,20)

""" positional and keyword arguments """

def func(q,w):
    print(q,w)

func("hi","sridhar") ##positional
func(w="sridhar",q="hi") ##keyword

###POSITIONAL ARGUMENTS MUST APPEAR BEFORE KEYWORD ARGUMENTS

""" return multiple values """
def mul(a,b,c):
    return a,b,c

s=mul(11,22,33)
print(s)
print(type(s))


