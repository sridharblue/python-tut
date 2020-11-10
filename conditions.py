a = 100
if a%2==0:
    print("even number")
else:
    print("odd number")

person = 'George'

if person == 'Sammy':
    print('Welcome Sammy!')
elif person =='George':
    print('Welcome George!')
else:
    print("Welcome, what's your name?")

#single line
print("even number") if a%2==0 else print("odd number")


#For Loop
for a in range(2,10,2):
    print(a)

for a in range(10):
    if a==5:
        continue
    print(a)

list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')

#Tuple unpacking
list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)

for (t1,t2) in list2:
    print(t1)

#Dictionaries
d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)

# Dictionary unpacking
for k,v in d.items():
    print(k)
    print(v)

list(d.keys())
sorted(d.values())

#While Loop 

i=1
while i<=10:
    print(i)
    i=i+1
'''
break, continue, pass
We can use break, continue, and pass statements in our loops to add additional functionality for various cases. The three statements are defined by:

break: Breaks out of the current closest enclosing loop.
continue: Goes to the top of the closest enclosing loop.
pass: Does nothing at all.
'''
string = 'SRIDHAR'
for letter in string:
    if letter == 'D':
        continue
    print(letter)

string = 'SRIDHAR'
for letter in string:
    if letter == 'D':
        break
    print(letter)
print('Broke out of loop')
