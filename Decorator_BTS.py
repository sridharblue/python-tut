def sample():
    return 1 

ex = sample
print(ex)
print(ex())
print(sample)
del sample
# print(sample) #deleted from memory using del, 
print(ex()) #Even though we deleted the name sample, the name ex still points to our original function object. 
            #It is important to know that functions are objects that can be passed to other objects!

#functions within fucntions
def main():
    print('this is from main')

    def inside_func1():
        return '\t this is inside_func1'

    def inside_func2():
        return '\t this is inside_func2'

    print(inside_func1())
    print(inside_func2())
    print('Back to the main')

print(main())
# print(inside_func1()) #we cant access this function here, cause it scope is only inside the main function 
# to access a function outside of its scope we have to return that perticular function from main function

#Returning Functions
def welcome(name='tea'):
    print('Tea or Coffee')

    def tea():
        return '\t this is tea function'

    def coffee():
        return f'\t this is coffee function'

    if name.upper() == 'TEA':
        return tea()
    else:
        return coffee()

x = welcome()
print(x)

#another example
def cool():

    def super_cool():
        return 'im super cool'

    return super_cool

c = cool()
print(c()) 

#Functions as Arguments
def name():
    return 'hello my name sridhar'

def deco_func(another_func):
    print('this is the decorator function')
    print(another_func())

deco_func(name)

#Creating a Decorator
def new_decorator(func):
    
    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func")

    return wrap_func

# def func_needs_decorator():
#     print("This function is in need of a Decorator")

# decorated_func = new_decorator(func_needs_decorator) #without using @decorator method
# decorated_func()

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()



