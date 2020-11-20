"""  Try Except """

print("this program started")
try:
    print(10/0)
except ZeroDivisionError:
    print("handled ZeroDivisionError")

print("this program ended")


""" try except else """

print("this program started")
try:
    print(10/5)
except TypeError:
    print("handled ZeroDivisionError")
except AttributeError:
    print("handled ZeroDivisionError")
else:
    print("entered into else block") ##this line executes when there is no exception error

print("this program ended")

""" try except else finally"""

print("this program started")
try:
    print(10/0)
except TypeError:
    print("handled ZeroDivisionError")
except ZeroDivisionError:
    print("handled ZeroDivisionError")
else:
    print("entered into else block") ##this line executes when there is no exception error
finally:
    print("entered into finally block") ##finally will always execute
print("this program ended")


#prob 1
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('Invalid operation')

#prob2
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('Invalid Operation')
finally:
    print('All Done')

#prob3
def ask():
    while True:
        try:
            num = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            print(f'Thank you, your number squared is: {num**2}')
            break


""" Raising Exception
    Creating our own exceptions
"""

def enterage(age):
    if age<0:
        raise ValueError()
    if age % 2 == 0:
        print("even number")
    else:
        print("odd number")

try:
    enterage(-2)
except ValueError:
    print(("only positive numbers are allowed"))
except:
    print(("somethings wrong"))

