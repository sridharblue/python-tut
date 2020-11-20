""" Constructor"""
#Constructor will always run first
class myclass():
    def fun(self):
        print("this is class method")
    def __init__(self):
        print("this is class constructor")

mc=myclass()
mc.fun()

"""convert local to class variables"""

class myclass7():
    def fun(self,a,b):
        print(a,b)
        self.a=a
        self.b=b

    def add(self):
        print(self.a+self.b)

mc=myclass7()
mc.fun(10,20)
mc.add()

""" using constructor"""
class myclass1():
    def __init__(self,a,b):
        print(a,b)
        self.a=a
        self.b=b

    def add(self):
        print(self.a+self.b)

mc1=myclass1(100,200)
mc1.add()


""" calling a method from another method of same class"""
class myclass2():
    def m1(self):
        print("this is m1 method")
        self.m2("called from m1")

    def m2(self,a):
         print("this is m2 method", a)

mc2=myclass2()
mc2.m1()

"""CONSTRUCTORS WITH ARGUMENTS"""

class myclass3():
    a=222
    def __init__(self,a): ##accessing local variables
        print(a)
        print(self.a) ##accessing class variables

mc=myclass3(100)

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

class myclass4():
    pass

c=myclass4() ## c is the reference variable
print(c) ## printing ref variable will call __str__() method, ## which will return obj memory location

""" __str__ override"""

class myclass5():
    def __str__(self):
        return "HELLO" ##MUST RETURN ONLY STRING TYPE

c=myclass5()
print(c) ##we overrided default __str__() method by defining our own __str__() method

""" ex for __str__"""

class Emp1():
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal

    def __str__(self):
        return "EmpID:{},EmpNAme:{},EmpSal:{}".format(self.eid,self.ename,self.sal)
        ##return ("EmpID:%d,EmpName:%s,EmpSal:%g" %(self.eid,self.ename,self.sal))

mc=Emp1(1,"sridhar",10000)
print(mc)

"""__del__() method """

class myclass6():
    def __del__(self):
        print("hello")

c=myclass6()
c1=myclass()

del c,c1 ## del function executes when we destroy an object







 


   
