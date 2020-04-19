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