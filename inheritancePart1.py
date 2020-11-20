""" 5 types in inheritance 
#   single 
#   multilevel
#   hierarchical
#   multiple
#   hybrid
"""

"""single"""
class A():
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    def m2(self):
        print("This is m2 method from class B")

b=B()
b.m2()
b.m1()

"""multilevel"""
class A1():
    def m1(self):
        print("This is m1 method from class A")

class B1(A1):
    def m2(self):
        print("This is m2 method from class B")

class C1(B1):
    def m3(self):
        print("This is m3 method from class C")

b=B()
b.m2()
b.m1()

c=C1()
c.m3()
c.m2()
c.m1()

""" Hierarchical """
class A2():
    def m1(self):
        print("This is m1 method from class A")

class B2(A2):
    def m2(self):
        print("This is m2 method from class B")

class C2(A2):
    def m3(self):
        print("This is m3 method from class C")

b=B2()
b.m2()
b.m1()

c=C2()
c.m3()
c.m1()

""" multiple """
class A3():
    def m1(self):
        print("This is m1 method from class A")

class B3():
    def m2(self):
        print("This is m2 method from class B")

class C3(A3,B3):
    def m3(self):
        print("This is m3 method from class C")


c=C3()
c.m3()
c.m1()
c.m2()


