#lambda expression
#lambda expressions allow us to create "anonymous" functions. This basically means we can quickly make ad-hoc functions without needing to properly define a function using def.
'''
Function objects returned by running lambda expressions work exactly the same as those created and assigned by defs. There is key difference that makes lambda useful in specialized roles:

lambda's body is a single expression, not a block of statements.

The lambda's body is similar to what we would put in a def body's return statement. We simply type the result as an expression instead of explicitly returning it. Because it is limited to an expression, a lambda is less general that a def. We can only squeeze design, to limit program nesting. lambda is designed for coding simple functions, and def handles the larger tasks.
'''
a = lambda x: x % 2 == 0
print(a(26))

my_list = [0,1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x % 2 == 0, my_list)))

#Lambda expression for grabbing the first character of a string
str_list = ['sri','blue','mars','red']
print(list(map(lambda y: y[0] , str_list)))

#Lambda expression for reversing a string:
str_list = ['sri','blue','mars','red']
print(list(map(lambda y: y[::-1] , str_list)))

#simple ex's
x= lambda a: a + 10
print(x(10))

x= lambda a,b,c: a + b + c
print(x(10,20,30))



