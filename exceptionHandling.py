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

""" Raising Exception
    Creating our own exceptions
"""

def enterage(age):
    if age<0:
        raise ValueError("only positive numbers")
    if age % 2 == 0:
        print("even number")
    else:
        print("odd number")

try:
    enterage(-5)
except ValueError:
    print(("only positive numbers are allowed"))
except:
    print(("somethings wrong"))

