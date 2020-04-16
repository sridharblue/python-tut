""" Accessible only in their own class, starts with two underscores __"""

""" private variable """
class A():
    __a = 10 ##private variable
    b=20
    def m1(self):
        print(self.__a)

obj=A()
obj.m1()

print(A().b)

""" private methods """

class A():
    def __m1(self): ##private method
        print("this is private method")

    def m2(self):
        print("this is public method")

obj=A()
obj.__m1() ## cant access outside class
obj.m2()

""" ACCESSING PRIVATE CLASS INSIDE ITS OWN CLASS"""
class A():
    def __m1(self): ##private method
        print("this is private method")

    def m2(self):
        print("this is public method")
        self.__m1() ##calling private class
obj=A()
#obj.__m1() ## cant access outside class
obj.m2()
 
""" accessing private variables outside of class indirectly using methods"""

class A():
    __empid = 10 ##private variable
    def m1(self,eid):
        self.__empid=eid
        print(self.__empid)

    def m2(self):
        print(self.__empid)

obj=A()
obj.m1(20)
obj.m2()









