#Timing your code
'''
Sometimes it's important to know how long your code is taking to run, or at least know if a particular line of code is slowing down your entire project. Python has a built-in timing module to do this.
'''
import timeit

c = '-'.join(str(n) for n in range(100))
d = '-'.join([str(n) for n in range(100)])
print(c)
print(timeit.timeit(c, number=10000))
print(timeit.timeit(d, number=10000))
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))

