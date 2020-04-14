""" Constructor"""

# class myclass():
#     def fun(self):
#         print("this is class method")
#     def __init__(self):
#         print("this is class constructor")

# mc=myclass()
# mc.fun()

"""convert local to class variables"""

class myclass():
    def fun(self,a,b):
        print(a,b)
        self.a=a
        self.b=b

    def add(self):
        print(self.a+self.b)

mc=myclass()
mc.fun(10,20)
mc.add()

""" using constructor"""
class myclass():
    def __init__(self,a,b):
        print(a,b)
        self.a=a
        self.b=b

    def add(self):
        print(self.a+self.b)

mc=myclass(100,200)
mc.add()


""" calling a method from another method of same class"""
class myclass():
    def m1(self):
        print("this is m1 method")
        self.m2("called from m1")

    def m2(self,a):
         print("this is m2 method", a)

mc=myclass()
mc.m1()

"""CONSTRUCTORS WITH ARGUMENTS"""

class myclass():
    a=222
    def __init__(self,a): ##accessing local variables
        print(a)
        print(self.a) ##accessing class variables

mc=myclass(100)

""" TEST """

class Emp():
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
        self.Display()

    def Display(self):
        print("EmpID:{},EmpNAme:{},EmpSal:{}".format(self.eid,self.ename,self.sal))
        print("EmpID:%d,EmpName:%s,EmpSal:%g" %(self.eid,self.ename,self.sal))

mc=Emp(1,"sridhar",10000)

""" __str__ method """

class myclass():
    pass

c=myclass() ## c is the reference variable
print(c) ## printing ref variable will call __str__() method, ## which will return obj memory location

""" __str__ override"""

class myclass():
    def __str__(self):
        return "HELLO" ##MUST RETURN ONLY STRING TYPE

c=myclass()
print(c) ##we overrided default __str__() method by defining our own __str__() method

""" ex for __str__"""

class Emp():
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal

    def __str__(self):
        return "EmpID:{},EmpNAme:{},EmpSal:{}".format(self.eid,self.ename,self.sal)
        ##return ("EmpID:%d,EmpName:%s,EmpSal:%g" %(self.eid,self.ename,self.sal))

mc=Emp(1,"sridhar",10000)
print(mc)

"""__del__() method """

class myclass():
    def __del__(self):
        print("hello")

c=myclass()
c1=myclass()

del c,c1 ## del function executes when we destroy an object







 


   
