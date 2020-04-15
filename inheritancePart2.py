""" SUPER() KEYWORD """
""" to invoke parent class method """
class A():
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    def m2(self):
        print("This is m2 method from class B")
        super().m1() ##calling parent class method from child class using SUPER()

b=B()
b.m2()

""" to invoke parent class variables """
class A():
    a,b=10,20
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    i,j=100,200
    def m2(self,x,y):
        print(x+y) ##local variable
        print(self.i+self.j) #child class variable
        print(self.a+self.b) #parent class variable

b=B()
b.m2(1,2)

""" variables with same name """
a,b=1000,2000
class A():
    a,b=10,20
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    a,b=100,200
    def m2(self,a,b):
        print(a+b) ##local variable
        print(self.a+self.b) #child class variable
        print(super().a+super().b) #parent class variable
        print(globals()['a']+globals()['b']) #global variable
bobj=B()
bobj.m2(1,2)

""" to invoke parent class constructor """
class A():
    def __init__(self):
        print("this is from class A constructor")

class B(A):
    def __init__(self):
        print("this is from class B constructor")
        super().__init__() #calls parent class constructor method1
        A.__init__(self) #calls parent class constructor method2

bobj=B()




