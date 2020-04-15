""" two concepts in Polymorphism
overriding and overloading """

""" overriding variables """

class A():
    name="sri"
    
class B(A):
    #name="blue"
    pass

obj=B()
print(obj.name)

""" overriding methods """

class bank1():
    def RoI(self):
        return 1.5

class bank2(bank1):
    def RoI(self): #overriding RoI method here.
        return 10.5 

obj=bank2()
print(obj.RoI())
obj1=bank1()
print(obj1.RoI())

""" overloading methods """

class A():
    def m1(self,name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("no name")
obj=A()
obj.m1("sridhar")
obj.m1()




