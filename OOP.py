#Objects
#In Python, everything is an object.
print(type(1))
print(type([]))
print(type(()))
print(type({}))
#So we know all these things are objects, so how can we create our own Object types? That is where the class keyword comes in.

#class
#User defined objects are created using the class keyword. The class is a blueprint that defines the nature of a future object. From classes we can construct instances.

'''
Attributes
The syntax for creating an attribute is:

self.attribute = something
There is a special method called:

__init__()
This method is used to initialize the attributes of an object
'''

class Person():
    #class object attribute
    species = 'Human'
    #create attributes
    def __init__(self,name,color,number):
        self.name = name
        self.color = color
        self.number = number
    #create methods
    def name_func(self,name):
        print("name is:", name)

    def color_func(self,name):
        print("Name is:",name)
    def all_details(self):
        print(f'Name: {self.name}\nColor: {self.color}\nNumber: {self.number}')
details = Person('sri','blue',21)
print(details.all_details())
# print(details.name_func('sri'))
# print(details.color_func('blue'))

#Methods are functions defined inside the body of a class. They are used to perform operations with the attributes of our objects.
#You can basically think of methods as functions acting on an Object that take the Object itself into account through its self argument.

class Circle:
    #class object attribute
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
        self.area = radius * radius * Circle.pi #we use Circle.pi instead of self.pi, to improve readability

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2

c = Circle()
print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())

c.setRadius(5)
print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())

'''
Inheritance
Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes. 
Important benefits of inheritance are code reuse and reduction of complexity of a program. The derived classes (descendants) override or extend the functionality of base classes (ancestors).
'''
class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dogg(Animal):
    def __init__(self):
        Animal.__init__(self) #calling constructor from parent class
        print("Dog created")

    def whoAmI(self): #modified a method from parent class in child class
        print("Dog - modified in child class")

    def bark(self):
        print("Woof!")

d = Dogg()
print(d)
print(d.whoAmI())
print(d.eat())
print(d.bark())

'''
Polymorphism
We've learned that while functions can take in different arguments, methods belong to the objects they act on. 
In Python, polymorphism refers to the way in which different object classes can share the same method name, 
and those methods can be called from the same place even though a variety of different objects might be passed in.
'''
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!' 
    
niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())

#There a few different ways to demonstrate polymorphism. First, with a for loop:
for pet in [niko,felix]:
    print(pet.speak())

#Another example with functions:
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

#In both cases we were able to pass in different object types, and we obtained object-specific results from the same mechanism.

'''
ABSTRACT classes
A more common practice is to use abstract classes and inheritance. An abstract class is one that never expects to be instantiated. 
For example, we will never have an Animal object, only Dog and Cat objects, although Dogs and Cats are derived from Animals:
'''
class Animal1:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog1(Animal1):
    
    def speak(self):
        return self.name+' says Woof!'
    
class Cat1(Animal1):

    def speak(self):
        return self.name+' says Meow!'
    
fido = Dog1('Fido')
isis = Cat1('Isis')

print(fido.speak())
print(isis.speak())

#Special Methods
'''
 Classes in Python can implement certain operations with special method names. 
 These methods are not actually called directly but by Python specific language syntax.
 '''
class Language():
     
    def __init__(self, name,letters,origin):
        self.name = name
        self.letters = letters
        self.origin =  origin

    def __str__(self): #special method
        return f'{self.name} language has {self.letters} characters and originated from {self.origin}'
    
    def __len__(self):
        return self.letters

    # def __del__(self):
    #     print('Language is deleted')

lang = Language('English', 26, 'England')
print(lang)
print(len(lang))


