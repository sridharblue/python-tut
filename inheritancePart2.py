""" SUPER() KEYWORD """
""" to invoke parent class method """
class A():
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    def m2(self):
        print("This is m2 method from class B")
        super().m1() ##calling parent class method from child class using SUPER()
        A.m1(self) #another way of calling parent class method

b=B()
b.m2()

""" to invoke parent class variables """
class A1():
    a,b=10,20
    def m1(self):
        print("This is m1 method from class A")

class B1(A1):
    i,j=100,200
    def m2(self,x,y):
        print(x+y) ##local variable
        print(self.i+self.j) #child class variable
        print(self.a+self.b) #parent class variable

b=B1()
b.m2(1,2)

""" variables with same name """
a,b=1000,2000
class A2():
    a,b=10,20
    def m1(self):
        print("This is m1 method from class A")

class B2(A2):
    a,b=100,200
    def m2(self,a,b):
        print(a+b) ##local variable
        print(self.a+self.b) #child class variable
        print(super().a+super().b) #parent class variable
        print(globals()['a']+globals()['b']) #global variable
bobj=B2()
bobj.m2(1,2)

""" to invoke parent class constructor """
class A3():
    def __init__(self):
        print("this is from class A constructor")

class B3(A3):
    def __init__(self):
        print("this is from class B constructor")
        super().__init__() #method1: calls parent class constructor
        A3.__init__(self) #method2: calls parent class constructor

bobj=B3()






