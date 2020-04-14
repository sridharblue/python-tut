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
class A():
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    def m2(self):
        print("This is m2 method from class B")

class C(B):
    def m3(self):
        print("This is m3 method from class C")

b=B()
b.m2()
b.m1()

c=C()
c.m3()
c.m2()
c.m1()

""" Hierarchical """
class A():
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    def m2(self):
        print("This is m2 method from class B")

class C(A):
    def m3(self):
        print("This is m3 method from class C")

b=B()
b.m2()
b.m1()

c=C()
c.m3()
c.m1()

""" multiple """
class A():
    def m1(self):
        print("This is m1 method from class A")

class B():
    def m2(self):
        print("This is m2 method from class B")

class C(A,B):
    def m3(self):
        print("This is m3 method from class C")


c=C()
c.m3()
c.m1()
c.m2()


